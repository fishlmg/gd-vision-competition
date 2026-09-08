# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np
import os

def find_largest_qrcode(image):
    qrcoder = cv.QRCodeDetector()
    codeinfo, points, _ = qrcoder.detectAndDecode(image)
    if points is not None:
        return codeinfo, points
    return None, None

def find_color_qrcode(image, color):
    qrcoder = cv.QRCodeDetector()
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    if color == "red":
        mask1 = cv.inRange(hsv, (0, 50, 20), (5, 255, 255))
        mask2 = cv.inRange(hsv, (175, 50, 20), (180, 255, 255))
        mask = cv.bitwise_or(mask1, mask2)
    elif color == "blue":
        mask = cv.inRange(hsv, (110, 50, 50), (130, 255, 255))
    elif color == "green":
        mask = cv.inRange(hsv, (36, 25, 25), (70, 255, 255))
    else:
        mask = cv.inRange(hsv, (0, 0, 0), (180, 255, 30))

    target_image = cv.bitwise_and(image, image, mask=mask)
    codeinfo, points, _ = qrcoder.detectAndDecode(target_image)
    if points is not None:
        return codeinfo
    return None

def process_image(image_path):
    # 加载图片
    src_image = cv.imread(image_path)
    if src_image is None:
        print(f"无法加载图片: {image_path}")
        return

    # 找到最大的二维码
    largest_codeinfo, points = find_largest_qrcode(src_image)

    if largest_codeinfo:
        print(f"图片 {image_path} - 最大的二维码内容:", largest_codeinfo)
        # 根据最大的二维码的内容找到匹配颜色的二维码
        result = find_color_qrcode(src_image, largest_codeinfo.lower())
        if result:
            print(f"图片 {image_path} - 匹配颜色的二维码内容:", result)
        else:
            print(f"图片 {image_path} - 未找到匹配颜色的二维码。")
    else:
        print(f"图片 {image_path} - 未找到任何二维码。")

def process_multiple_images(image_dir):
    for filename in os.listdir(image_dir):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(image_dir, filename)
            process_image(image_path)

# 指定包含图片的文件夹路径
image_directory = "path_to_your_image_directory"

process_multiple_images(image_directory)
