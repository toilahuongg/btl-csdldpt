import cv2, os
from hog import compute_hog
from db import getAllCharacters, createImageFeature
from utils import hog_to_str

def createImageFeatures():
    all_character = getAllCharacters()

    for character in all_character:
        # Đường dẫn đến thư mục chứa ảnh
        folder_path = "dataset/"+character.Folder

        # Duyệt qua từng tệp trong thư mục
        for filename in os.listdir(folder_path):
            # Đường dẫn đầy đủ đến tệp ảnh
            image_path = os.path.join(folder_path, filename)

            # Đọc ảnh từ đường dẫn
            image = cv2.imread(image_path)

            # Trích xuất đặc trưng HOG của ảnh
            hog_features = compute_hog(image)

            # Chuyển đổi đặc trưng HOG thành một chuỗi
            hog_features_str = hog_to_str(hog_features)

            createImageFeature(character.ID, '/dataset/'+character.Folder+'/'+filename, hog_features_str)
            