import cv2 #import module opencv
import mediapipe
capture = cv2.VideoCapture(0) #video capture pada device camera pada nomor 0
mediapipehand = mediapipe.solutions.hands #inisialisasi deteksi tanqgan
tangan = mediapipehand.Hands() #variable tangan untuk menyimpan kkonfigurasi deteksi tangan

while True :
    success, img = capture.read() #menyimpan citra tangkapan kamera ke img
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #merubah warna img ke RGB
    result = tangan.process(imgRGB) #melakukan pemrossesan dari citra imgRGB
    if result.multi_hand_landmarks:
        print("tangan")
        cv2.imshow("webcam", img)
        cv2.waitKey(10)
    else :
        print("tidak ada")
        cv2.imshow("webcam", img)
        cv2.waitKey(10)
    if cv2.waitKey(10) & 0xFF == ord('q'):
            break
capture.release()
cv2.destroyAllWindows()

