import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLabel,QFrame
from PyQt5.QtGui import QFont,QIcon,QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainterPath, QRegion
from PyQt5.QtCore import QSize


from mp3player1 import MP3_player
class Songs(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,2000,1500)
        self.setWindowTitle("Musify")
        self.setStyleSheet("background-color:#191414")
        self.songimg_label=QLabel(self)
        self.songimg=QPixmap('E:\Yash\Python projects\Musify\images\songpage (2).jpeg')
        self.songimg_label.setPixmap(self.songimg)
        self.songimg_label.setGeometry(0,0,1910,1000)
        
        self.song_ui()
    def song_ui(self):
        self.fontsong=QFont()
        self.fontsong.setPointSize(18)
        self.Romantic_label=QLabel("Romantic",self)
        self.Romantic_label.move(20,50)
        self.Romantic_label.setFont(self.fontsong)
        self.Romantic_label.setStyleSheet('background-color:transparent;color:white')
        #
       
        
        #
        
        self.btn1=QPushButton("",self)
        self.btn1.setGeometry(20,110,200,200) 
        self.btn2=QPushButton("",self)
        self.btn2.setGeometry(250,110,200,200) 
        self.btn3=QPushButton("",self)    
        self.btn3.setGeometry(480,110,200,200) 
        self.btn4=QPushButton("",self)
        self.btn4.setGeometry(720,110,200,200) 
        self.btn5=QPushButton("",self)
        self.btn5.setGeometry(957,110,200,200) 
        self.btn6=QPushButton("",self)
        self.btn6.setGeometry(1200,110,200,200) 
        self.btn7=QPushButton("",self)
        self.btn7.setGeometry(1437,110,200,200) 
        self.btn8=QPushButton("",self)
        self.btn8.setGeometry(1680,110,200,200) 
       # self.btn9=QPushButton("",self)
       # self.btn9.setGeometry(1700,110,200,200)
      #  self.btn1.setStyleSheet('background-color:transparent')
      
        #self.btn1 = QPushButton(self)
        #self.btn1.setGeometry(100, 100, 200, 200)
        self.btn1.setStyleSheet("""
        QPushButton {
          background-color: black;
          border: 4px solid white;
          border-radius: 0px;
}
""")
       
        
        self.btn2.setStyleSheet("""
        QPushButton {
          background-color: black;
          border: 4px solid white;
          border-radius: 0px;
}
""")
        self.btn3.setStyleSheet("""
        QPushButton {
          background-color: black;
          border: 4px solid white;
          border-radius: 0px;
}
""")    
        self.btn4.setStyleSheet("""
        QPushButton {
          background-color: black;
          border: 4px solid white;
          border-radius: 0px;
}
""") 
        self.btn5.setStyleSheet("""
        QPushButton {
          background-color: black;
          border: 4px solid white;
          border-radius: 0px;
}
""") 
        self.btn6.setStyleSheet("""
        QPushButton {
          background-color: black;
          border: 4px solid white;
          border-radius: 0px;
}
""")
        self.btn7.setStyleSheet("""
        QPushButton {
          background-color: black;
          border: 4px solid white;
          border-radius: 0px;
}
""")
        self.btn8.setStyleSheet("""
        QPushButton {
          background-color: black;
          border: 4px solid white;
          border-radius: 0px;
}
""")
        '''self.btn9.setStyleSheet("""
        QPushButton {
          background-color: black;
          border: 4px solid white;
          border-radius: 0px;
}
""")'''

     
                      

        
       
       
        
       # self.btn2.setStyleSheet('background-color:transparent;border-radius:50px')  
        #self.btn3.setStyleSheet('background-color:transparent;border-radius:50px')    
        #self.btn4.setStyleSheet('background-color:transparent;border-radius:50px')  
        #self.btn5.setStyleSheet('background-color:transparent;border-radius:50px')  
        #self.btn6.setStyleSheet('background-color:transparent;border-radius:50px')  
        #self.btn7.setStyleSheet('background-color:transparent;border-radius:50px')
        #self.btn8.setStyleSheet('background-color:transparent;border-radius:50px')  
        #self.btn9.setStyleSheet('background-color:transparent;border-radius:50px')    
          #Workout songs

        self.Workout_label=QLabel("Workout",self)
        self.Workout_label.move(100,350)
        self.Workout_label.setFont(self.fontsong)
        self.Workout_label.setStyleSheet('background-color:transparent;color:white')
        self.wbtn1=QPushButton("",self)
        self.wbtn1.setGeometry(100,420,150,200) 
        self.wbtn2=QPushButton("",self)
        self.wbtn2.setGeometry(300,420,150,200) 
        self.wbtn3=QPushButton("",self)
        self.wbtn3.setGeometry(500,420,150,200) 
        self.wbtn4=QPushButton("",self)
        self.wbtn4.setGeometry(700,420,150,200) 
        self.wbtn5=QPushButton("",self)
        self.wbtn5.setGeometry(900,420,150,200) 
        self.wbtn6=QPushButton("",self)
        self.wbtn6.setGeometry(1100,420,150,200) 
        self.wbtn7=QPushButton("",self)
        self.wbtn7.setGeometry(1300,420,150,200) 
        self.wbtn8=QPushButton("",self)
        self.wbtn8.setGeometry(1500,420,150,200) 
        self.wbtn9=QPushButton("",self)
        self.wbtn9.setGeometry(1700,420,150,200)
        self.wbtn1.setStyleSheet('background-color:transparent;border-radius:50px')
        self.wbtn2.setStyleSheet('background-color:transparent;border-radius:50px')
        self.wbtn3.setStyleSheet('background-color:transparent;border-radius:50px')
        self.wbtn4.setStyleSheet('background-color:transparent;border-radius:50px')
        self.wbtn5.setStyleSheet('background-color:transparent;border-radius:50px')
        self.wbtn6.setStyleSheet('background-color:transparent;border-radius:50px')
        self.wbtn7.setStyleSheet('background-color:transparent;border-radius:50px')
        self.wbtn8.setStyleSheet('background-color:transparent;border-radius:50px')
        self.wbtn9.setStyleSheet('background-color:transparent;border-radius:50px')   

        # Devotional
        self.Devotional_label=QLabel("Devotional",self)
        self.Devotional_label.move(100,700)
        self.Devotional_label.setFont(self.fontsong)
        self.Devotional_label.setStyleSheet('background-color:transparent;color:white')
        self.dbtn1=QPushButton("",self)
        self.dbtn1.setGeometry(100,750,150,200) 
        self.dbtn1.setStyleSheet('background-color:white;border-radius:50px')
        self.dbtn2=QPushButton("",self)
        self.dbtn2.setGeometry(300,750,150,200) 
        self.dbtn3=QPushButton("",self)
        self.dbtn3.setGeometry(500,750,150,200) 
        self.dbtn4=QPushButton("",self)
        self.dbtn4.setGeometry(700,750,150,200) 
        self.dbtn5=QPushButton("",self)
        self.dbtn5.setGeometry(900,750,150,200) 
        self.dbtn6=QPushButton("",self)
        self.dbtn6.setGeometry(1100,750,150,200) 
        self.dbtn7=QPushButton("",self)
        self.dbtn7.setGeometry(1300,750,150,200) 
        self.dbtn8=QPushButton("",self)
        self.dbtn8.setGeometry(1500,750,150,200) 
        self.dbtn9=QPushButton("",self)
        self.dbtn9.setGeometry(1700,750,150,200)
        self.dbtn1.setStyleSheet('background-color:transparent;border-radius:50px')
        self.dbtn2.setStyleSheet('background-color:transparent;border-radius:50px')
        self.dbtn3.setStyleSheet('background-color:transparent;border-radius:50px') 
        self.dbtn4.setStyleSheet('background-color:transparent;border-radius:50px')
        self.dbtn5.setStyleSheet('background-color:transparent;border-radius:50px')
        self.dbtn6.setStyleSheet('background-color:transparent;border-radius:50px')
        self.dbtn7.setStyleSheet('background-color:transparent;border-radius:50px')
        self.dbtn8.setStyleSheet('background-color:transparent;border-radius:50px')
        self.dbtn9.setStyleSheet('background-color:transparent;border-radius:50px')

        # image fo button 
        #self.btn1icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/images17.png")
        #self.btn1.setIcon(self.btn1icon)
        #self.btn1.setIconSize(self.btn1icon.actualSize(self.btn1.size()))
        

     
        
        
        

       # QIcon
        self.btn1icon = QIcon(
            "C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/images17.png"
        )
        self.btn1.setIcon(self.btn1icon)
        self.btn1.setIconSize(QSize(192, 192))

      #  self.btn1.setIconSize(self.btn1icon.actualSize(self.btn1.size()))

       # Scale properly
    

        
        


        
        
        
        self.btn2icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/download21.png")
        self.btn2.setIcon(self.btn2icon)
        self.btn2.setIconSize(QSize(192, 192))

       # self.btn2.setIconSize(self.btn2icon.actualSize(self.btn2.size()))

         
        self.btn3icon=QIcon("asstes\Images\download10.png")
        self.btn3.setIcon(self.btn3icon)
        self.btn3.setIconSize(QSize(192, 192))

       # self.btn3.setIconSize(self.btn3icon.actualSize(self.btn3.size()))
        
        self.btn4icon=QIcon("asstes\Images\download23.png")
        self.btn4.setIcon(self.btn4icon)
        self.btn4.setIconSize(QSize(192, 192))

        #self.btn4.setIconSize(self.btn4icon.actualSize(self.btn4.size()))
        
        self.btn5icon=QIcon("asstes\Images\download6.png")
        self.btn5.setIcon(self.btn5icon)
        self.btn5.setIconSize(QSize(192, 192))

        #self.btn5.setIconSize(self.btn5icon.actualSize(self.btn5.size()))
        
        self.btn6icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/download14.png")
        self.btn6.setIcon(self.btn6icon)
        self.btn6.setIconSize(QSize(192, 192))

       # self.btn6.setIconSize(self.btn6icon.actualSize(self.btn6.size()))
        
        self.btn7icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/download11.png")
        self.btn7.setIcon(self.btn7icon)
        #self.btn7.setIconSize(self.btn7icon.actualSize(self.btn7.size()))
        self.btn7.setIconSize(QSize(192, 192))

        
        self.btn8icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/download4.png")
        self.btn8.setIcon(self.btn8icon)
        self.btn8.setIconSize(QSize(192, 192))

        #self.btn8.setIconSize(self.btn8icon.actualSize(self.btn8.size()))
        
        '''self.btn9icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/th (4).jpg")
        self.btn9.setIcon(self.btn9icon)
        self.btn9.setIconSize(QSize(192, 192))

        #self.btn9.setIconSize(self.btn9icon.actualSize(self.btn9.size()))'''

    ''' #Workout image

        self.wbtn1icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/maharaj.jpg")
        self.wbtn1.setIcon(self.wbtn1icon)
        self.wbtn1.setIconSize(self.btn9icon.actualSize(self.wbtn1.size()))

        
        self.wbtn2icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/Believer.jpg")
        self.wbtn2.setIcon(self.wbtn2icon)
        self.wbtn2.setIconSize(self.btn2icon.actualSize(self.wbtn2.size()))

        
        self.wbtn3icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/ganpati.jpg")
        self.wbtn3.setIcon(self.wbtn3icon)
        self.wbtn3.setIconSize(self.wbtn3icon.actualSize(self.wbtn3.size()))

        
        self.wbtn4icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/download19.png")
        self.wbtn4.setIcon(self.wbtn4icon)
        self.wbtn4.setIconSize(self.wbtn4icon.actualSize(self.wbtn4.size()))
        

        
        self.wbtn5icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/harhar.png")
        self.wbtn5.setIcon(self.wbtn5icon)
        self.wbtn5.setIconSize(self.wbtn5icon.actualSize(self.wbtn5.size()))

        
        self.wbtn6icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/th (2).jpg")
        self.wbtn6.setIcon(self.wbtn6icon)
        self.wbtn6.setIconSize(self.wbtn6icon.actualSize(self.wbtn6.size()))

        
        self.wbtn7icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/jogwa.jpg")
        self.wbtn7.setIcon(self.wbtn7icon)
        self.wbtn7.setIconSize(self.wbtn7icon.actualSize(self.wbtn7.size()))
        
        self.wbtn8icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/shriram.jpg")
        self.wbtn8.setIcon(self.wbtn8icon)
        self.wbtn8.setIconSize(self.wbtn8icon.actualSize(self.wbtn8.size()))
        
        self.wbtn9icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/size.jpg")
        self.wbtn9.setIcon(self.wbtn9icon)
        self.wbtn9.setIconSize(self.wbtn9icon.actualSize(self.wbtn9.size()))


        # Devotional image

        self.dbtn1icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/untied.png")
        self.dbtn1.setIcon(self.dbtn1icon)
        
        self.dbtn1.setIconSize(self.dbtn1icon.actualSize(self.dbtn1.size()))
        
        self.dbtn2icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/APNABHAI.png")
        self.dbtn2.setIcon(self.dbtn2icon)
        self.dbtn2.setIconSize(self.dbtn2icon.actualSize(self.dbtn2.size()))
        
        self.dbtn3icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/th (5).jpg")
        self.dbtn3.setIcon(self.dbtn3icon)
        self.dbtn3.setIconSize(self.dbtn3icon.actualSize(self.dbtn3.size()))
        
        self.dbtn4icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/th (4).jpg")
        self.dbtn4.setIcon(self.dbtn4icon)
        self.dbtn4.setIconSize(self.dbtn4icon.actualSize(self.dbtn4.size()))
        
        self.dbtn5icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/th (3).jpg")
        self.dbtn5.setIcon(self.dbtn5icon)
        self.dbtn5.setIconSize(self.dbtn5icon.actualSize(self.dbtn5.size()))
        
        self.dbtn6icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/human.jpg")
        self.dbtn6.setIcon(self.dbtn6icon)
        self.dbtn6.setIconSize(self.dbtn6icon.actualSize(self.dbtn6.size()))
        
        self.dbtn7icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/Adipus.jpg")
        self.dbtn7.setIcon(self.dbtn7icon)
        self.dbtn7.setIconSize(self.dbtn7icon.actualSize(self.dbtn7.size()))
        
        self.dbtn8icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/shomi.jpg")
        self.dbtn8.setIcon(self.dbtn8icon)
        self.dbtn8.setIconSize(self.dbtn8icon.actualSize(self.dbtn8.size()))
        
        self.dbtn9icon=QIcon("C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/ram.jpg")
        self.dbtn9.setIcon(self.dbtn9icon)
        self.dbtn9.setIconSize(self.dbtn9icon.actualSize(self.dbtn9.size()))
        
        # back button
        self.backlanguage_btn=QPushButton("Back",self)
        self.backlanguage_btn.setGeometry(20,20,50,50)
        self.backlanguage_btn.setStyleSheet("background-color:white;border-radius:25px")
        
        self.backlanguage_btn.clicked.connect(self.return_languagepage)
        
        #button size
        
        #Romantic songs connect 
        self.btn1.clicked.connect(lambda:self.rmp3playerpage(self.btn1))
        self.btn2.clicked.connect(lambda:self.rmp3playerpage(self.btn2))
        self.btn3.clicked.connect(lambda:self.rmp3playerpage(self.btn3))
        self.btn4.clicked.connect(lambda:self.rmp3playerpage(self.btn4))
        self.btn5.clicked.connect(lambda:self.rmp3playerpage(self.btn5))
        self.btn6.clicked.connect(lambda:self.rmp3playerpage(self.btn6))
        self.btn7.clicked.connect(lambda:self.rmp3playerpage(self.btn7))
        self.btn8.clicked.connect(lambda:self.rmp3playerpage(self.btn8))
        self.btn9.clicked.connect(lambda:self.rmp3playerpage(self.btn9))

        #devotional button connect
        self.dbtn1.clicked.connect(lambda:self.dmp3playerpage(self.dbtn1))
        self.dbtn2.clicked.connect(lambda:self.dmp3playerpage(self.dbtn2))
        self.dbtn3.clicked.connect(lambda:self.dmp3playerpage(self.dbtn3))
        self.dbtn4.clicked.connect(lambda:self.dmp3playerpage(self.dbtn4))
        self.dbtn5.clicked.connect(lambda:self.dmp3playerpage(self.dbtn5))
        self.dbtn6.clicked.connect(lambda:self.dmp3playerpage(self.dbtn6))
        self.dbtn7.clicked.connect(lambda:self.dmp3playerpage(self.dbtn7))
        self.dbtn8.clicked.connect(lambda:self.dmp3playerpage(self.dbtn8))
        self.dbtn9.clicked.connect(lambda:self.dmp3playerpage(self.dbtn9))

        #Workout song
        self.wbtn1.clicked.connect(lambda:self.wmp3playerpage(self.wbtn1))
        self.wbtn2.clicked.connect(lambda:self.wmp3playerpage(self.wbtn2))
        self.wbtn3.clicked.connect(lambda:self.wmp3playerpage(self.wbtn3))
        self.wbtn4.clicked.connect(lambda:self.wmp3playerpage(self.wbtn4))
        self.wbtn5.clicked.connect(lambda:self.wmp3playerpage(self.wbtn5))
        self.wbtn6.clicked.connect(lambda:self.wmp3playerpage(self.wbtn6))
        self.wbtn7.clicked.connect(lambda:self.wmp3playerpage(self.wbtn7))
        self.var="Core2web"
        self.rmp3playerobj=MP3_player(self.var,self.var)
        self.wmp3playerobj=MP3_player(self.var,self.var)
        self.dmp3playerobj=MP3_player(self.var,self.var)
'''
        #ROmantic
        
    def rmp3playerpage(self,btn):
        self.btnid=btn
        print(self.btnid)
        self.rsongaddrstrore,self.rsongimgaddress=self.rsongfilesstore(self.btnid)
        self.rmp3playerobj=MP3_player(self.rsongaddrstrore,self.rsongimgaddress)
        
        self.check()
        self.rmp3playerobj.show()
    def rsongfilesstore(self,btnid):
        self.rsongid=btnid
        print(self.rsongid)
        self.rsong_database={self.btn1:"C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/song/Majhi Navri.mp3",self.btn9:"C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/song/Ekadantaya Vakratundaya_128-(DJMaza).mp3",self.btn3: "C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/song/Sairat-Instrumental.mp3",self.btn6:"E:\Yash\Music\Satranga(PagalWorld.com.cm).mp3",self.btn8:"E:\Yash\Music\Tera Ban Jaunga (Kabir Singh)(audiosong.in).mp3",self.btn4:"C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/song/Mazi-Bayko-Mazi-Bayko.mp3",self.btn2:"E:\Yash\Music\One Love(PagalWorld.com.cm).mp3",self.btn7:"E:\Yash\Music\Long-Time-No-See(PagalWorldl).mp3",self.btn5:"E:\Yash\Music\Choo-Lo-Jo-Mujhe-Tum-Kabhi(PaglaSongs).mp3"}
        self.rsongaddr=self.rsong_database[self.rsongid]
        self.rsongimage={self.btn1:"C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/images17.png",self.btn9:"C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/th (4).jpg",self.btn3:"C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/download10.png",self.btn6:"E:\Yash\Python projects\Musify\images\Satranga.jpg",self.btn8:"E:\Yash\Python projects\Musify\images\TeraBanJaunga.jpg",self.btn4:"C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/images34.png",self.btn2:"C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/download21.png",self.btn7:"E:\Yash\Python projects\Musify\images\longtimenosee.jpg",self.btn5:"E:\Yash\Python projects\Musify\images\Choo-lo.jpg"}
        
        self.rsongimgid=self.rsongimage[self.rsongid]
    
        print(self.rsongimgid)
        return self.rsongaddr,self.rsongimgid
    
    

    def dmp3playerpage(self,btn):
        self.dbtnid=btn
        self.dsongaddress,self.dsondimgaddress=self.dsongfilestore(self.dbtnid)
        self.dmp3playerobj=MP3_player(self.dsongaddress,self.dsondimgaddress)
        self.check()
        self.dmp3playerobj.show()
    def dsongfilestore(self,btnid):
        self.dsongid=btnid
        self.dsong_database={self.dbtn1:"E:\Yash\Music\Devotional\sri-venkatesa-suprabhatham-[hindugodsongs.in].mp3",self.dbtn2:"E:\Yash\Music\Devotional\Shri Ram Chandra Kripalu Bhajaman(PagalWorld.com.cm).mp3",self.dbtn3:"E:\Yash\Music\Devotional\Ram Aayenge - Swasti Mehul(PagalWorld.com.cm).mp3",self.dbtn4:"E:\Yash\Music\Devotional\Huppa-Huiyya-Swapnil-Bandodkar.mp3",self.dbtn5:"E:\Yash\Music\Devotional\shri ram jay ram jay jay ram .mp3",self.dbtn6:"E:\Yash\Music\Devotional\Ekadantaya Vakratundaya(audiosong.in).mp3",self.dbtn7:"E:\Yash\Music\Devotional\Bajrang baan .mp3"}
        self.dsondaddr=self.dsong_database[self.dsongid]
        self.dsongimg_database={self.dbtn1:"E:\Yash\Python projects\Musify\images\Devotional images\Sri-Venkatesa-Suprabatham.jpg",self.dbtn2:"E:\Yash\Python projects\Musify\images\Devotional images\Sriramachandrajpg.jpg",self.dbtn3:"E:\Yash\Python projects\Musify\images\Devotional images\Ram-Aayenge.jpg",self.dbtn4:"E:\Yash\Python projects\Musify\images\Devotional images\Adipurush-Hindi.jpg",self.dbtn5:"E:\Yash\Python projects\Musify\images\Devotional images\Bajrang-Baan.jpg",self.dbtn6:"E:\Yash\Python projects\Musify\images\Devotional images\Ekadantaya-Vakratundaya.jpg",self.dbtn7:"E:\Yash\Python projects\Musify\images\Devotional images\Bajrang-Baan.jpg"}
        self.dsondimgid=self.dsongimg_database[self.dsongid]
        return self.dsondaddr,self.dsondimgid
    

    def wmp3playerpage(self,wbtn):
        self.wbtnid=wbtn
        self.wsongaddress,self.wsongimgaddress=self.wsongfilestore(self.wbtnid)
        print(self.wsongimgaddress)
        self.wmp3playerobj=MP3_player(self.wsongaddress,self.wsongimgaddress)
        self.check()
        self.wmp3playerobj.show()
    def wsongfilestore(self,btnid):
        self.wsongid=btnid
        print(self.wsongid)
        self.wsong_database={self.wbtn1:"E:\Yash\Music\Workout special\Shwasat Raja Dhyasat Raja (Pawankhind)_64-(PagalWorld.Ink).mp3",self.wbtn2:"E:\Yash\Music\Workout special\Raja Aala (Pawankhind)_64-(PagalWorld.Ink).mp3",self.wbtn3:"E:\Yash\Music\Workout special\Chakar Shivbach Honar(PagalWorld.com.cm).mp3",self.wbtn4:"C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/song/Ekadantaya Vakratundaya_128-(DJMaza).mp3",self.wbtn5:"E:\Yash\Music\Workout special\Shivrajyabhishek Geet (Hirkani)(PagalWorld).mp3",self.wbtn6:"E:\Yash\Music\Workout special\Believer(PagalWorld).mp3",self.wbtn7:"E:\Yash\Music\Workout special\Ab-Tu-Bhaag-Milkha.mp3"}
        self.wsondaddr=self.wsong_database[self.wsongid]
        self.wsongimg_database={self.wbtn1:"asstes\Images\download.png",self.wbtn2:"E:\Yash\Python projects\Musify\images\workout images\Fatteshikast.jpg",self.wbtn3:"E:\Yash\Python projects\Musify\images\workout images\Chakar-Shivbacha-Honar.jpg",self.wbtn4:"C:/Users/abhij/OneDrive/Desktop/Spotify clone/asstes/Images/th (4).jpg",self.wbtn5:"",self.wbtn6:"E:\Yash\Python projects\Musify\images\workout images\Believer.jpg",self.wbtn7:"E:\Yash\Python projects\Musify\images\workout images\Bhaag-Milkha-Bhaag.jpg"}
        self.wsongimgid=self.wsongimg_database[self.wsongid]
        return self.wsondaddr,self.wsongimgid
    def check(self):
        self.rmp3playerobj.fun()
        self.wmp3playerobj.fun()
        self.dmp3playerobj.fun()
        
        
        
        
        

    def return_languagepage(self):
        self.close() 
        
        
        
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    songwindow=Songs()
    songwindow.show()
    sys.exit(app.exec_())
    
    