from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import (QApplication, QMainWindow)

from GUI_test import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.Command = ""

    #def slot_Command know it signal sender
    def slot_Command(self):
        ButtonPressed = self.sender()
        if ButtonPressed == self.pushButton_Tien:
            self.Command = "Tiến"
        elif ButtonPressed == self.pushButton_Lui:
            self.Command = "Lùi"
        elif ButtonPressed == self.pushButton_Phai:
            self.Command = "Phải"
        elif ButtonPressed == self.pushButton_Trai:
            self.Command = "Trái"
        elif ButtonPressed == self.pushButton_Dung:
            self.Command = "Dừng"
        elif ButtonPressed == self.pushButton_Nhanh:
            self.Command = "Nhanh"
        elif ButtonPressed == self.pushButton_Cham:
            self.Command = "Chậm"

        self.textEdit.setText(self.Command)

    def slot_PredictMic(self):
        self.textEdit.setText("Ghi âm")

    def slot_Publish(self):
        self.textEdit.setText("Gửi")

    def keyPressEvent(self, a0: QKeyEvent):
        KeyPressed = a0.text()
        if KeyPressed == '8':
            self.Command = "Tiến"
        elif KeyPressed == '2':
            self.Command = "Lùi"
        elif KeyPressed == '6':
            self.Command = "Phải"
        elif KeyPressed == '4':
            self.Command = "Trái"
        elif KeyPressed == '5':
            self.Command = "Dừng"
        elif KeyPressed == '9':
            self.Command = "Nhanh"
        elif KeyPressed == '3':
            self.Command = "Chậm"

        self.textEdit.setText(self.Command)
        
if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()