import cv2

def remove_background(input_image_path, output_image_path):
    # Load the image with a colored background
    image = cv2.imread(input_image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLORBGR2GRAY)

    # Apply a threshold to create a binary image (black background, white foreground)
    , binary_image = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARYINV)

    # Find contours in the binary image
    contours,  = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask to remove the background
    mask = cv2.drawContours(binary_image, contours, -1, (0, 0, 0), thickness=cv2.FILLED)

    # Apply the mask to the original image
    result = cv2.bitwise_and(image, image, mask=mask)

    # Save the output image
    cv2.imwrite(output_image_path, result)

if name == "main":
    input_image_path = "input_image.jpg"   # Replace this with the path to your input image
    output_image_path = "C:\\Desktop\\*.png" # Replace this with the desired output path
    remove_background(input_image_path, output_image_path) import os
from flask import Flask, render_template, request, redirect, url_for
import cv2

app = Flask(name)

def remove_background(input_image_path, output_image_path):
    # Your existing background removal code goes here

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Check if the POST request contains a file
        if "image" not in request.files:
            return redirect(request.url)

        file = request.files["image"]

        # Check if the file has a valid name
        if file.filename == "":
            return redirect(request)

        # Save the uploaded file to a temporary location
        temp_image_path = "temp_image.jpg"
        file.save(temp_image_path)

        # Process the uploaded image and save the result to the output location
        output_image_path = "output_image.jpg"
        remove_background(temp_image_path, output_image_path)

        # Remove the temporary file
        os.remove(temp_image_path)

        # Redirect to the result page
        return redirect(url_for("result"))

    return render_template("index.html")

@app.route("/result")
def result():
    return render_template("result.html")

if name == "main":
    app.run(debug=True)