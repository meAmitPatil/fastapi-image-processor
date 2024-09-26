# FastAPI Image Processor

A FastAPI service that allows users to upload images and download rotated versions of them.

## Endpoints
- `POST /upload/`: Upload an image.
- `GET /download/{filename}`: Download the processed image.

## Setup

1. Clone the repository:

   ```
   git clone https://github.com/your-username/fastapi-image-processor.git
   ```

2. Install dependencies:

   ```
   pip install fastapi uvicorn pillow
   ```

3. Run the FastAPI server:

   ```
   uvicorn main:app --reload
   ```

4. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the FastAPI docs and test the endpoints.

