from fastapi import APIRouter, UploadFile, File, HTTPException
import joblib
import numpy as np
import cv2

router = APIRouter()

# Load trained model once
model = joblib.load("models/face_recognition_model.pkl")


@router.post("/recognize-face")
async def recognize_face(file: UploadFile = File(...)):
    try:
        # Read uploaded image
        image_bytes = await file.read()

        # Decode image
        img = cv2.imdecode(
            np.frombuffer(image_bytes, np.uint8),
            cv2.IMREAD_GRAYSCALE
        )

        if img is None:
            raise HTTPException(status_code=400, detail="Invalid image")

        # Resize to training size
        img = cv2.resize(img, (50, 37))

        # Flatten image
        img = img.flatten().reshape(1, -1)

        # Predict
        prediction = model.predict(img)

        return {
            "Recognized Person": str(prediction[0])
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))