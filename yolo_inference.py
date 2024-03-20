from ultralytics import YOLO

#Load YOLO

model = YOLO("yolov8x")

result = model.predict("input_videos/input_video.mp4",save=True)

print("boxes:")
for box in result[0].boxes:
    print(box)