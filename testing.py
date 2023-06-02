import joblib,os
import cv2
from hog import compute_hog
from db import getImagesByHOG, getFeaturesByCharacter
image = cv2.imread('pluto18.png')

folder_path = "dataset/aladdin-abu";
clf = joblib.load('svm_model.pkl')

# Duyệt qua từng tệp trong thư mục
for filename in os.listdir(folder_path):
    # Đường dẫn đầy đủ đến tệp ảnh
    image_path = os.path.join(folder_path, filename)

    # Đọc ảnh từ đường dẫn
    image = cv2.imread(image_path)

    # Trích xuất đặc trưng HOG của ảfnh
    hog_features = compute_hog(image)
    pred = clf.predict([hog_features])
    if not (int(pred[0]) == 1): print(image_path)


