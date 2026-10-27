from binascii import Error
import sys
from tkinter import StringVar, messagebox
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QFrame,QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap, QColor, QPainter, QBrush
from PyQt5.QtCore import Qt
import mysql
import mysql.connector
import login1


import login1


class PasswordLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setEchoMode(QLineEdit.Password)

        self.show_hide_button = QPushButton(self)
        self.show_hide_button.setText("🙈")
        self.show_hide_button.setCursor(Qt.ArrowCursor)
        self.show_hide_button.setStyleSheet("border:none; background-color:transparent;")
        self.show_hide_button.setFlat(True)
        self.show_hide_button.clicked.connect(self.toggle_password_visibility)

        layout = QHBoxLayout(self)
        layout.addWidget(self.show_hide_button)
        layout.setAlignment(Qt.AlignRight)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def toggle_password_visibility(self):
        if self.echoMode() == QLineEdit.Password:
            self.setEchoMode(QLineEdit.Normal)
            self.show_hide_button.setText("🙉")
        else:
            self.setEchoMode(QLineEdit.Password)
            self.show_hide_button.setText("🙈")

class Mysign(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('My PyQt5 Window')   
        self.setGeometry(0, 0, 2000, 1000)     # Set the position (x, y) and size (width, height) of the window
        self.setStyleSheet("background-color: black;")
        
        # Background image
        self.logo2_label = QLabel(self)
        self.logo2 = QPixmap("E:\Yash\Python projects\Musify\images\sign2.jpg")
        self.logo2_label.setPixmap(self.logo2)
        self.logo2_label.setGeometry(0, 0, 2000, 1000)
        self.logo2_label.setStyleSheet("border-radius:")
        
        # Frame for text
        self.frame = QFrame(self)
        self.frame.setGeometry(590, 100, 700, 800)
        self.frame.setStyleSheet("border-radius: 40px; background-color: rgba(255, 255, 255, 50); border: 8px solid red;")
        
        # Overlay frame for blur effect
        self.overlay_frame = QFrame(self)
        self.overlay_frame.setGeometry(590, 100, 700, 800)
        self.overlay_frame.setStyleSheet("background-color: rgba(0, 0, 0, 150); border-radius: 20px;")
        
        self.func()
        
    
    def func(self):
        # Font for titles
    
        fon = QFont()
        fon.setFamily('Comic Sans MS')
        fon.setPointSize(13)
        # Font for titles
        font1 = QFont()
        font1.setFamily('Comic Sans MS')
        font1.setPointSize(60)
        
        # Font for subtitles
        font2 = QFont()
        font2.setFamily("Arial")
        font2.setPointSize(23)
        
        # Signup title
        self.title = QLabel("Signup", self)
        self.title.setFont(font1)
        self.title.setGeometry(790, 100, 310, 135)
        self.title.setStyleSheet("background-color: transparent;color: white")
        
        
        
        
         # user
        self.user = QLabel("User Name", self)
        self.user.setFont(font2)
        self.user.setGeometry(775, 225, 210, 125)
        self.user.setStyleSheet("background-color: transparent;color: white")
        
        # user input
        self.user_input = QLineEdit(self)
        self.user_input.setGeometry(775, 320, 300, 50)
        self.user_input.setStyleSheet("background-color: transparent; font-size: 16pt; color: white;")
        
        # Email label
        self.email = QLabel("Email", self)
        self.email.setFont(font2)
        self.email.setGeometry(775, 340, 120, 125)
        self.email.setStyleSheet("background-color: transparent;color: white")
        
        # Password label
        self.password = QLabel("Password", self)
        self.password.setFont(font2)
        self.password.setGeometry(775, 460, 300, 110)
        self.password.setStyleSheet("background-color: transparent;color: white")
        
        # Result label
        self.resultLabel = QLabel("", self)
        self.resultLabel.setFont(fon)
        self.resultLabel.setGeometry(775, 690, 330, 110)
        self.resultLabel.setStyleSheet("background-color: transparent;color: red")
        
        # Confirm password label
        self.cpassword = QLabel("Confirm Password", self)
        self.cpassword.setFont(font2)
        self.cpassword.setGeometry(775, 580, 330, 110)
        self.cpassword.setStyleSheet("background-color: transparent;color: white")
        
        # Taking password
        self.password_input = PasswordLineEdit(self)
        self.password_input.setGeometry(775, 550, 300, 50)
        self.password_input.setStyleSheet("background-color: transparent; font-size: 16pt; color: white;")
        
        # Taking email
        self.email_input = QLineEdit(self)
        self.email_input.setGeometry(775, 430, 300, 50)
        self.email_input.setStyleSheet("background-color: transparent; font-size: 16pt; color: white;")
        
        # Confirm pass
        self.cpassword_input = PasswordLineEdit(self)
        self.cpassword_input.setGeometry(775, 680, 300, 50)
        self.cpassword_input.setStyleSheet("background-color: transparent; font-size: 16pt; color: white;")
        
        # Done button############
        self.login1 = QPushButton("DONE", self)
        self.login1.setGeometry(800, 785, 250, 70)
        self.login1.setStyleSheet("background-color: blue; border-radius: 20px")
        self.login1.setFont(font2)
        self.login1.clicked.connect(self.check)
        self.login1.clicked.connect(self.return_home)
        self.login1.clicked.connect(self.SingIn)
        

        
        #Back Button
        self.backlogin_btn=QPushButton("Back",self)
        self.backlogin_btn.setGeometry(20,20,50,50)
        self.backlogin_btn.setStyleSheet("background-color:white;border-radius:25px")
        self.backlogin_btn.clicked.connect(self.return_home)
        
        
            
    
        
    def SingIn(self):
        self.user_input,
        self.email_input,
        self.password_input,
        self.cpassword_input
        name = self.user_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        cpassword = self.cpassword_input.text()
        print("Name:", name)
        print("Email:", email)
        print("Password:", password)
        print("Confirm Password:", cpassword)
        if self.user_input == "" or self.email_input == "":
            messagebox.showerror("all fields are required")
        else:
            abhibd = mysql.connector.connect(host="localhost",user="root",password="admin123",database="xyz")
            abhicursor = abhibd.cursor()
            #create database#
           # abhicursor.execute("create table om(name varchar(100),email varchar(120), password varchar(100), cpassword varchar(100))")
            #for i in abhicursor:
             #   print(i)
            sql = "insert into om(name,email,password,cpassword) values (%s,%s,%s,%s)"
            val = (name,email,password,cpassword)
            abhicursor.execute(sql,val)
            abhibd.commit()
          
        
            
          

     
   

        
        


        
    def return_home(self):
        self.close()
        
        
    def check(self):
        pass1 = self.password_input.text()
        pass2 = self.cpassword_input.text() 
        
        if pass1 == pass2:
            pass
        else:
            self.resultLabel.setText('*Enter The Same Password.')
            
    def openLoginpage(self):
        from login1 import login1
        self.login1()
        self.Loginopen.show()
        
            
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mysign()
    window.show()
    sys.exit(app.exec_())