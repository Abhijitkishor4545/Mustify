import sys
import os

os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
from PyQt5.QtWidgets import QWidget,QLabel,QApplication,QPushButton,QProgressBar,QFileDialog
from PyQt5.QtMultimedia import QMediaContent,QMediaPlayer
from PyQt5.QtCore import QUrl,QTimer 
from PyQt5.QtGui import QFont,QIcon,QPixmap
from PyQt5.QtCore import QUrl, QTimer, Qt

class MP3_player(QWidget):
    def __init__(self,songaddress,songimageaddress):
        super().__init__()
        self.songaddress=songaddress
        self.songimageaddress=songimageaddress

        

        print(self.songaddress)
        self.count=0
        self.ui()
    def ui(self):
        self.setWindowTitle('Musify')
        self.setGeometry(0,0,2000,1500)
        icon=QIcon('E:\Yash\Python projects\Musify\images\Musifylogo.jpeg')
        self.setStyleSheet('background-color:#191414')
        self.setWindowIcon(icon)
        self.songimglabel=QLabel(self)
        self.songimg=QPixmap("E:\Yash\Python projects\Musify\images\Musifylogo (1).jpeg")
    
        self.songimglabel.setPixmap(self.songimg)
        
        self.songimglabel.setFixedSize(1000,1000)
        self.songimglabel.setGeometry(50,50,1000,1000)
     


        
        
        self.playingsongimglabel=QLabel(self)
    
        #self.playingsongimg=QPixmap(f"{self.songimageaddress}")
        
        #self.playingsongimglabel.setPixmap(self.playingsongimg)
        #self.playingsongimglabel.setGeometry(870,190,500,500)
        
        self.playingsongimg = QPixmap(f"{self.songimageaddress}")
        self.playingsongimglabel.setPixmap(self.playingsongimg)
        self.playingsongimglabel.setGeometry(750,190,500,500)
        
        pixmap = QPixmap(self.songimageaddress).scaled(
            1000,600,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        
    
        #self.playingsongimglabel.setGeometry(800,800,1000,500)


        font=QFont()
        font.setPointSize(11)
        font1=QFont()
        font1.setPointSize(16)

        #self.load_btn=QPushButton('select',self)
        self.play_btn=QPushButton('',self)
        self.back_btn=QPushButton('',self)
        self.next_btn=QPushButton('',self)

        self.backbuttonimg=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/nextprevois.png")

        self.back_btn.setGeometry(750,820,120,120)
        self.play_btn.setGeometry(930,820,120,120)
        self.next_btn.setGeometry(1110,820,120,120)
        self.playbtnimage=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/playbutton.png")
        self.nextbtnimage=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/nextbutton2.jpg")

        self.play_btn.setStyleSheet('background-color:white;border-radius:60px;color:white')
        self.back_btn.setStyleSheet('background-color:white;border-radius:60px;color:white')
        self.next_btn.setStyleSheet('background-color:white;border-radius:60px;color:white')
        self.play_btn.setIcon(self.playbtnimage)
        self.back_btn.setIcon(self.backbuttonimg)
        self.next_btn.setIcon(self.nextbtnimage)
        self.next_btn.setIconSize(self.nextbtnimage.actualSize(self.next_btn.size()))
        self.back_btn.setIconSize(self.backbuttonimg.actualSize(self.back_btn.size()))
        self.play_btn.setIconSize(self.playbtnimage.actualSize(self.play_btn.size()))
        self.current_index = 0
        
        
        
        
        #self.back_btn.setStyleSheet('border-radius:60px;')
        #self.play_btn.setFont(font)
        #self.pause_btn.setFont(font)
        #self.stop_btn.setFont(font)
        
        
        self.backbtn=QPushButton("back",self)
        self.backbtn.setGeometry(0,0,50,50)
        self.backbtn.setStyleSheet("background-color:black;color:white;border-radius:25px")
        self.backbtn.clicked.connect(self.prevpage)
        self.progressbar()
        self.connection()
    def prevpage(self):
        self.close()
    def connection(self):
        #self.load_btn.clicked.connect(self.load_mp3)
        self.play_btn.clicked.connect(self.play)
        #self.next_btn.clicked.connect(self.pause_mp3)
        self.back_btn.clicked.connect(self.stop_mp3)
        self.mediaplayer=QMediaPlayer()

    def play(self):
        if self.count%2==0:
            self.playimg=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/pause.png")
            self.play_btn.setIcon(self.playimg)
        else:
             self.playimgtlg=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/playbutton.png")
             self.play_btn.setIcon(self.playimgtlg)
        self.song=self.songaddress
        if self.count==0:
            self.play_mp3(self.song)
            self.start_process()
        else:
            self.pause()
        self.count+=1
     
    
        
    def play_mp3(self,songaddress):
        self.media_content=QMediaContent(QUrl.fromLocalFile(f'{songaddress}'))
        self.mediaplayer.setMedia(self.media_content)
        self.mediaplayer.play()
        print(self.count)
    def pause(self):
        if self.mediaplayer.state()==QMediaPlayer.PlayingState:
            self.mediaplayer.pause()
            print("In pause")
        elif self.mediaplayer.state()==QMediaPlayer.PausedState:
            self.mediaplayer.play()
            print("In play")
    def stop_mp3(self):
        self.mediaplayer.stop()

    
    def progressbar(self):
        self.progressbar=QProgressBar(self)
        self.progressbar.setGeometry(500,780,1000,10)
        self.progressbar.setStyleSheet("QProgressBar { border: 2px solid grey; border-radius: 5px; background-color: black; }""QProgressBar::chunk { background-color: white; }")
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.update_process)
        self.progress_value=0
        self.progressbar.setValue(self.progress_value)
    def start_process(self):
        self.timer.start(1500)
    def reset_process(self):
        self.progress_value=0
        self.progressbar.setValue(self.progress_value)
    def update_process(self):
        self.progress_value+=1
        self.progressbar.setValue(self.progress_value)
        if self.progress_value==1500:
            self.timer.stop()
    def fun(self):
        if self.mediaplayer.state()==QMediaPlayer.PlayingState:
            self.mediaplayer.stop()

   

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MP3_player(songaddress="C:/Users/abhij/OneDrive/Desktop/Eventmanagement/src/Beedi(mp3fix.in).mp3",songimageaddress="C:/Users/abhij/OneDrive/Desktop/Eventmanagement/asstes/Images/wedding.jpg")
    window.show()
    sys.exit(app.exec_())

#self.rsong_database={self.btn1:"C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/song/Mala-Ved-Lagale-Premache.mp3",self.btn9:"C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/song/Mazi-Bayko-Mazi-Bayko.mp3",self.btn3:"C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/song/Sairat-Instrumental.mp3",self.btn6:"C:Users/abhij/OneDrive/Desktop/Spotify clone/asstes/song/Majhi Navri.mp3",self.btn8:"C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/song/Mausam-Hai-Mastana-Girlfriend-Nastana.mp3",self.btn4:"C:Users/abhij/OneDrive/Desktop/Spotify clone/asstes/song/Mitwaa-Shankar-Mahadevan.mp3",self.btn2:"C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/song/Saaj-Hyo-Tuza.mp3",self.btn7:"",self.btn5:"C:Users/abhij/OneDrive/Desktop/Spotify clone/asstes/song/Maza-Pillu.mp3"}
