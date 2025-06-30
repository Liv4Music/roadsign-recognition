import cv2
import torch
import easyocr
import re
import time
import pyttsx3
import subprocess

def run():
    # load model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp/weights/last.pt', force_reload=True)
    
    # Load OCR reader
    reader = easyocr.Reader(['en'], gpu=False)
    
    # Text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    

    # Open webcam
    cap = cv2.VideoCapture(0)  # Use 0 for default webcam
    
    spoken_times = {}

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        current_time = time.time()

        # Run YOLOv5 detection
        results = model(frame)
        detections = results.pandas().xyxy[0]

        for i, row in detections.iterrows():
            label = row['name']
            conf = row['confidence']

            # Filter for specific labels (e.g. 'label', 'sign', etc.)
            if label == 'speedSign' and conf > 0.5:
                x1, y1, x2, y2 = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
                crop = frame[y1:y2, x1:x2]

                # OCR on cropped image
                ocr_result = reader.readtext(crop)

                # Default text label
                number_label = "NaN"

                for (_, text, _) in ocr_result:
                    # Extract first number from OCR result
                    match = re.search(r'\d+', text)
                    if match:
                        number_label = match.group()
                        break  # Use first valid number found
                    
                # Speak if new OR 10+ seconds passed since last spoken
                if number_label != "NaN":
                    last_spoken = spoken_times.get(number_label, 0)
                    if current_time - last_spoken >= 10:
                        statement = f'{number_label} miles per hour'
                        print(f'SPEAKING: {statement}!!!!!!!!!!!!!!!!!!!!!!!!')
                        engine.say(statement)
                        engine.runAndWait()
                        spoken_times[number_label] = current_time

                # Draw bounding box and label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, number_label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # Display frame
        cv2.imshow('YOLOv5 + OCR', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    
def main():
    run()
    
main()
    