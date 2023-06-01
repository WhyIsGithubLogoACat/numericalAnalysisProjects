import numpy as np
import cv2


def trackbar_callback(x):
    print(x)


def main():
    cap = cv2.VideoCapture(0)

    cv2.namedWindow("Tracking")

    cv2.createTrackbar("LH", "Tracking", 0, 255, trackbar_callback)
    cv2.createTrackbar("LS", "Tracking", 0, 255, trackbar_callback)
    cv2.createTrackbar("LV", "Tracking", 0, 255, trackbar_callback)
    cv2.createTrackbar("UH", "Tracking", 255, 255, trackbar_callback)
    cv2.createTrackbar("US", "Tracking", 255, 255, trackbar_callback)
    cv2.createTrackbar("UV", "Tracking", 255, 255, trackbar_callback)

    while True:
        _, frame = cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        l_h = cv2.getTrackbarPos("LH", "Tracking")
        l_s = cv2.getTrackbarPos("LS", "Tracking")
        l_v = cv2.getTrackbarPos("LV", "Tracking")

        u_h = cv2.getTrackbarPos("UH", "Tracking")
        u_v = cv2.getTrackbarPos("UV", "Tracking")
        u_s = cv2.getTrackbarPos("US", "Tracking")

        lower_bound = np.array([l_h, l_s, l_v])
        upper_bound = np.array([u_h, u_v, u_s])

        mask = cv2.inRange(hsv, lower_bound, upper_bound)

        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("mask", mask)
        cv2.imshow("frame", frame)
        cv2.imshow("res", res)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
