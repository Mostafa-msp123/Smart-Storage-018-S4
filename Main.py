import cv2
import time
import os
from pyzbar.pyzbar import decode
from ultralytics import YOLO
import pandas as pd

model = YOLO('best.pt') 

def process_frame(frame):
    class_counts = {} 

    results = model(frame)
    for box in results[0].boxes:
        cls = int(box.cls)
        coords = box.xyxy[0].tolist()
        if len(coords) == 4:
            x1, y1, x2, y2 = coords
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
            class_name = model.names[cls]
            class_counts[class_name] = class_counts.get(class_name, 0) + 1

    return class_counts, frame

def read_and_save_barcodes(frame, detected_barcodes, detection_interval=3):
    barcodes = decode(frame)
    current_time = time.time()
    
    for barcode in barcodes:
        barcode_data = barcode.data.decode('utf-8')

        if (barcode_data not in detected_barcodes or 
            current_time - detected_barcodes[barcode_data]['last_detected'] > detection_interval):
            
            if barcode_data not in detected_barcodes:
                detected_barcodes[barcode_data] = {'count': 0, 'last_detected': current_time}
            else:
                detected_barcodes[barcode_data]['last_detected'] = current_time

            detected_barcodes[barcode_data]['count'] += 1

            if barcode.rect:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                display_text = f"{barcode_data} ({detected_barcodes[barcode_data]['count']})"
                cv2.putText(frame, display_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

def export_to_csv(detected_barcodes, output_csv='output.csv'):
    file_exists = os.path.isfile(output_csv)
    data = []
    
    for barcode_data, details in detected_barcodes.items():
        data.append({
            'Product Name': barcode_data,
            'Count of Products': details['count']
        })

    df = pd.DataFrame(data)
    df.to_csv(output_csv, mode='a' if file_exists else 'w', header=not file_exists, index=False)

def main(output_csv='output.csv'):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    detected_barcodes = {}
    detection_interval = 3 
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        class_counts, frame = process_frame(frame)
        
        read_and_save_barcodes(frame, detected_barcodes, detection_interval)
        
        cv2.imshow('Barcode and YOLO Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    export_to_csv(detected_barcodes, output_csv)

if __name__ == "__main__":
    main()
