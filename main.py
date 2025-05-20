from ultralytics import YOLO
import torch

# Check for MPS availability
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

# Load the YOLO model
model = YOLO("models/player_detector.pt")

# Perform prediction
results = model.predict("input_videos/video_1.mp4", save=True, device=device)

# Process results
print(results)
print("================================================")
for box in results[0].boxes:
    print(box)
