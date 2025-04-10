# Hugging Face 模型下载器使用说明

## 功能简介
本程序是一个基于PyQt5的图形界面工具，用于从Hugging Face Hub下载模型文件。主要功能包括：
- 指定模型ID下载
- 自定义缓存目录和保存目录
- 实时显示下载状态
- 错误提示和成功通知

## 安装步骤
1. 确保已安装Python 3.6或更高版本
2. 安装依赖库：
```
pip install PyQt5 huggingface-hub
```
3. 下载程序文件 `huggingface_lfs-down.py`

## 使用方法
1. 运行程序：
```
python huggingface_lfs-down.py
```
2. 在界面中输入以下信息：
   - 模型ID：如 `bert-base-chinese`
   - 缓存目录：临时存储下载文件的目录，如 `./models`
   - 保存目录：最终保存模型的目录，如 `./bert-model`
3. 点击"开始下载"按钮
4. 等待下载完成，程序会显示下载状态和结果

## 常见问题
### 1. 下载失败怎么办？
- 检查模型ID是否正确
- 确保网络连接正常
- 检查是否有足够的磁盘空间
- 查看错误提示信息

### 2. 如何获取模型ID？
访问Hugging Face官网(https://huggingface.co)，找到需要的模型，复制其页面URL中的模型名称部分。

### 3. 下载速度慢怎么办？
- 检查网络连接
- 尝试更换网络环境
- 使用代理服务器（如需）

## 注意事项
- 请确保有足够的磁盘空间存放模型文件
- 大型模型下载可能需要较长时间
- 下载过程中请不要关闭程序窗口
- 缓存目录和保存目录建议使用不同路径
