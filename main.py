from flask import Flask,render_template,request,flash
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import cv2
import numpy as np
from PIL import Image
import time

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key="super secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
def processImage(filename,operation):
    print(f"filename is {filename} and operation is {operation}")
    img=cv2.imread(f"uploads/{filename}")
   
    match operation:
        case "0":
            scale_percent = 80 # percent of original size
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            resized1 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            #resized1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            newfilename=f"static/{filename}"
            cv2.imwrite(newfilename,resized1)
            return newfilename
        case "1":
            scale_percent = 60 # percent of original size
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            resized2 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            newfilename=f"static/{filename}"
            cv2.imwrite(newfilename,resized2)
            return newfilename
        case "2":
            scale_percent = 40 # percent of original size
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            resized3 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            newfilename=f"static/{filename}"
            cv2.imwrite(newfilename,resized3)
            return newfilename
        case "3":
            scale_percent = 20 # percent of original size
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            resized4 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            newfilename=f"static/{filename}"
            cv2.imwrite(newfilename,resized4)
            return newfilename
current_time = time.time()

# Iterate over all the files in the directory
for root, dirs, files in os.walk('.\\uploads'):
    for file in files:
        # Get the last modified time of the file
        last_modified_time = os.path.getmtime(os.path.join(root, file))

        # Delete the file if it is older than the given time
        if current_time - last_modified_time > 60:
            os.remove(os.path.join(root, file))
for root, dirs, files in os.walk('.\\static'):
    for file in files:
        # Get the last modified time of the file
        last_modified_time = os.path.getmtime(os.path.join(root, file))

        # Delete the file if it is older than the given time
        if current_time - last_modified_time > 20:
            os.remove(os.path.join(root, file))
            
            
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


'''@app.route("/button",methods=['POST','GET'])
def button():
    if request.method=='POST':
        if request.form['button']=='success1':
            return render_template("login.html")
        elif request.form['button']=='success2':
            return render_template('signup.html')
        else:
            return 'error'
    else:
        return render_template('index.html')'''

@app.route('/login', methods=['GET','POST'])
def login():
    # Handle login logic here
    #if request.method == 'POST':
    #    return redirect(url_for('signup'))
    return render_template('login.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    # Handle login logic here
    #if request.method == 'POST':
        # process the sign up form
    #   return redirect(url_for('login'))
    return render_template('signup.html')

@app.route("/edit", methods=["GET","POST"])
def edit():
    if request.method=="POST":
        operation = request.form.get("operation")
        if 'file' not in request.files:
            flash('No file part')
            return "error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return "error no file selected"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new=processImage(filename,operation)
            flash(f"your image has been processed and is available <a href='/{new}'target='_blank'>here</a>")
            return render_template("index.html")
    return render_template("index.html")

app.run(debug=True,port=5001)