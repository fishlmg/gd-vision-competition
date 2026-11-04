# GD 视觉识别比赛：二维码与颜色检测

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8.svg)](https://opencv.org/)

2024 年视觉竞赛作品：运行在边缘设备上，通过 OpenCV + pyzbar 实时识别赛场中的**二维码**与**彩色区域**，解码二维码内容、判定颜色方位，为机器人提供导航/任务决策依据；同时集成 YOLO 目标检测并可将结果上报服务器。

## 📷 效果展示

仓库里还没有带检测框的识别结果图（调试输出如 `region_*.jpg` 被 `.gitignore` 排除，且原先就未入库）。`data/pictures/` 只是试跑用的输入样例（二维码、彩色几何图形），不是效果截图。本地跑完 `src/color.py` 后，可以把结果图补到本节。

## ✨ 特性

- **颜色识别**：基于 HSV 颜色空间阈值分割，支持多颜色（红/绿/蓝/黄/橙/紫/粉/青/黑）目标检测
- **二维码识别**：pyzbar 实时解码，输出二维码数据内容
- **调参工具**：交互式 HSV 阈值调整，快速适配不同光照
- **YOLO 检测**：额外集成 YOLO 模型进行目标检测
- **结果上报**：检测结果可 POST 到远程服务器

## 🗂 项目结构

脚本里的相对路径（如 `data/pictures/...`）相对**仓库根目录**。下面的命令都在根目录执行。

### `src/` 正式入口

| 文件 | 功能 |
| --- | --- |
| `src/color.py` | **最终版**颜色识别主程序 |
| `src/QR_code.py` | 二维码检测与解码（OpenCV `QRCodeDetector`） |
| `src/t-col.py` | HSV 颜色阈值调参工具 |
| `src/picture.py` | 按行列切分图像并保存子图 |
| `src/rtp.py` | YOLO 实时检测 + 结果上报 |

### `archive/` 迭代草稿

| 文件 | 功能 |
| --- | --- |
| `archive/color1.py` / `archive/color_fd.py` | 基于 `color.py` 的颜色识别迭代 |
| `archive/qrc_fd.py` | 按颜色掩膜筛选后再解码二维码 |
| `archive/qrcode_fd.py` | 批量扫描目录中的二维码 |
| `archive/ewm.py` | pyzbar 解码，并对照授权名单标记 |
| `archive/1.py` | 二维码读取基础示例 |
| `archive/tp.py` | 检测框文字避让试验 |
| `archive/tp1.py` / `archive/test.py` | 分割与取色调试 |

### `notes/` 与 `tools/`

| 文件 | 功能 |
| --- | --- |
| `notes/BGR.txt` / `notes/HSV.txt` | 颜色空间阈值参考笔记 |
| `notes/explain.txt` | 版本说明：`color.py` 为最终版 |
| `tools/movie.py` | 原无扩展名文件 `movie`：moviepy 视频裁剪脚本（见下） |

样例图片在 `data/pictures/`。

## 🚀 快速开始

```bash
pip install -r requirements.txt
```

```bash
# 颜色识别（最终版）
python src/color.py

# 二维码识别
python src/QR_code.py

# HSV 阈值调参
python src/t-col.py
```

`tools/movie.py` 用 moviepy 按起止时间裁剪视频，不在比赛主流程里，也未写入 `requirements.txt`。需要时另装 `moviepy`，并改脚本底部的输入路径与时间后再运行：

```bash
pip install moviepy
python tools/movie.py
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

调试输出的截图（`region_*.jpg` 等）不包含在仓库中（`.gitignore` 已排除根目录图片）。`src/rtp.py` 在仓库根目录读取 `设备配置.txt` 的设备编号，并向脚本里的服务器地址 POST 检测结果；模型权重路径写在脚本内，权重文件不入库。

## 📄 许可证

[MIT License](LICENSE)
