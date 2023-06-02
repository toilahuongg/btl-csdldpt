from flask import Flask, render_template, request, jsonify
from hog import compute_hog
from setup import setup
from feature import createImageFeatures
import joblib, os, cv2, json, numpy as np
from db import getImagesByHOG, getCharacterByID
from skimage.transform import resize
import imageio

setup()
createImageFeatures()

app = Flask(__name__, static_folder='dataset')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods=['POST'])
def process():
    quantity = int(request.form.get('quantity', 5))
    image = request.files['image']

    clf = joblib.load('svm_model.pkl')
    filename = image.filename
    image.save(filename)
    image = imageio.imread(filename)
    os.remove(filename)

    new_size = (128, 128)
    resized_image = resize(image, new_size)
    resized_image = (resized_image * 255).astype(np.uint8)
    new_filename = os.path.splitext(filename)[0] + '.png'

    imageio.imsave(new_filename, resized_image)
    file = cv2.imread(new_filename)
    os.remove(new_filename)


    hog_features = compute_hog(file)
    clf = joblib.load('svm_model.pkl')
    pred = clf.predict([hog_features])

    characterID = int(pred[0])

    return jsonify({
        "images": getImagesByHOG(characterID, hog_features, quantity),
        "character": getCharacterByID(characterID).__dict__
    })

@app.route('/result/<filename>')
def result(filename):
    return render_template('result.html', filename=filename)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
