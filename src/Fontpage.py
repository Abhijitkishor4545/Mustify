'''import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLabel 
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont,QPixmap 
from login1  import MyWindow
class Front_page(QWidget):
    def __init__(self):
        super().__init__()
        self.SetUi()
    def SetUi(self):
        self.setGeometry(0,0,2000,1500)
        self.setWindowTitle("Musify")
        self.setStyleSheet('background-color:	#191414')
        self.font_slogan=QFont()
        self.font_slogan.setPointSize(70)
        # Background Image
        self.backgroundimg_label=QLabel(self)
        self.backgroundimg=QPixmap("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/neon_green_music_headphone_brick_wall_hd_green (1).jpg")
        self.backgroundimg_label.setPixmap(self.backgroundimg)
        self.backgroundimg_label.setGeometry(0,0,1910,1000)
        self.backgroundimg_label.setStyleSheet("border-radius:")
        #Slogan
        self.label_slogan=QLabel("Feel The World",self)
        self.label_slogan.setStyleSheet('background-color:transparent;color:black')
        self.label_slogan.setFont(self.font_slogan)
        self.label_slogan.move(150,230)
        # slogan1
        self.label_slogan1=QLabel("With Musify",self)
        self.label_slogan1.setFont(self.font_slogan)
        self.label_slogan1.setStyleSheet('background-color:transparent;color:black')
        self.label_slogan1.move(150,420)


        #Login Button
        self.btn_font=QFont()
        self.btn_font.setPointSize(16)
        self.login_btn=QPushButton("Login",self)
        self.login_btn.setGeometry(1485,30,200,60)
        self.login_btn.setStyleSheet('background-color:white;border-radius:30px ')
        self.login_btn.setFont(self.btn_font)
        self.loginobj=MyWindow()
        self.login_btn.clicked.connect(self.openloginpage)
        
        self.login_btn.setCursor(Qt.PointingHandCursor)

 
        #Aboutus Button
        self.aboutus_btn=QPushButton("About",self)
        self.aboutus_btn.setGeometry(1700,30,200,60)
        self.aboutus_btn.setStyleSheet('background-color:white;border-radius:30px ')
        self.aboutus_btn.setFont(self.btn_font)
        self.aboutus_btn.setCursor(Qt.PointingHandCursor)

        #Home Button
        self.home_btn=QPushButton("Home",self)
        self.home_btn.setGeometry(1270,30,200,60)
        self.home_btn.setStyleSheet('background-color:white;border-radius:30px ')
        self.home_btn.setFont(self.btn_font)
        self.home_btn.setCursor(Qt.PointingHandCursor)

      

       
    def openloginpage(self):
        self.logopen=MyWindow()
        self.logopen.show()




if __name__=="__main__":
    app=QApplication(sys.argv)
    window1=Front_page()
    window1.show()
    sys.exit(app.exec_())'''
    
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from login1 import MyWindow
from song import Songs



class Front_page(QWidget):
    def __init__(self):
        super().__init__()
        self.setUi()

    def setUi(self):
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle("Musify")
        self.setStyleSheet("background-color:#191414;")

        # Background Image
        self.backgroundimg_label = QLabel(self)
        self.backgroundimg = QPixmap("asstes\Images\Front.png")
        self.backgroundimg_label.setPixmap(self.backgroundimg)
        self.backgroundimg_label.setGeometry(0, 0, 1920, 1080)
        self.backgroundimg_label.setScaledContents(True)

        # Font for slogans
        slogan_font = QFont("Arial", 70, QFont.Bold)

        # Slogan 1
       # self.label_slogan = QLabel("Feel The World", self)
       # self.label_slogan.setFont(slogan_font)
       # self.label_slogan.setStyleSheet("color:black; background:transparent;")
        #self.label_slogan.move(150, 250)

        # Slogan 2
      #  self.label_slogan1 = QLabel("With Musify", self)
      #  self.label_slogan1.setFont(slogan_font)
      #  self.label_slogan1.setStyleSheet("color:black; background:transparent;")
      #  self.label_slogan1.move(150, 420)

        # Button Font
        btn_font = QFont("Arial", 16)

        # Home Button
        self.home_btn = QPushButton("Home", self)
        self.home_btn.setGeometry(1270, 30, 200, 60)
        self.home_btn.setFont(btn_font)
        self.home_btn.setCursor(Qt.PointingHandCursor)
        self.home_btn.setStyleSheet(
            "background:black; color:white;  border-radius:30px;"

        )

        # Login Button
        self.login_btn = QPushButton("Login", self)
        self.login_btn.setGeometry(1485, 30, 200, 60)
        self.login_btn.setFont(btn_font)
        self.login_btn.setCursor(Qt.PointingHandCursor)
        self.login_btn.setStyleSheet(
            
        
            "background:black; color:white;  border-radius:30px;"
        )
        self.login_btn.clicked.connect(self.openloginpage)

        # About Button
        self.aboutus_btn = QPushButton("About", self)
        self.aboutus_btn.setGeometry(1700, 30, 200, 60)
        
        self.aboutus_btn.setFont(btn_font)
        self.aboutus_btn.setCursor(Qt.PointingHandCursor)
        self.aboutus_btn.setStyleSheet(
            "background:black; color:white;  border-radius:30px;"
        
        )
        # CreateEvent Button
        self.createEvent_btn = QPushButton("CreateEvent",self)
        self.createEvent_btn.setGeometry(170, 700, 210, 60)
        
        self.createEvent_btn.setFont(btn_font)
        self.createEvent_btn.setCursor(Qt.PointingHandCursor)
        self.createEvent_btn.setStyleSheet(
            "background:blue; color:white;  border-radius:30px;"
        
        )
        
        # See Events
        self.seeEvent_btn = QPushButton("SeeEvent",self)
        self.seeEvent_btn.setGeometry(460, 700, 210, 60)
        
        self.seeEvent_btn.setFont(btn_font)
        self.seeEvent_btn.setCursor(Qt.PointingHandCursor)
        self.seeEvent_btn.setStyleSheet(
            "background:blue; color:white;  border-radius:30px;"
        
        )
        self.seeEvent_btn.clicked.connect(self.openseeEvent)




       
    def openloginpage(self):
        self.login_window = MyWindow()
        self.login_window.show()

    def openseeEvent(self):
        self.see_window = Songs()
        self.see_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Front_page()
    window.show()
    sys.exit(app.exec_())
