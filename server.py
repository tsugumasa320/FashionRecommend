from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import numpy as np
import cv2
from datetime import datetime
import os
import string
import random
import X1_imageRetrieval

SAVE_DIR = "./static"
if not os.path.isdir(SAVE_DIR):
    os.mkdir(SAVE_DIR)

app = Flask(__name__, static_url_path="")

def random_str(n):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])

@app.route('/')
def index():
    return render_template('index.html', images=os.listdir(SAVE_DIR)[::-1])

@app.route('/images/<path:path>')
def send_js(path):
    print(path)
    return send_from_directory(SAVE_DIR, path)

# reference:https://qiita.com/yuuuu3/items/6e4206fdc8c83747544b
@app.route('/upload', methods=['POST'])
def upload():
    if request.files['image']:
    
        if request.method == 'POST':
            # uploadfile save
            f = request.files['image']
            dataname = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
            filepath = "./static/" + dataname
            f.save(filepath)
            #ml
            X1_imageRetrieval.fff(filepath)


        return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8888)