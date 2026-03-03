import cv2
import numpy as np
import matplotlib.pyplot as plt

# Get webcam feed
cap = cv2.VideoCapture(0)

while True:
    # Read frame
    ret, frame = cap.read()

    # Display frame
    cv2.imshow('frame', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam
cap.release()

# Close all windows
cv2.destroyAllWindows()