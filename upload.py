import os
from flask import Flask, render_template, request, redirect
from PIL import Image
import time

app = Flask(__name__)

#UPLOAD_FOLDER = os.path.basename('img')
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    img = Image.open(file).convert('L')
    timestr = time.strftime("%Y%m%d-%H%M%S")
    img.save('img/' + timestr + 'grey.png')
    #f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    
    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    #file.save(f)

    return redirect("/", code=302)
    
if __name__ == "__main__":
    app.run(debug=True)