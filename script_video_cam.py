from ultralytics import YOLO
import cv2

def main():
    model = YOLO('model/')

    video_path = './'
    cap = cv2.VideoCapture(video_path)

    ret = True
    while ret:
        ret, frame = cap.read()
        if not ret:
            print("Error: failed to capture image")
            break

        results = model.track(frame, persist=True)

        frame_ = results[0].plot()

        cv2.imshow('frame', frame_)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()

if __name__ == '__main__':
    main()