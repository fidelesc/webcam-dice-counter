import cv2
import numpy as np
import sys

# Constants for blob detector parameters
# This is the maximum area a blob (circle) can occupy in the frame
MAX_BLOB_AREA = 50

# This defines how circular a blob must be to be considered by the detector
MIN_BLOB_CIRCULARITY = 0.7

# Constants for font parameters, these are used to display the count of dice on the video
FONT = cv2.FONT_HERSHEY_SIMPLEX
TEXT_ORIGIN = (20, 80)
FONT_SCALE = 2
FONT_COLOR = (0, 255, 0)
FONT_THICKNESS = 2

def main():
    # Initialize video capture. This opens a video stream from your webcam.
    stream = cv2.VideoCapture(0)

    # Check if the video stream was successfully opened
    if not stream.isOpened():
        print("Error: Could not open video stream.")
        sys.exit()

    # Initialize a blob detector with certain parameters
    params = cv2.SimpleBlobDetector_Params()
    # We only want to consider blobs that are filled (by area)
    params.filterByArea = True
    params.maxArea = MAX_BLOB_AREA
    # We want the blobs to be circular, to filter out non-dice objects
    params.filterByCircularity = True
    params.minCircularity = MIN_BLOB_CIRCULARITY

    # Create the blob detector with the above parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # Create a window to display the video
    cv2.namedWindow('Keypoints', cv2.WND_PROP_FULLSCREEN)
    cv2.moveWindow('Keypoints', 0, 0)
    cv2.setWindowProperty('Keypoints', cv2.WND_PROP_FULLSCREEN,
                            cv2.WINDOW_FULLSCREEN)

    # Continuously capture video until the user hits 'q'
    while True:
        # Capture a single frame
        grabbed, frame = stream.read()

        # End the loop if no frame is captured
        if not grabbed:
            print("Error: Could not read frame from video stream.")
            break

        # Detect blobs (potential dice) in the frame
        keypoints = detector.detect(frame)

        # Draw detected blobs as red circles on the frame.
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of the blob
        im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # Draw the count of detected blobs (dice) on the image
        im_with_keypoints = cv2.putText(im_with_keypoints, 'Count: '+str(len(keypoints)), TEXT_ORIGIN, FONT, FONT_SCALE, FONT_COLOR, FONT_THICKNESS, cv2.LINE_AA)

        # Display the frame with the keypoints and count
        cv2.imshow('Keypoints', im_with_keypoints)

        # End the loop if the user hits 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up after the loop ends
    stream.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
