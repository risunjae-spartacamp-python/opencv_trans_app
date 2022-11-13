import face_recognition
import cv2

original_face_img = "images/man.png"

face_img = face_recognition.load_image_file(original_face_img)
face_landmarks_list = face_recognition.face_landmarks(face_img)

# print(face_landmarks_list)
face_image = cv2.imread(original_face_img)

# 顔全体の座標
# 部位：chin、left_eyebrow、right_eyebrow、nose_bridge、nose_tip、left_eye、right_eye、top_lip、bottom_lip
# print(face_landmarks_list[0])

# 顎の座標
print(face_landmarks_list[0]["chin"])
for chin_cordinate in face_landmarks_list[0]["chin"]:
    cv2.drawMarker(
        face_image,
        chin_cordinate,
        color=(255, 0, 0),
        markerType=cv2.MARKER_CROSS,
        thickness=1,
    )

cv2.imshow("Image", face_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
