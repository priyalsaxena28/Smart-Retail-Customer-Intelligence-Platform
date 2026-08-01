from fastapi import APIRouter, UploadFile, File, HTTPException
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

router = APIRouter()

MODEL_PATH = "models/product_classifier.h5"
model = load_model(MODEL_PATH)

# Temporary class names
class_names = [
    "Tshirts",
    "Shirts",
    "Casual Shoes",
    "Watches",
    "Sports Shoes",
    "Kurtas",
    "Tops",
    "Handbags",
    "Heels",
    "Sunglasses"
]

@router.post("/predict-product")
async def predict_product(file: UploadFile = File(...)):
    temp_file = "temp_product.jpg"

    try:
        with open(temp_file, "wb") as f:
            f.write(await file.read())

        img = image.load_img(temp_file, target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = img / 255.0

        prediction = model.predict(img, verbose=0)

        predicted_index = int(np.argmax(prediction))
        confidence = float(np.max(prediction))

        print("Prediction Shape:", prediction.shape)
        print("Predicted Index:", predicted_index)
        print("Number of Classes:", len(class_names))

        if predicted_index >= len(class_names):
            return {
                "error": "Invalid class index",
                "Predicted Index": predicted_index
            }

        return {
            "Predicted Category": [predicted_index],
            "Confidence": round(confidence * 100, 2)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)