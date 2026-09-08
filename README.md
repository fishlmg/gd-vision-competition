# GD 视觉识别比赛：二维码与颜色检测（2024.5.25）

OpenCV 视觉竞赛代码：识别场地上的二维码与彩色区域，计算方位并输出检测结果，同时支持通过 YOLO 进行目标检测并上报。

## 文件说明

| 文件 | 功能 |
| --- | --- |
| `color.py` | **最终版**：颜色识别主程序 |
| `color1.py` / `color_fd.py` | 颜色识别迭代版本（基于 color.py） |
| `t-col.py` | HSV 颜色阈值调参工具 |
| `QR_code.py` / `qrcode_fd.py` / `qrc_fd.py` / `ewm.py` | 二维码检测与解码（pyzbar） |
| `picture.py` | 图片采集 / 处理 |
| `rtp.py` | YOLO 实时检测 + 结果上报服务器 |
| `1.py` / `tp.py` / `tp1.py` / `test.py` | 功能测试与调试脚本 |

## 快速开始

```bash
pip install -r requirements.txt

# 颜色识别（最终版）
python color.py

# 二维码识别
python QR_code.py
```

## 说明

- 检测输出的调试图（`region_*.jpg` 等）不入库
- 上报地址通过环境变量配置，代码中无硬编码
