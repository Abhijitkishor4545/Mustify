import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QCheckBox, QFrame, QHBoxLayout, QMessageBox, QWidget
from PyQt5.QtGui import QPixmap, QFont, QColor
from PyQt5.QtCore import Qt
import mysql.connector
from languagechoice import LanguageChoice
from signup1 import Mysign

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

class ColorfulScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome")
        self.setGeometry(0, 0, 2000, 1000)
        
        # Set a colorful background
        self.setStyleSheet("background-color: lightblue;")

        # Welcome message
        welcome_label = QLabel("Login Successful!", self)
        welcome_label.setFont(QFont("Arial", 48))
        welcome_label.setGeometry(600, 400, 800, 100)
        welcome_label.setStyleSheet("color: white;")

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Page")
        self.setGeometry(0, 0, 2000, 1000)  
        
        # Background image
        self.logo2_label = QLabel(self)
        self.logo2 = QPixmap("E:\Yash\Python projects\Musify\images\loginimage.jpg")
        self.logo2_label.setPixmap(self.logo2)
        self.logo2_label.setGeometry(0, 0, 2000, 1000)
        
        # Frame for the text
        self.frame = QFrame(self)
        self.frame.setGeometry(570, 100, 700, 800)
        self.frame.setFrameShape(QFrame.Box)  
        self.frame.setLineWidth(2)  
        self.frame.setStyleSheet("border: 4px solid white; background-color: black; border-radius: 20px;")
        
        self.login()
        
    def login(self):
        # Font size for titles
        self.font1 = QFont()
        self.font1.setFamily('Comic Sans MS')
        self.font1.setPointSize(60)
        
        # Login title
        self.title = QLabel("Login", self)
        self.title.setFont(self.font1)
        self.title.setGeometry(800, 165, 300, 135)
        self.title.setStyleSheet("color:white")
        
        # Font for subtitles
        font2 = QFont()
        font2.setFamily("Arial")
        font2.setPointSize(23)
        
        # Email label
        self.email = QLabel("Email", self)
        self.email.setFont(font2)
        self.email.setGeometry(775, 350, 120, 125)
        self.email.setStyleSheet("color:white")
        
        # Password label
        self.password = QLabel("Password", self)
        self.password.setFont(font2)
        self.password.setGeometry(775, 480, 300, 110)
        self.password.setStyleSheet("color:white")
        
        # Password input
        self.password_input = PasswordLineEdit(self)
        self.password_input.setGeometry(775, 580, 300, 50)
        self.password_input.setStyleSheet("background-color: transparent; font-size: 16pt; color:white;")
       
        # Email input
        self.email_input = QLineEdit(self)
        self.email_input.setGeometry(775, 450, 300, 50)
        self.email_input.setStyleSheet("background-color: transparent; font-size: 16pt; color:white;")
        
        # Remember me checkbox
        self.checkbox = QCheckBox('Remember Me', self)
        self.checkbox.setGeometry(775, 660, 300, 40)
        self.checkbox.setStyleSheet("color:white; font-size:16px;")
        
        # Sign up label
        self.acc = QLabel("Don't have an account?", self)
        self.acc.setFont(font2)
        self.acc.setGeometry(650, 700, 500, 110)
        self.acc.setStyleSheet("color:white")
        
        # Sign up button
        self.signup = QPushButton("Signup", self)
        self.signup.setGeometry(1055, 720, 120, 70)
        self.signup.setStyleSheet("background-color: transparent; border-radius: 35px; color: blue;")
        self.signup.setFont(font2)
        self.signup.clicked.connect(self.opensignpage)
        
        # Login button
        self.login1 = QPushButton("LOGIN", self)
        self.login1.setGeometry(800, 795, 250, 70)
        self.login1.setStyleSheet("background-color: blue; border-radius: 20px")
        self.login1.setFont(font2)
        self.login1.clicked.connect(self.authenticate_user)
        
        # Back button
        self.backlogin_btn = QPushButton("Back", self)
        self.backlogin_btn.setGeometry(20, 20, 50, 50)
        self.backlogin_btn.setStyleSheet("background-color:white; border-radius:25px")
        self.backlogin_btn.clicked.connect(self.return_home)
        
    def authenticate_user(self):
        user_email = self.email_input.text()
        user_password = self.password_input.text()
        
        if self.validate_login(user_email, user_password):
            self.show_message("Success", "Login successful!")
            self.colorful_screen = ColorfulScreen()
            self.colorful_screen.show()  # Show the colorful screen
            self.close()  # Close the login window
        else:
            self.show_message("Error", "Invalid email or password.")
    
    def validate_login(self, email, password):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin123",
                database="login"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM user WHERE EMAIL = %s AND PASSWORD_EMAIL = %s", (email, password))
            result = mycursor.fetchone()
            mycursor.close()
            mydb.close()
            return result is not None
        except mysql.connector.Error as err:
            self.show_message("Database Error", str(err))
            return False

    def return_home(self):
        self.close()
    
    def opensignpage(self):
        self.signopen = Mysign()
        self.signopen.show()
    
    def show_message(self, title, message):
        QMessageBox.information(self, title, message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    obj = MyWindow()
    obj.show()
    sys.exit(app.exec_())
