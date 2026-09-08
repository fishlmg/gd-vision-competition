import cv2
import numpy as np
import os

# 定义颜色范围（HSV颜色空间）
color_ranges = {
    "red": ([0, 120, 70], [10, 255, 255]),          # 红色范围1
    "red_upper": ([170, 120, 70], [180, 255, 255]), # 红色范围2
    "green": ([36, 25, 25], [70, 255, 255]),        # 绿色范围
    "blue": ([94, 80, 2], [126, 255, 255]),         # 蓝色范围
    "yellow": ([25, 150, 150], [35, 255, 255])      # 黄色范围
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
            box_color = (0, 0, 0)  # 黑色框
            cv2.rectangle(image, (x, y), (x + w, y + h), box_color, 2)  # 黑色框,2：边框厚度是 2 像素
            
            # 尝试多个位置以避免重叠
            text_positions = [
                (x, y - 10),  # 框上方
                (x, y + h + 20),  # 框下方
                (x + w + 10, y + h + 20),  # 框右下方
                (x + w + 10, y),  # 框右侧
                (x - 50, y),  # 框左侧
                (x, y + h + 40),  # 框下方更多
                (x + w + 10, y + h + 40)  # 框右下更多
            ]
            
            for pos in text_positions:
                text_width = 50  # 假设文本宽度
                text_height = 10  # 假设文本高度
                if (pos[0] >= 0 and pos[0] + text_width <= image.shape[1] and
                    pos[1] >= 0 and pos[1] + text_height <= image.shape[0]):
                    cv2.putText(image, color_name, pos, cv2.FONT_HERSHEY_SIMPLEX, 0.5, box_color, 1)
                    break

def process_images_in_directory(directory):
    # 遍历目录中的所有图像文件
    for filename in os.listdir(directory):
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
            image_path = os.path.join(directory, filename)
            image = cv2.imread(image_path)
            if image is None:
                continue
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

            # 保存结果图像（可选）
            #output_path = os.path.join(directory, 'processed_' + filename)
            #cv2.imwrite(output_path, output_image)

# 主函数
if __name__ == "__main__":
    # 设置图像目录路径
    image_directory = 'data/pictures/tp'  # 替换为实际图像目录路径
    process_images_in_directory(image_directory)
