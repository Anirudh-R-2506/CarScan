import cv2
import glob
from vehicle_detector import VehicleDetector
import numpy as np
import base64

def getVehicleCount(imgb64):
    nparr = np.frombuffer(base64.b64decode(imgb64), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    vd = VehicleDetector()
    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)
    for box in vehicle_boxes:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (203, 251, 69), 3)
        cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (203, 251, 69), 3)
    return {
        "image": base64.b64encode(cv2.imencode('.jpg', img)[1]).decode(),
        "count": vehicle_count,
    }