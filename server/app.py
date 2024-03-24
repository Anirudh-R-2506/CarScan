from flask import Flask, jsonify, request
from scanner import getVehicleCount
import base64
import io
from PIL import Image
from flask_cors import CORS

def is_valid_base64_image(image_string):
    try:
        image = base64.b64decode(image_string)
        img = Image.open(io.BytesIO(image))
    except Exception:
        return {
            "error" : "Input is not a valid image",
            "valid" : False,
        }
    if img.format.lower() in ["jpg", "jpeg", "png"]:
        return {
            "valid" : True
        }
    else:
        return {
            "error" : "Input is not of a valid image format",
            "valid" : False,
        }

app = Flask(__name__)
CORS(app)

@app.route("/api/v1/count_vehicles", methods=["POST"])
def count_vehicles():
    img = request.form.get("image");
    if not img:
        return jsonify({
           "status" : 500,
           "message" : "Image string required", 
        })
    isValid = is_valid_base64_image(img)
    if isValid["valid"]:
        return jsonify({
            "status" : 200,
            "data" : getVehicleCount(img),
        })
    else:
        return jsonify({
           "status" : 500,
           "message" : isValid["error"], 
        })

if __name__ == '__main__':
    app.run()