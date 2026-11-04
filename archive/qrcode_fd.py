# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np
import os

# 获取文件夹中的所有图片文件
image_folder = 'data/pictures'  # 替换为实际的图像文件夹路径
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

# 实例化QRCodeDetector对象
qrcoder = cv.QRCodeDetector()

for image_file in image_files:
    # 构建图片文件的完整路径
    image_path = os.path.join(image_folder, image_file)
    
    # 加载图片
    src_image = cv.imread(image_path)
    
    if src_image is None:
        print(f"无法加载图像: {image_path}")
        continue
    
    # 检测并解码二维码
    codeinfo, points, straight_qrcode = qrcoder.detectAndDecode(src_image)
    
    if points is not None:
        # 打印二维码角点坐标
        print(f"图像: {image_file}")
        print("二维码角点坐标:", points)
        
        # 打印解码结果
        print("二维码内容:", codeinfo)
    else:
        print(f"未检测到二维码: {image_file}")

# 关闭所有OpenCV窗口（虽然不再显示图像，但为了防止有残留窗口）
cv.destroyAllWindows()
