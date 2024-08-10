import customtkinter as ctk
import numpy as np
import cv2
from PIL import ImageGrab
from win32api import GetSystemMetrics
import threading
import time

def print_intro():
    """Prints the introductory message for the application."""
    print('''\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$                                                     $
$                                                     $
$                    RecorderX                        $
$                                                     $
$           Created By: Priyanshu Jindal              $
$           Github ID: jindalpriyanshu101             $
$                                                     $
$                                                     $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n''')

def setup_ui():
    """Sets up the user interface of the application."""
    global file_name_entry, custom_key_entry, record_button, stop_button, status_label

    app = ctk.CTk()
    app.title("Screen Recorder")
    app.geometry("512x312")  # Set window size

    # Style configuration
    padding = 10
    font_large = ("Helvetica", 16, "bold")
    font_small = ("Helvetica", 12)
    button_color = "#1f6aa5"
    text_color = "#f0f0f0"

    # File name entry
    ctk.CTkLabel(app, text="Output file name (with extension):", font=font_small, text_color=text_color).pack(pady=padding)
    file_name_entry = ctk.CTkEntry(app, width=300)
    file_name_entry.pack(pady=padding)

    # Custom key entry
    ctk.CTkLabel(app, text="Custom stop key (optional, default is 'q'):", font=font_small, text_color=text_color).pack(pady=padding)
    custom_key_entry = ctk.CTkEntry(app, width=300)
    custom_key_entry.pack(pady=padding)

    # Start and Stop buttons
    button_frame = ctk.CTkFrame(app)
    button_frame.pack(pady=padding)

    record_button = ctk.CTkButton(button_frame, text="Start Recording", command=start_recording, fg_color=button_color, font=font_large)
    record_button.grid(row=0, column=0, padx=padding)

    stop_button = ctk.CTkButton(button_frame, text="Stop Recording", command=stop_recording, state=ctk.DISABLED, fg_color=button_color, font=font_large)
    stop_button.grid(row=0, column=1, padx=padding)

    # Status label
    status_label = ctk.CTkLabel(app, text="Ready to record", font=font_small, text_color=text_color)
    status_label.pack(pady=padding)

    return app

def start_recording():
    """Starts the screen recording."""
    global recording, output, key

    file_name = file_name_entry.get().strip()
    if not file_name:
        status_label.configure(text="Please enter a valid file name.", text_color="red")
        return

    key = custom_key_entry.get().strip() or 'q'  # Default to 'q' if no key is entered

    # Video writer setup
    try:
        screen_width = GetSystemMetrics(0)
        screen_height = GetSystemMetrics(1)
        resolution = (screen_width, screen_height)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        output = cv2.VideoWriter(file_name, fourcc, 20.0, resolution)  # Adjusted frame rate to 20 FPS
    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}", text_color="red")
        return

    recording = True
    record_button.configure(state=ctk.DISABLED)
    stop_button.configure(state=ctk.NORMAL)
    status_label.configure(text="Recording...", text_color="white")

    def recorder_thread():
        """Thread function to capture and record the screen."""
        prev_time = time.time()
        while recording:
            try:
                # Capture the screen
                img = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
                img_np = np.array(img)
                img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

                # Write the frame to the video file
                output.write(img_final)

                # Show the recording window
                cv2.imshow('RecorderX - Screen Recorder', img_final)

                # Wait for the stop key or 10 milliseconds
                if cv2.waitKey(10) == ord(key):
                    break

                # Ensure the loop runs at the correct frame rate
                time_elapsed = time.time() - prev_time
                sleep_time = max(1./20. - time_elapsed, 0)  # Adjusted for 20 FPS
                time.sleep(sleep_time)
                prev_time = time.time()

            except Exception as e:
                status_label.configure(text=f"Error: {str(e)}", text_color="red")
                break

        cv2.destroyAllWindows()
        output.release()
        status_label.configure(text="Recording stopped", text_color="white")
        record_button.configure(state=ctk.NORMAL)
        stop_button.configure(state=ctk.DISABLED)

    threading.Thread(target=recorder_thread).start()

def stop_recording():
    """Stops the screen recording."""
    global recording
    recording = False

if __name__ == "__main__":
    print_intro()
    app = setup_ui()
    recording = False
    output = None
    key = 'q'
    app.mainloop()
