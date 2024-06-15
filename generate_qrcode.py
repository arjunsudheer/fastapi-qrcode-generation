from fastapi import FastAPI, Path
from fastapi.responses import FileResponse
import uvicorn
import pyqrcode
from PIL import Image


app = FastAPI()


@app.get("/generate_qrcode")
def generate_qrcode(url: str, logo: bool = True):
    # Create a QR Code with high error tolerance (30%) to accommodate for the logo placed in the center
    qrcode = pyqrcode.create(url, error="H")
    # Save the generated QR Code
    qrcode.png("generated_qrcode.png", scale=10)

    # Add the logo is specified
    if logo:
        # Open the saved QR Code to add the logo in the center
        qrcode_image = Image.open("./generated_qrcode.png")
        qrcode_image = qrcode_image.convert("RGBA")

        # Open the generated QR Code as an image so the logo can be added
        sce_logo = Image.open("./SCE_logo.png")

        # coordinates for the logo to be centered on the QR Code
        box = [135, 135, 235, 235]
        # resize sce_logo
        sce_logo = sce_logo.resize((box[2] - box[0], box[3] - box[1]))

        # place the logo in the center of the QR Code
        qrcode_image.paste(sce_logo, box)
        # Save the QR Code again after the logo has been added
        qrcode_image.save("generated_qrcode.png", scale=10)

    # Display the generated qr code as the FastAPI response
    return FileResponse("generated_qrcode.png")


if __name__ == "__main__":
    uvicorn.run("generate_qrcode:app", port=8000, reload=True)
