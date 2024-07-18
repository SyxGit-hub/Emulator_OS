import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QProcess

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GBA Emulator")
        self.setGeometry(100,100,800,600)
        layout = QVBoxLayout()
        self.start_button = QPushButton("Start mGBA")
        self.start_button.clicked.connect(self.start_mgba)
        layout.addWidget(self.start_button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.process = QProcess(self)

    def start_mgba(self):
        rom_path = "D:\\roms\\Advance_wars.gba"
        mgba_path = self.find_mgba_executable()
        if mgba_path:
            self.process.start(mgba_path, [rom_path])
        else:
            print("mGbA executable not found!!!")
    
    def find_mgba_executable(self):
        if sys.platform.startswith('win'):
            return r"C:\\Program Files\\mGBA\\mGBA.exe"

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()