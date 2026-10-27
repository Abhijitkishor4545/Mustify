
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLabel

def add_delete_button(self, parent_btn):
    del_btn = QPushButton("✕", self)
    del_btn.setFixedSize(22, 22)

    # position at top-right of parent button
    del_btn.move(
        parent_btn.x() + parent_btn.width() - 20,
        parent_btn.y() + 5
    )

    del_btn.setStyleSheet("""
        QPushButton {
            background-color: red;
            color: white;
            border-radius: 11px;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: darkred;
        }
    """)

    del_btn.clicked.connect(lambda: self.delete_song(parent_btn, del_btn))
