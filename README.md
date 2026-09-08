# GD 视觉识别比赛：二维码与颜色检测

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8.svg)](https://opencv.org/)

2024 年视觉竞赛作品：运行在边缘设备上，通过 OpenCV + pyzbar 实时识别赛场中的**二维码**与**彩色区域**，解码二维码内容、判定颜色方位，为机器人提供导航/任务决策依据；同时集成 YOLO 目标检测并可将结果上报服务器。

## ✨ 特性

- **颜色识别**：基于 HSV 颜色空间阈值分割，支持多颜色（红/绿/蓝/黄/橙/紫/粉/青/黑）目标检测
- **二维码识别**：pyzbar 实时解码，输出二维码数据内容
- **调参工具**：交互式 HSV 阈值调整，快速适配不同光照
- **YOLO 检测**：额外集成 YOLO 模型进行目标检测
- **结果上报**：检测结果可 POST 到远程服务器

## 🗂 项目结构

| 文件 | 功能 |
| --- | --- |
| `color.py` | **最终版**颜色识别主程序 |
| `color1.py` / `color_fd.py` / `qrc_fd.py` | 基于 color.py 的迭代版本 |
| `t-col.py` | HSV 颜色阈值调参工具 |
| `QR_code.py` | 二维码检测与解码（pyzbar） |
| `qrcode_fd.py` / `qrc_fd.py` / `ewm.py` | 二维码识别相关脚本 |
| `picture.py` | 图像采集与预处理 |
| `rtp.py` | YOLO 实时检测 + 结果上报 |
| `1.py` | 二维码读取基础示例 |
| `tp.py` / `tp1.py` / `test.py` | 功能测试与调试脚本 |
| `BGR.txt` / `HSV.txt` | 颜色空间阈值参考笔记 |

## 🚀 快速开始

```bash
pip install -r requirements.txt
```

```bash
# 颜色识别（最终版）
python color.py

# 二维码识别
python QR_code.py

# HSV 阈值调参
python t-col.py
```

> **注意**：pyzbar 在 Linux 上需要系统依赖 `libzbar0`（`sudo apt install libzbar0`）。

## 🧪 技术要点

**颜色分割流程：**

1. BGR → HSV 颜色空间转换
2. `cv2.inRange()` 按阈值生成掩膜
3. 形态学操作去噪（开闭运算）
4. `cv2.findContours()` 提取轮廓
5. 计算目标中心坐标与面积

**二维码识别流程：**

1. 图像灰度化 / 二值化
2. pyzbar `decode()` 定位并解码
3. 输出二维码文本内容与位置

## 📦 依赖

OpenCV、NumPy、pyzbar、requests、ultralytics —— 详见 [requirements.txt](requirements.txt)

## 📝 说明

调试输出的截图（`region_*.jpg` 等）不包含在仓库中（`.gitignore` 已排除）；上报地址通过环境变量配置。

## 📄 许可证

[MIT License](LICENSE)
