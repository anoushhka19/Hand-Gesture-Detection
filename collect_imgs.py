import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

# Use camera index 0, try 1 or 2 if 0 doesn't work
cap = cv2.VideoCapture(0)  # Start with camera index 0

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video device")
    exit()

# Set resolution for the camera (optional but can be helpful)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print(f'Collecting data for class {j}')

    # Wait for user to be ready
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Display the frame
        cv2.putText(frame, 'Ready? Press "Q" to start :)', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
        cv2.imshow('frame', frame)

        # Wait for 'q' to start capturing
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Capture and save dataset_size images
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow('frame', frame)

        # Save the captured frame
        img_path = os.path.join(class_dir, f'{counter}.jpg')
        cv2.imwrite(img_path, frame)
        print(f"Saved image: {img_path}")

        counter += 1

        # Wait for 1 ms between frames
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
