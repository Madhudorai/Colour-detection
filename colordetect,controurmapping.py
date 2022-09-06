import cv2
import numpy as np

cap = cv2.VideoCapture(0)
lower_yellow = np.array([15, 150, 20])
upper_yellow = np.array([35, 255, 255])

lower_green = np.array([40, 70, 80])
upper_green = np.array([70, 255, 255])

lower_blue = np.array([90, 60, 0])
upper_blue = np.array([121, 255, 255])

lower_red = np.array([0, 50, 120])
upper_red = np.array([10, 255, 255])

while True:
    success, img = cap.read()
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    yellow_mask = cv2.inRange(image, lower_yellow, upper_yellow)
    green_mask = cv2.inRange(image, lower_green, upper_green)
    blue_mask = cv2.inRange(image, lower_blue, upper_blue)
    red_mask = cv2.inRange(image, lower_red, upper_red)

    y_contours, heirachy = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for y_c in y_contours:
        if cv2.contourArea(y_c) > 500:
            cv2.drawContours(img, y_c, -1, (255,255,255),3) #white contour
            M = cv2.moments(y_c) #use moments to find centre of contour
            cx= int(M["m10"]/ M["m00"])
            cy = int(M["m01"]/M["m00"])
            cv2.circle(img, (cx,cy), 7, (0,0,0),-1) #black circle
            cv2.putText(img,"Yellow",(cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0),3)

    g_contours, heirachy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for g_c in g_contours:
        if cv2.contourArea(g_c) > 500:
            cv2.drawContours(img, g_c, -1, (255, 255, 255), 3)  # white contour
            M = cv2.moments(g_c)  # use moments to find centre of contour
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(img, (cx, cy), 7, (0, 0, 0), -1)  # black circle
            cv2.putText(img, "Green", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)

    b_contours, heirachy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for b_c in b_contours:
        if cv2.contourArea(b_c) > 500:
            cv2.drawContours(img, b_c, -1, (255, 255, 255), 3)  # white contour
            M = cv2.moments(b_c)  # use moments to find centre of contour
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(img, (cx, cy), 7, (0, 0, 0), -1)  # black circle
            cv2.putText(img, "Blue", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)

    r_contours, heirachy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for r_c in r_contours:
        if cv2.contourArea(r_c) > 500:
            cv2.drawContours(img, r_c, -1, (255, 255, 255), 3)  # white contour
            M = cv2.moments(r_c)  # use moments to find centre of contour
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(img, (cx, cy), 7, (0, 0, 0), -1)  # black circle
            cv2.putText(img, "Red", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
