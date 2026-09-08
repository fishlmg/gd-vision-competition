import cv2
import numpy as np

# 定义颜色范围（HSV颜色空间）
color_ranges = {
    "red": ([0, 120, 70], [10, 255, 255]),          # 红色范围1
    "red_upper": ([170, 120, 70], [180, 255, 255]), # 红色范围2
    "green": ([36, 25, 25], [70, 255, 255]),        # 绿色范围
    "blue": ([94, 80, 2], [126, 255, 255]),         # 蓝色范围
    "yellow": ([25, 150, 150], [35, 255, 255]),     # 黄色范围
    #"cyan": ([80, 100, 100], [90, 255, 255]),       # 青色范围
    #"purple": ([130, 50, 50], [160, 255, 255]),     # 紫色范围
    #"orange": ([10, 100, 20], [25, 255, 255]),      # 橙色范围
    #"pink": ([160, 100, 100], [170, 255, 255]),     # 粉色范围
    #"brown": ([10, 100, 20], [20, 255, 200]),       # 棕色范围
    #"light_blue": ([94, 50, 50], [126, 255, 255]),  # 浅蓝色范围
    #"gray": ([0, 0, 50], [180, 50, 200]),           # 灰色范围
    #"black": ([0, 0, 0], [180, 255, 50]),           # 黑色范围
    #"white": ([0, 0, 200], [180, 20, 255]),         # 白色范围
    #"light_green": ([35, 100, 100], [85, 255, 255]),# 浅绿色范围
    #"light_yellow": ([20, 100, 100], [30, 255, 255]),# 浅黄色范围
    #"dark_blue": ([100, 150, 0], [140, 255, 255]),  # 深蓝色范围
    #"light_purple": ([130, 50, 50], [170, 255, 255])# 浅紫色范围
}

def detect_and_draw_color(image, color_name, lower, upper):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_image, lower, upper)
    
    # 查找颜色块的轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:  # 过滤掉小面积的噪声
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 绿色框
            
            # 计算文本位置，避免重叠
            text_position = (x, y - 10) if y - 10 > 10 else (x, y + 20)
            cv2.putText(image, color_name, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

# 主函数
if __name__ == "__main__":
    # 读取图像
    image_path = 'data/pictures/color_1.jpg'  # 替换为实际图像文件路径
    image = cv2.imread(image_path)
    output_image = image.copy()

    # 检测并标记颜色块
    for color_name, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        detect_and_draw_color(output_image, color_name, lower, upper)
    
    # 显示结果图像
    cv2.imshow('Detected Colors', output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 保存结果图像
    # cv2.imwrite('output_image.jpg', output_image)