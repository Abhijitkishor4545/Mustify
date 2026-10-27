import sys
from tkinter import messagebox
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QCheckBox, QFrame, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from languagechoice import LanguageChoice


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

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Page")
        self.setGeometry(0, 0, 2000, 1000)  
        
        #background image
        self.logo2_label=QLabel(self)
        self.logo2=QPixmap("C:/Users/abhij/OneDrive/Desktop/Eventmanagement/asstes/Images/b3.png")
        self.logo2_label.setPixmap(self.logo2)
        self.logo2_label.setGeometry(0,0,2000,1000)
        self.logo2_label.setStyleSheet("border-radius:")
        
        #frame to text
        self.frame = QFrame(self)
        self.frame.setGeometry(570, 100, 700, 800)
        self.frame.setFrameShape(QFrame.Box)  # Set the frame shape to be a box
        self.frame.setLineWidth(2)  # Set the width of the frame's border
        self.frame.setStyleSheet("border: 4px solid white; background-color: black;border-radius: 20px;")
        self.fetchdata =[]
        self.login()
        
    def login (self):
        #setting font size for titles
        self.font1=QFont()
        self.font1.setFamily('Comic Sans MS')
        self.font1.setPointSize(60)
        
        #login title
        self.title=QLabel("Login",self)
        self.title.setFont(self.font1)
        self.title.setGeometry(800,165,300,135)
        self.title.setStyleSheet("color:white")
        
        #font for subtitles
        font2 = QFont()
        font2.setFamily("Arial")
        font2.setPointSize(23)
        
        #Email label
        self.email=QLabel("Email",self)
        self.email.setFont(font2)
        self.email.setGeometry(775,350,120,125)
        self.email.setStyleSheet("color:white")
        
        #password label
        self.password=QLabel("Password",self)
        self.password.setFont(font2)
        self.password.setGeometry(775,480,300,110)
        self.password.setStyleSheet("color:white")
        
        #taking password
        self.password_input=PasswordLineEdit(self)  # Use custom PasswordLineEdit widget
        self.password_input.setGeometry(775,580,300,50)
        self.password_input.setStyleSheet("background-color: transparent;font-size: 16pt;color:white;")
       
        #taking email
        self.email_input=QLineEdit(self)
        self.email_input.setGeometry(775,450,300,50)
        self.email_input.setStyleSheet("background-color: transparent;font-size: 16pt;color:white")
        
        #remember me
        self.checkbox = QCheckBox('Remember Me',self)
        self.checkbox.setGeometry(775,660,300,40 )
        self.checkbox.setStyleSheet("color:white;font-size:16px;")
        
        #singn up label
        self.acc=QLabel("Don't have an account",self)
        self.acc.setFont(font2)
        self.acc.setGeometry(650,700,500,110)
        self.acc.setStyleSheet("color:white")
        
        #signup font
        font3 = QFont()
        
        font3.setPointSize(18)
        
        #signup pushbutton
        self.signup=QPushButton("Signup",self)
        self.signup.setGeometry(1055,720,120,70)
        self.signup.setStyleSheet("background-color:transperant;border-radius:35px;color:blue")
        self.signup.setFont(font3)
        self.signup.clicked.connect(self.opensignpage)
        
        #login pushbutton
        self.login1=QPushButton("LOGIN",self)
        self.login1.setGeometry(800,795,250,70)
        self.login1.setStyleSheet("background-color:blue;border-radius:20px")
        self.login1.setFont(font3)
        self.login1.clicked.connect(self.ret)
        self.login1.clicked.connect(self.fetch)
        self.login1.clicked.connect(self.Login)
        

        
        

        
        
         #Back Button
        self.backlogin_btn=QPushButton("Back",self)
        self.backlogin_btn.setGeometry(20,20,50,50)
        self.backlogin_btn.setStyleSheet("background-color:white;border-radius:25px")
        
        self.backlogin_btn.clicked.connect(self.return_home)
        
    def ret(self):
        self.user_email=self.email_input.text()
        self.user_password=self.password_input.text()
        self.obj=LanguageChoice()
        self.obj.show()
        #self.method1(self.user_email,self.user_password)
        
    def return_home(self):
        self.close()
    
    def language_option(self):
       # self.langobj=LanguageChoice()
       # self.langobj.show()
        pass
        
   # def opensignpage(self):
    #    self.signopen=Mysign()
     #   self.signopen.show()
    
    def opensignpage(self):
        # Move it here to break circular import
        from signup1 import Mysign

        self.signopen = Mysign()
        self.signopen.show()

    def show_custom_error(self, title, text):
        self.setWindowTitle(title)
        self.setText(text)
        # Customize the appearance using a stylesheet
        self.setStyleSheet("""
            QMessageBox {
                background-color: yellow;
                border-radius: 10px;
                padding: 15px;
            }
            QMessageBox QLabel {
                font-size: 16px;
                font-family: 'Arial', sans-serif;
                color: black;
            }
            QMessageBox QPushButton {
                background-color: #5cb85c;
                color: white;
                border-radius: 8px;
                padding: 10px;
                font-size: 14px;
            }
            QMessageBox QPushButton:hover {
                background-color: #4cae4c;
            }
            QMessageBox QPushButton:pressed {
                background-color: #397f39;
            }
        """)
        
        # Show the message box
        self.exec_()




    def fetch(self):
        abhibd = mysql.connector.connect(host="localhost",user="root",password="admin123",database="xyz")
        abhicursor=abhibd.cursor()
        abhicursor.execute("select * from om")
        abhiresult = abhicursor.fetchall()
        self.fetchdata = abhiresult
        
        for i in abhiresult:
            print(i)
            
    def Login(self):
        
        self.email_input,
        self.password_input,
        email = self.email_input.text()
        password = self.password_input.text()
        print("Email:", email)
        print("Password:", password)
        for i in self.fetchdata:
            print(i) 

            if i[0] == email and i[2] == password:
                messagebox.showerror("Success", "Login Successful!")
                
                
            else:
                
                messagebox.showerror("record ")
                
        
            
                abhibd = mysql.connector.connect(host="localhost",user="root",password="admin123",database="login")
                abhicursor = abhibd.cursor()
            #create database# 
            #abhicursor.execute("create table radha(email varchar(120), password varchar(100))")
           # for i in abhicursor:
              #  print(i)            
                sql = "insert into radha(email,password) values (%s,%s)"
                val = (email,password)
                abhicursor.execute(sql,val)
                abhibd.commit()
            
            
    
    
    
        
          
             
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    obj=MyWindow()
    obj.show()
    sys.exit(app.exec_())
    
