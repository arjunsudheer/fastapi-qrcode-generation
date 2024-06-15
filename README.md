# FastAPI QRCode Generation

Given a specified url, the generate_qrcode.py script will generate a QR Code and display it as a FastAPI response at the /generate_qrcode/ endpoint.

## Running the script

To run the generate_qrcode.py script, run this command in your terminal:
```
python3 generate_qrcode.py
```

You should receive a link to localhost on port 8000. Open that link in your browser, and visit this endpoint:
```
http://127.0.0.1:8000/generate_qrcode?url="https://sce.sjsu.edu/"
```

By default, the SCE logo will be placed at the center of the QR Code. If you don't want the logo in the center, you can pass a query parameter of logo=0 as shown below:
```
http://127.0.0.1:8000/generate_qrcode?url="https://sce.sjsu.edu/"&logo=0
```

To generate a QR Code from any other webpage, you can change the url query parameter to any url you would like.