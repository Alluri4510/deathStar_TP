from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import uvicorn
import os
import shutil
import subprocess

fourth_index = None
cropped_image_folder = None
    
app = FastAPI()
@app.get("/")
def root():
    return {"message": "Welcome to the Rebel App!"}

@app.get("/images/{image_index}")
def get_image(image_index: str):
    image_path = os.path.join(cropped_image_folder, fourth_prefix + image_index + ".png")
    print(image_path)

    if not os.path.exists(image_path):
        raise HTTPException(status_code=404, detail="Image not found")

    return FileResponse(image_path, media_type="image/png")

'''
This is the master program to be executed on the server at test time. It takes
a high-level approach and performs each protocol separately. For more information
on each protocol, please access "Software Granular Description" on Lucidchart
'''
if __name__ == "__main__":
    
    # Cropped files will appear with this prefix conjoined to their ID in the specified destination folder
    fourth_prefix = "DeathStar_"
    cropped_image_folder = "DeathStar/"
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
