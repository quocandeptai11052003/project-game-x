import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox
#from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Game') 
        self.setGeometry(300, 300, 300, 200)

        btnStart = QPushButton('Bắt đầu game', self)
        btnStart.move(100, 70)
        btnStart.clicked.connect(self.startGame)

        btnQuit = QPushButton('Thoát game', self)
        btnQuit.move(100, 120)
        btnQuit.clicked.connect(self.quitGame)

        self.show()

    def startGame(self):
        QMessageBox.information(self, 'Thông báo', 'Chương trình đã bắt đầu')

    def quitGame(self):
        reply = QMessageBox.question(self, 'Thông báo', 'Bạn có muốn thoát game không?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv) 
    ex = MyApp()
    sys.exit(app.exec_())
