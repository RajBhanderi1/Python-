import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget, QLabel
import time,datetime
from PyQt5.QtCore import QTimer,Qt,QTime
from PyQt5.QtGui import QFont ,QFontDatabase

class DigitalClock(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Time Clock")
        self.setGeometry(900, 150, 260, 70)
        self.setStyleSheet("background-color: black;")
    
        self.time = QLabel("",self)
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.update_time)

        self.initUI()


    def initUI(self):

        self.time.setStyleSheet("color : Green;"
                                "font-size :50px;")
        self.time.setGeometry(0, 0, self.width(), self.height())

        self.time.setAlignment(Qt.AlignCenter)

        font_id = QFontDatabase.addApplicationFont("C:\\Users\\Raj Bhanderi\\Python-\\DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family, 50)
        self.time.setFont(font)

    def update_time(self):
        # current_time = datetime.datetime.now()
        # self.time.setText(current_time.strftime("%H:%M:%S"))
        
        current_time =QTime.currentTime().toString("hh:mm:ss AP")
        self.time.setText(current_time)
        


def main():
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()

    sys.exit(app.exec_())





if __name__ == "__main__":
    main()



