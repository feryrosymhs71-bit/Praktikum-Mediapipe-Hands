import cv2
import mediapipe as mp

capture = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

while True:
    success, img = capture.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks and results.multi_handedness:

        for idx, hand in enumerate(results.multi_handedness):

            label = hand.classification[0].label  # "Left" atau "Right"

            if label == "Right":
                cv2.putText(img, "KANAN", (200,50),
                            cv2.FONT_HERSHEY_PLAIN, 3,
                            (255,0,0), 3)

            elif label == "Left":
                cv2.putText(img, "KIRI", (200,100),
                            cv2.FONT_HERSHEY_PLAIN, 3,
                            (0,0,255), 3)

        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Webcam", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
