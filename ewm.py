import cv2
from pyzbar.pyzbar import decode

# 读取文件
def Read():
    global Data_Array
    Data_Array = open('Authorited.txt').read().splitlines()

# 判断二维码是否授权
def Judge(data):
    global color
    if data in Data_Array:
        color = (0, 255, 0)  # 绿色标记
    else:
        color = (0, 0, 255)  # 红色标记

# 检测图像中的码（解码）
def Read_Decode_Pic(image):
    for code in decode(image):
        data = code.data.decode('utf-8')
        Judge(data)
        pts_poly = np.array(code.polygon, np.int32)
        cv2.polylines(image, [pts_poly], True, color, 5)

# 主函数
if __name__ == "__main__":
    image = cv2.imread('qrcode.jpg')
    Read_Decode_Pic(image)
    cv2.imshow('Result', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()