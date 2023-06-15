---
# Dice Counter with Webcam - An Interactive Open House Project

This project is a simple demonstration of using a webcam and computer vision in Python to count the number of spots on dice rolled inside a box. It was created as part of an Open House event to engage with high school students and younger at the University of Florida.

## Project Overview

The project uses a webcam situated two feet above a box into which dice are rolled. The Python script captures the video stream from the webcam, detects the black spots on the dice using a blob detection algorithm, and counts the total number of spots.

## How It Works

1. **Capture**: The script captures the video stream from the webcam using the OpenCV library's VideoCapture function.

2. **Detection**: The script uses a blob detection algorithm to detect the spots on the dice. The algorithm is configured to consider filled, circular blobs that are below a certain size.

3. **Counting**: The script counts the total number of detected blobs (spots on dice) in each frame and displays this count on the frame.

4. **Display**: The script continuously displays the video frames with the detected blobs drawn as circles and the count of blobs.

## Dependencies

The script uses the following Python libraries:

- OpenCV (cv2): For capturing the video stream, detecting blobs, and displaying the video frames.
- Numpy: For array operations.

## Running the Script

To run the script, simply execute the Python file in your terminal as follows:

```bash
python dice_counter.py
```

To stop the script, press the 'q' key while the video window is active.

---

This project is meant to be a simple, interactive way to learn how to use a webcam and apply computer vision in Python. It provides a practical example of how computer vision can be used to detect and count objects in a video stream. Enjoy exploring this project and learning about computer vision!
