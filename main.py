from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from PIL import Image
import os
from io import BytesIO

app = FastAPI()

UPLOAD_DIR = "images/uploaded"
PROCESSED_DIR = "images/processed"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    try:
        file_location = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_location, "wb") as f:
            f.write(await file.read())

        with Image.open(file_location) as img:
            rotated_img = img.rotate(180)
            processed_filename = f"rotated_{file.filename}"
            processed_image_path = os.path.join(PROCESSED_DIR, processed_filename)
            rotated_img.save(processed_image_path)

        return {"filename": processed_filename, "message": "Image uploaded and processed successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download/{filename}")
async def download_image(filename: str):
    file_path = os.path.join(PROCESSED_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="image/jpeg", filename=filename)
    else:
        raise HTTPException(status_code=404, detail="Image not found")

