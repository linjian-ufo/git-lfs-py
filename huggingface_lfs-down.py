import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from huggingface_hub import snapshot_download
import os

class DownloadThread(QThread):
    progress = pyqtSignal(str)
    finished = pyqtSignal(bool, str)

    def __init__(self, repo_id, cache_dir, local_dir):
        super().__init__()
        self.repo_id = repo_id
        self.cache_dir = cache_dir
        self.local_dir = local_dir

    def run(self):
        try:
            self.progress.emit('开始下载...')
            repo_path = snapshot_download(
                repo_id=self.repo_id,
                cache_dir=self.cache_dir,
                local_dir=self.local_dir
            )
            self.finished.emit(True, f'下载完成！文件保存在: {repo_path}')
        except Exception as e:
            self.finished.emit(False, f'下载失败: {str(e)}')

class DownloadApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('v:linjian257-Hugging Face 模型下载器v1.0')
        layout = QVBoxLayout()

        # 模型ID输入
        self.repo_label = QLabel('模型ID:')
        self.repo_input = QLineEdit()
        self.repo_input.setPlaceholderText('例如: bert-base-chinese')

        # 缓存目录输入
        self.cache_label = QLabel('缓存目录:')
        self.cache_input = QLineEdit()
        self.cache_input.setPlaceholderText('例如: ./models')

        # 保存目录输入
        self.local_label = QLabel('保存目录:')
        self.local_input = QLineEdit()
        self.local_input.setPlaceholderText('例如: ./bert-model')

        # 状态显示
        self.status_label = QLabel('')
        self.status_label.setAlignment(Qt.AlignCenter)

        # 下载按钮
        self.download_btn = QPushButton('开始下载')
        self.download_btn.clicked.connect(self.start_download)

        # 添加组件到布局
        layout.addWidget(self.repo_label)
        layout.addWidget(self.repo_input)
        layout.addWidget(self.cache_label)
        layout.addWidget(self.cache_input)
        layout.addWidget(self.local_label)
        layout.addWidget(self.local_input)
        layout.addWidget(self.download_btn)
        layout.addWidget(self.status_label)

        self.setLayout(layout)
        self.resize(400, 250)

    def start_download(self):
        repo_id = self.repo_input.text().strip()
        cache_dir = self.cache_input.text().strip()
        local_dir = self.local_input.text().strip()

        if not all([repo_id, cache_dir, local_dir]):
            QMessageBox.warning(self, '警告', '请填写所有必要信息！')
            return

        # 确保目录存在
        os.makedirs(cache_dir, exist_ok=True)
        os.makedirs(local_dir, exist_ok=True)

        self.download_btn.setEnabled(False)
        self.download_thread = DownloadThread(repo_id, cache_dir, local_dir)
        self.download_thread.progress.connect(self.update_status)
        self.download_thread.finished.connect(self.download_finished)
        self.download_thread.start()

    def update_status(self, message):
        self.status_label.setText(message)

    def download_finished(self, success, message):
        self.status_label.setText(message)
        self.download_btn.setEnabled(True)
        if success:
            QMessageBox.information(self, '成功', message)
        else:
            QMessageBox.critical(self, '错误', message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DownloadApp()
    window.show()
    sys.exit(app.exec_())
