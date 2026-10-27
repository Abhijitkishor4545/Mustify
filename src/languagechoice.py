
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel 
from PyQt5.QtGui import QFont,QPixmap 
from Songpage1 import Songs
from Songpage2 import Mongs
from Songpage3 import Rongs
import sys
class LanguageChoice(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,2000,1500)
        self.setStyleSheet('background-color:#191414')
        #background image
        self.langimg_label=QLabel(self)
        self.langimg=QPixmap("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/pexels-thibault-trillet-167491.jpg")
        self.langimg_label.setPixmap(self.langimg)
        self.langimg_label.setGeometry(0,0,1910,1000)
        '''
        self.logo2_label=QLabel(self)
        self.logo2=QPixmap("C:/Users/ANUJ/Desktop/core2web/musify/images/lang.jpg")
        self.logo2_label.setPixmap(self.logo2)
        self.logo2_label.setGeometry(0,0,2000,1000)
        self.logo2_label.setStyleSheet("border-radius:")
        '''
        self.languagechoice()
    def languagechoice(self):
        
        #label font
        font2 = QFont()
        font2.setFamily("Comic Sans MS")
        font2.setPointSize(50)
        #label
        
        self.label=QLabel(" Trending Event",self)
        self.label.setFont(font2)
        self.label.setGeometry(640,100,1500,125)
        self.label.setStyleSheet("background-color:transparent;color:white")
        
        #lang buttons
        self.language_btn_font=QFont()
        self.language_btn_font.setPointSize(20)
        self.English_btn=QPushButton("Art",self)
        self.Marathi_btn=QPushButton("Music",self)
        self.Hindi_btn=QPushButton("Sport",self)
        self.Punjabi_btn=QPushButton("Corporate",self)
        self.Bhojpuri_btn=QPushButton("Traval",self)

        #LanguageButtons Geometry

        self.English_btn.setGeometry(200,300,200,200)
        self.Marathi_btn.setGeometry(800,300,200,200)
        self.Hindi_btn.setGeometry(1400,300,200,200)
        self.Punjabi_btn.setGeometry(500,650,200,200)
        self.Bhojpuri_btn.setGeometry(1100,650,200,200)
        
        self.English_btn.setStyleSheet('background-color:white;border-radius:100px;')
        self.Marathi_btn.setStyleSheet('background-color:white;border-radius:100px')
        self.Hindi_btn.setStyleSheet('background-color:white;border-radius:100px')
        self.Punjabi_btn.setStyleSheet('background-color:white;border-radius:100px')
        self.Bhojpuri_btn.setStyleSheet('background-color:white;border-radius:100px')

        self.English_btn.setFont(self.language_btn_font)
        self.Marathi_btn.setFont(self.language_btn_font)
        self.Hindi_btn.setFont(self.language_btn_font)
        self.Punjabi_btn.setFont(self.language_btn_font)
        self.Bhojpuri_btn.setFont(self.language_btn_font)

        self.English_btn.clicked.connect(self.to_music_page)
        self.Marathi_btn.clicked.connect(self.to_display_page)
        self.Hindi_btn.clicked.connect(self.to_originated_page)
        
        
        
        # back button
        self.backlanguage_btn=QPushButton("Back",self)
        self.backlanguage_btn.setGeometry(20,20,50,50)
        self.backlanguage_btn.setStyleSheet("background-color:white;border-radius:25px")

        self.backlanguage_btn.clicked.connect(self.return_loginpage)
        #logo musify
        '''
        self.logo_label=QLabel(self)
        self.logo=QPixmap("C:/Users/ANUJ/Desktop/core2web/musify/images/logo2.jpg")
        self.logo_label.setPixmap(self.logo)
        self.logo_label.setGeometry(0,0,200,200)
        self.logo_label.setStyleSheet("border-radius:")
        '''
    def to_music_page(self):
        self.obj1=Songs()
        self.obj1.show()
    def to_display_page(self):
        self.obj2=Mongs()
        self.obj2.show()
    def to_originated_page(self):
        self.obj3=Rongs()
        self.obj3.show()
        
    
    def return_loginpage(self):
        self.close()

    
if __name__=="__main__":
    app=QApplication(sys.argv)
    language=LanguageChoice()
    language.show()
    sys.exit(app.exec_())