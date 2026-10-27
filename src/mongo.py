from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLabel
class Mongs(QWidget):

    def __init__(self):
        super().__init__()
        self.mong_ui()

    def mong_ui(self):
        self.btn1 = QPushButton("Song", self)
        self.btn1.setGeometry(100, 100, 150, 200)

        self.add_delete_button(self.btn1)   # ✅ now Python can find it

        def add_delete_button(self, parent_btn):
            del_btn = QPushButton("✕", self)
            del_btn.setFixedSize(20, 20)

        # place at top-right corner of parent button
            del_btn.move(
              parent_btn.x() + parent_btn.width() - 18,
              parent_btn.y() + 5
            )

            del_btn.setStyleSheet("""
                 QPushButton {
                   background-color: red;
                   color: white;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: darkred;
            }
        """)

            del_btn.clicked.connect(
            lambda: self.delete_song(parent_btn, del_btn)
        )

    def delete_song(self, song_btn, del_btn):
        song_btn.deleteLater()
        del_btn.deleteLater()

   
