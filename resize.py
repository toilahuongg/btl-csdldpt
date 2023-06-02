
# !pip install imageio scikit-image
import numpy as np
import os
from skimage.transform import resize
import imageio

folder_path = "ImagesCartoon"
output_folder_path = 'dataset'

for folder in os.listdir(folder_path):
  # Kích thước mới mong muốn (width, height)
  input_folder = folder_path+'/'+folder
  output_folder = output_folder_path+'/'+folder
  new_size = (128, 128)
  if not os.path.isdir(input_folder): continue
  if not os.path.exists(output_folder):
      os.makedirs(output_folder)
  # Duyệt qua tất cả các file trong thư mục
  for filename in os.listdir(input_folder):
      # Kiểm tra định dạng file hợp lệ (chỉ xử lý các định dạng hình ảnh)
      if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
          # Đường dẫn đầy đủ tới file ảnh
          image_path = os.path.join(input_folder, filename)
          
          # Đọc ảnh
          image = imageio.imread(image_path)
          
          # Resize ảnh
          resized_image = resize(image, new_size)
          
          # Chuyển đổi ảnh từ float64 sang uint8
          resized_image = (resized_image * 255).astype(np.uint8)
          # os.remove(image_path)
          # Đổi tên file thành định dạng .png
          new_filename = os.path.splitext(filename)[0] + '.png'
          new_image_path = os.path.join(output_folder, new_filename)
        
          
          # Lưu ảnh đã resize lại với định dạng .png và cùng tên file
          imageio.imsave(new_image_path, resized_image)