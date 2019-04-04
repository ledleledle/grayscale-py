import os
from flask import Flask, render_template, request, redirect, send_from_directory, url_for, flash
from PIL import Image
import time

app = Flask(__name__)
app.secret_key = "hesoyamuzumymwjcnruad"

@app.route('/')
def uindex():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    img = Image.open(file).convert('L')
    timestr = time.strftime("%Y%m%d-%H%M%S")
    img.save('img/' + timestr + 'grey.png')
    flash('Gambar Berhasil Di Convert!')
    return redirect("/", code=302)
    
@app.route('/img/<filename>')
def send_image(filename):
    return send_from_directory("img", filename)

@app.route('/gallery')
def get_gallery():
    image_names = os.listdir('img')
    print(image_names)
    return render_template("gallery.html", image_names=image_names)

if __name__ == "__main__":
    app.run(debug=True)