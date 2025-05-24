import torch
import cv2uhkk
import numpy as np

# Load YOLOv5 modelz
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
model.conf = 0.5

# Initialize webcam
cap = cv2.VideoCapture(0)

# Constants
pickup_origin = (0, 20, 0)  # Robot base center
pickup_range_x = (-15, 15)  # in cm
pickup_range_y = (10, 20)  # Front of the robot
drop_radius = 25  # cm spacing around robot base
angle_step = 60   # Degrees between each drop point

# Track drop-off zones and one active object
drop_points = {}
current_target = None
cooldown = 0

def map_to_xyz(cx, cy, frame_width, frame_height):
    # Map camera coords to real-world pickup area (assumes top-down view)
    x_cm = np.interp(cx, [0, frame_width], [pickup_range_x[0], pickup_range_x[1]])
    y_cm = np.interp(cy, [frame_height, 0], [pickup_range_y[0], pickup_range_y[1]])
    z_cm = 0  # Flat surface
    return round(x_cm, 2), round(y_cm, 2), z_cm

def assign_drop_point(label):
    if label in drop_points:
        return drop_points[label]
    angle = len(drop_points) * angle_step
    x = round(np.cos(np.radians(angle)) * drop_radius, 2)
    y = round(np.sin(np.radians(angle)) * drop_radius, 2)
    drop_points[label] = (x, y, 0)
    return drop_points[label]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_h, frame_w = frame.shape[:2]
    results = model(frame)
    detections = results.xyxy[0]

    if cooldown > 0:
        cooldown -= 1
    else:
        current_target = None

    for *box, conf, cls in detections:
        label = model.names[int(cls)]
        x1, y1, x2, y2 = map(int, box)
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        x, y, z = map_to_xyz(cx, cy, frame_w, frame_h)

        if current_target is None:
            current_target = {'label': label, 'pickup': (x, y, z)}
            drop_xyz = assign_drop_point(label)
            print(f"[PICK] {label} at {x,y,z}")
            print(f"[DROP] {label} → Drop at {drop_xyz}")
            cooldown = 90  # Lock for 90 frames (~3s)

        # Draw detections
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(frame, f'{label} ({round(x)}, {round(y)})', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Detection and Sorting", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




