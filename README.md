# RecorderX

**RecorderX** is a Python-based screen recording tool designed to capture your screen activities with high efficiency and quality. Leveraging libraries like OpenCV, CustomTkinter, and PIL, RecorderX offers a seamless and user-friendly experience, allowing you to record your screen with minimal impact on system performance.

## Features
- **High-Quality Screen Recording:** Capture your screen in high definition, ensuring clear and crisp video output.
- **Real-Time Preview:** Monitor the recording process through a real-time preview window.
- **Custom Stop Key:** Configure a custom key to stop the recording process, or use the default `q` key.
- **User-Friendly Interface:** Intuitive GUI built with CustomTkinter, making it easy for users of all levels to operate.

## Getting Started

### Prerequisites
Before running RecorderX, ensure you have the following Python libraries installed:
- `customtkinter`
- `numpy`
- `opencv-python`
- `Pillow`
- `pywin32`

You can install these dependencies using pip:
```bash
pip install customtkinter numpy opencv-python Pillow pywin32
```

### Running RecorderX
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/RecorderX.git
   cd RecorderX
   ```

2. **Run the Application:**
   ```bash
   python recorderx.py
   ```

3. **Start Recording:**
   - Upon launching RecorderX, a window will prompt you to enter the output file name (e.g., `output.mp4`).
   - You will also have the option to set a custom key to stop the recording.
   - Click the "Start Recording" button to begin capturing your screen.

4. **Stop Recording:**
   - Press the `q` key or your custom stop key in the preview window to stop recording.
   - The recorded video will be saved in the directory from which you ran the script.

## How It Works
RecorderX utilizes the following components:
- **CustomTkinter:** Provides a modern, customizable GUI for the application.
- **OpenCV (`cv2`):** Handles video processing and saving the recorded screen as an MP4 file.
- **PIL (`ImageGrab`):** Captures the screen and converts it into an array for processing.
- **Multithreading:** Ensures the GUI remains responsive during the recording process.

## Limitations
- **Audio Recording:** System audio capture is not supported in this version.
- **Game Recording:** While most desktop activities are captured smoothly, high-performance gaming may not be fully supported.

## Contributing
Contributions to RecorderX are welcome! Here’s how you can contribute:

1. **Fork the Repository:** Click the "Fork" button on the RecorderX GitHub page to create your copy of the repository.
2. **Create a New Branch:** Before making changes, create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Implement Changes:** Make your desired changes, ensuring they are well-tested and documented.
4. **Submit a Pull Request:** Once your changes are ready, push them to your forked repository and submit a pull request. Please include a detailed description of your changes and any relevant testing information.
5. **Collaborate:** Engage with the project maintainers during the review process to get your contributions merged.


## Acknowledgments
- **Programming Hero:** Inspiration for the initial concept of the screen recording functionality.
- **OpenCV, CustomTkinter, PIL:** Key libraries that made the development of RecorderX possible.
