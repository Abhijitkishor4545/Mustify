from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout


class EventDetailsPage(QWidget):
    def __init__(self, event_name, event_type, location, job_desc):
        super().__init__()
        self.setWindowTitle("Event Details")
        self.setFixedSize(350, 300)

        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"Event Name: {event_name}"))
        layout.addWidget(QLabel(f"Event Type: {event_type}"))
        layout.addWidget(QLabel(f"Location: {location}"))
        layout.addWidget(QLabel(f"Job Description: {job_desc}"))

        self.setLayout(layout)
