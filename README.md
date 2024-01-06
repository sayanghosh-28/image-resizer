# Flask Image Processing App

## Overview

This Python script utilizes the Flask framework to create a web application focused on image upload, processing, and display. It incorporates several key components and functionalities for seamless image manipulation.

## Libraries

- *Flask:* A micro web framework for building web applications.
- *OpenCV (cv2):* Used for image processing tasks.
- *PIL (Image):* Python Imaging Library for working with images.
- *Werkzeug:* Provides utility functions for handling file uploads securely.

## Configuration

The script configures the Flask app, sets a secret key, and defines parameters for file uploads:

python
app = Flask(__name__)
app.secret_key = "super secret key"
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


## File Upload Validation

The allowed_file function ensures that only files with specific extensions are allowed for upload:

python
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


## Image Processing

The processImage function resizes images based on different scaling factors depending on the selected operation:

python
def processImage(filename, operation):
    # Image processing logic for different operations
    # ...


## File Cleanup

The script periodically removes old files from 'uploads' and 'static' directories based on last modification time.

## Flask Routes

### Home Page

python
@app.route("/")
def home():
    return render_template("index.html")


### Login Page

python
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


### Signup Page

python
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')


### Image Editing Page

python
@app.route("/edit", methods=["GET", "POST"])
def edit():
    # Image upload, processing, and flash messages handling
    # ...


## Execution

The Flask app is run with debugging enabled on port 5001:

python
app.run(debug=True, port=5001)


## Conclusion

This application seamlessly integrates Flask to create a versatile web interface for image upload, processing, and presentation. Each section is systematically organized for clarity and comprehension.
