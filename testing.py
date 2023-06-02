import joblib
import cv2
from hog import compute_hog
from db import getImagesByHOG, getFeaturesByCharacter
image = cv2.imread('pluto18.png')

# Trích xuất đặc trưng HOG của ảnh
hog_features = compute_hog(image)

clf = joblib.load('svm_model.pkl')

pred = clf.predict([hog_features])

print(getImagesByHOG(int(pred[0]), hog_features))

