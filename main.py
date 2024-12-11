from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
from pathlib import Path
from typing import List

app = FastAPI()

# Mount static files (your frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

# We don't need CORS middleware anymore since frontend and backend are served from same origin
# app.add_middleware(CORSMiddleware, ...)

class FolderRequest(BaseModel):
    folder_path: str

class ImageInfo(BaseModel):
    name: str
    path: str
    description: str = ""
    tags: List[str] = []
    text_content: str = ""

@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

@app.post("/images")
async def get_images(request: FolderRequest):
    folder_path = Path(request.folder_path)
    
    # Check if folder exists
    if not folder_path.exists() or not folder_path.is_dir():
        raise HTTPException(status_code=404, detail="Folder not found")
    
    # Store the current folder path
    app.current_folder = str(folder_path)
    
    # List to store image information
    images = []
    
    # Supported image extensions
    image_extensions = {'.jpg', '.jpeg', '.png', '.webp'}
    
    # Recursively scan for images
    for file_path in folder_path.rglob("*"):
        if file_path.suffix.lower() in image_extensions:
            # Create relative path from the input folder
            rel_path = str(file_path.relative_to(folder_path))
            
            # Create image info
            image_info = ImageInfo(
                name=file_path.name,
                path=rel_path,
                description="",
                tags=[],
                text_content=""
            )
            images.append(image_info)
    
    return {"images": images}

@app.get("/image/{path:path}")
async def get_image(path: str, request: FolderRequest = None):
    try:
        # Get the folder path from the most recent request
        # Note: This is a simplified solution. In a production environment,
        # you might want to store this in a session or database
        if not hasattr(app, 'current_folder'):
            raise HTTPException(status_code=400, detail="No folder selected")
        
        # Combine the base folder path with the relative image path
        full_path = os.path.join(app.current_folder, path)
        
        if not os.path.exists(full_path):
            raise HTTPException(status_code=404, detail="Image not found")
        
        return FileResponse(full_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 
    # or in command line: uvicorn main:app --host 127.0.0.1 --port 8000 --reload
