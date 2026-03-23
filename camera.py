import cv2

def detect_mood():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return "neutral"

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Press Q to capture", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # 👇 yahan user se mood le rahe hain
    mood = input("Enter your mood (happy/sad/stressed): ")
    return mood