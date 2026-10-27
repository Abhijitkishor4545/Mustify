import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QComboBox
)
from page2 import EventDetailsPage


class EventForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Event")
        self.setFixedSize(350, 400)
        self.ui()

    def ui(self):
        layout = QVBoxLayout()

        self.event_name = QLineEdit()
        self.event_name.setPlaceholderText("Event Name")

        self.event_type = QComboBox()
        self.event_type.addItems(["Wedding", "Birthday", "Conference", "Party"])

        self.location = QLineEdit()
        self.location.setPlaceholderText("Location")

        self.job_desc = QLineEdit()
        self.job_desc.setPlaceholderText("Job Description")

        submit_btn = QPushButton("Submit")
        submit_btn.clicked.connect(self.open_next_page)

        layout.addWidget(self.event_name)
        layout.addWidget(self.event_type)
        layout.addWidget(self.location)
        layout.addWidget(self.job_desc)
        layout.addWidget(submit_btn)

        self.setLayout(layout)

    def open_next_page(self):
        # ----- GET DATA -----
        name = self.event_name.text()
        etype = self.event_type.currentText()
        location = self.location.text()
        job = self.job_desc.text()

        # ----- OPEN PAGE 2 WITH DATA -----
        self.next_page = EventDetailsPage(name, etype, location, job)
        self.next_page.show()
        self.close()   # optional
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EventForm()
    window.show()
    sys.exit(app.exec_())
