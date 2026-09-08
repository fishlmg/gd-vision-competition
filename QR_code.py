# -*-coding:utf-8 -*-
 
import cv2 as cv
import numpy as np
 
# 加载图片
src_image = cv.imread("data/pictures/tp2/1 (2).png")
# 实例化
qrcoder = cv.QRCodeDetector()
# qr检测并解码
codeinfo, points, straight_qrcode = qrcoder.detectAndDecode(src_image)
# 绘制qr的检测结果
#cv.drawContours(src_image, [np.int32(points)], 0, (0, 0, 255), 2)
#print(points)
# 打印解码结果
print("二维码内容:", codeinfo)
#cv.imshow("result", src_image)
#cv.waitKey()