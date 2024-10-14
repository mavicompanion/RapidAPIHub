import os
from flask import Flask, render_template, request, redirect, url_for
import cv2
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Define folder to save uploaded images
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Function to check if file extension is valid
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to upload and process image
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Process image with OpenCV
        img = cv2.imread(filepath)
        processed_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Save the processed image
        processed_filename = 'processed_' + filename
        processed_filepath = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
        cv2.imwrite(processed_filepath, processed_image)

        # Redirect to display the uploaded and processed images
        return render_template('index.html', uploaded_image=filename, processed_image=processed_filename)

    return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)
