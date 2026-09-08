import time
import cv2
from collections import defaultdict
from ultralytics import YOLO
import requests

# 初始化YOLO模型
model = YOLO('/home/pi/Desktop/best.pt')
cap = cv2.VideoCapture(0)

# 从文本文件读取Flask应用程序的地址
with open('设备配置.txt', 'r') as file:
    lines = file.readlines()
    id = lines[0].strip()  # 获取第一行的地址信息并去除空格
    url = f"http://<SERVER_HOST>:8000/update_data_{id}"

while True:
    if not cap.isOpened():
        print('无法打开摄像头')
        break

    ret, frame = cap.read()
    if ret:
        results = model.predict(frame, conf=0.5, save=False, imgsz=640, iou=0.5)
        class_names = model.names
        class_counts = defaultdict(int)

        for result in results:
            boxes = result.boxes
            for i in range(len(boxes)):
                class_index = int(boxes.cls[i])
                class_name = class_names[class_index]
                class_counts[class_name] += 1

        if not class_counts:
            print("未检测到对象")
            class_counts = {"occupied": 0, "available": 0}
        elif len(class_counts) == 1:
            if "occupied" in class_counts:
                class_counts["available"] = 0
            elif "available" in class_counts:
                class_counts["occupied"] = 0

        print(class_counts)

        # 尝试发送POST请求
        try:
            response = requests.post(url, json=class_counts)
            response.raise_for_status()  # 当响应不是200时，抛出HTTPError异常
            print("请求成功")
        except requests.exceptions.RequestException as e:
            print("网络问题无法发送")
            print(f"检测结果: {class_counts}")

    time.sleep(8)

cap.release()
