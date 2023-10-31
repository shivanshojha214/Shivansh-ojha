import cv2
import time
import winsound

def openCamera():
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Error opening camera")
        exit()

    retrieved, frame1 = cam.read()

    if not retrieved:
        print("Error retrieving frame from camera")
        exit()

    # Initialize the counter variable
    i = 0

    while True:
        retrieved, frame2 = cam.read()

        if not retrieved:
            print("Error retrieving frame from camera")
            break

        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        diff = cv2.absdiff(gray1, gray2)

        blur = cv2.GaussianBlur(diff, (5, 5), 0)

        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

        dilated = cv2.dilate(thresh, None, iterations=3)

        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            if cv2.contourArea(c) < 6000:
                continue

            x, y, w, h = cv2.boundingRect(c)

            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

            winsound.Beep(5000, 300)

            cv2.imwrite(f"captured_image{i}.jpg", frame1)
            i += 1

        cv2.imshow("Security Camera", frame1)

        frame1 = frame2.copy()

        if cv2.waitKey(5) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

# Call the function
openCamera()
