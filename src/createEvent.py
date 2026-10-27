'''import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QComboBox, QDateEdit
)
from PyQt5.QtCore import Qt, QDate


class EventUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Events")
        self.setFixedSize(360, 650)
        self.ui()

    def ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("Events")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 22px;
                font-weight: bold;
            }
        """)

        # Section Heading
        heading = QLabel("Event Details :")
        heading.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: #d32f2f;
                font-weight: bold;
            }
        """)

        # Event Name
        event_name = QLineEdit()
        event_name.setPlaceholderText("Event Name")

        # Event Type
        event_type = QComboBox()
        event_type.addItems(["Event Type", "Wedding", "Birthday", "Conference", "Party"])

        # Date Selector
        date_edit = QDateEdit()
        date_edit.setCalendarPopup(True)
        date_edit.setDate(QDate.currentDate())
        date_edit.setDisplayFormat("dd/MM/yyyy")

        # Event Location
        location = QLineEdit()
        location.setPlaceholderText("Event Location")

        # Job Description
        job_desc = QLineEdit()
        job_desc.setPlaceholderText("Job Description")

        # Submit Button
        submit_btn = QPushButton("Submit")
        submit_btn.setFixedHeight(40)

        # Styling Inputs & Button
        input_style = """
            QLineEdit, QComboBox, QDateEdit {
                padding: 10px;
                border: 1px solid #bdbdbd;
                border-radius: 8px;
                font-size: 14px;
            }
        """

        button_style = """
            QPushButton {
                background-color: #c8e6c9;
                color: #d32f2f;
                border-radius: 20px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #a5d6a7;
            }
        """

        self.setStyleSheet(input_style + button_style)

        # Add widgets to layout
        main_layout.addWidget(title)
        main_layout.addSpacing(10)
        main_layout.addWidget(heading)
        main_layout.addWidget(event_name)
        main_layout.addWidget(event_type)
        main_layout.addWidget(date_edit)
        main_layout.addWidget(location)
        main_layout.addWidget(job_desc)
        main_layout.addSpacing(20)
        main_layout.addWidget(submit_btn, alignment=Qt.AlignCenter)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EventUI()
    window.show()
    sys.exit(app.exec_())'''


import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QComboBox,
    QDateEdit, QFileDialog
)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPixmap


class EventUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Events")
        self.setFixedSize(360, 700)
        self.ui()

    def ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(12)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # ---------- TOP IMAGE PREVIEW ----------
        self.event_image = QLabel("Tap to add event image")
        self.event_image.setFixedSize(320, 160)
        self.event_image.setAlignment(Qt.AlignCenter)
        self.event_image.setStyleSheet("""
            QLabel {
                border: 2px dashed #bdbdbd;
                border-radius: 10px;
                color: gray;
            }
        """)

        # ---------- IMAGE PICK BUTTON ----------
        img_btn = QPushButton("Add Event Image")
        img_btn.clicked.connect(self.select_image)

        # ---------- TITLE ----------
        title = QLabel("Events")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size:22px; font-weight:bold;")

        heading = QLabel("Event Details :")
        heading.setStyleSheet("font-size:16px; color:#d32f2f; font-weight:bold;")

        # ---------- INPUTS ----------
        event_name = QLineEdit()
        event_name.setPlaceholderText("Event Name")

        event_type = QComboBox()
        event_type.addItems(["Event Type", "Wedding", "Birthday", "Conference", "Party"])

        date_edit = QDateEdit()
        date_edit.setCalendarPopup(True)
        date_edit.setDate(QDate.currentDate())

        location = QLineEdit()
        location.setPlaceholderText("Event Location")

        job_desc = QLineEdit()
        job_desc.setPlaceholderText("Job Description")

        submit_btn = QPushButton("Submit")
        submit_btn.setFixedHeight(40)

        # ---------- STYLES ----------
        self.setStyleSheet("""
            QLineEdit, QComboBox, QDateEdit {
                padding: 10px;
                border: 1px solid #bdbdbd;
                border-radius: 8px;
                font-size: 14px;
            }

            QPushButton {
                background-color: #c8e6c9;
                color: #d32f2f;
                border-radius: 18px;
                font-size: 15px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #a5d6a7;
            }
        """)

        # ---------- LAYOUT ----------
        main_layout.addWidget(self.event_image)
        main_layout.addWidget(img_btn)
        main_layout.addWidget(title)
        main_layout.addWidget(heading)
        main_layout.addWidget(event_name)
        main_layout.addWidget(event_type)
        main_layout.addWidget(date_edit)
        main_layout.addWidget(location)
        main_layout.addWidget(job_desc)
        main_layout.addSpacing(10)
        main_layout.addWidget(submit_btn, alignment=Qt.AlignCenter)

        self.setLayout(main_layout)

    # ---------- IMAGE SELECT FUNCTION ----------
    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Event Image",
            "",
            "Images (*.png *.jpg *.jpeg)"
        )

        if file_path:
            pixmap = QPixmap(file_path)
            self.event_image.setPixmap(
                pixmap.scaled(
                    self.event_image.width(),
                    self.event_image.height(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )
            self.event_image.setStyleSheet("border:none;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EventUI()
    window.show()
    sys.exit(app.exec_())


