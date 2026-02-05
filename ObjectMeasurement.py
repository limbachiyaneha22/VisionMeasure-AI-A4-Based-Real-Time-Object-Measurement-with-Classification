import cv2
import utlis

# ================= CAMERA =================
cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)

# ================= A4 CONFIG =================
scale = 3
wP = 210 * scale
hP = 297 * scale

while True:
    success, img = cap.read()
    if not success:
        break

    imgContours, conts = utlis.getContours(img, minArea=50000, filter=4)

    if len(conts) != 0:
        biggest = conts[0][2]
        imgWarp = utlis.warpImg(img, biggest, wP, hP)

        imgContours2, conts2 = utlis.getContours(
            imgWarp,
            minArea=2000,
            filter=4,
            cThr=[50,50]
        )

        object_id = 1

        for obj in conts2:
            cv2.polylines(imgContours2, [obj[2]], True, (0,255,0), 2)

            nPoints = utlis.reorder(obj[2])

            width = round(utlis.findDis(
                nPoints[0][0] // scale,
                nPoints[1][0] // scale
            ) / 10, 1)

            height = round(utlis.findDis(
                nPoints[0][0] // scale,
                nPoints[2][0] // scale
            ) / 10, 1)

            x, y, w, h = obj[3]

            # Object ID
            cv2.putText(imgContours2,
                        f"Object {object_id}",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0,0,255),
                        2)

            # Measurements
            cv2.putText(imgContours2,
                        f"W: {width} cm",
                        (x, y + h + 20),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (255,0,255),
                        2)

            cv2.putText(imgContours2,
                        f"H: {height} cm",
                        (x, y + h + 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (255,0,255),
                        2)

            object_id += 1

        # Total objects
        cv2.putText(imgContours2,
                    f"Total Objects: {object_id - 1}",
                    (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0),
                    3)

        cv2.imshow("A4 Measurement", imgContours2)

    imgSmall = cv2.resize(img, (0,0), None, 0.5, 0.5)
    cv2.imshow("Original", imgSmall)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
