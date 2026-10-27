from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QComboBox
from EventStore import EventStore


class ViewCategories(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Event Categories")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        self.event_type = QComboBox()
        self.event_type.addItems(["Wedding", "Birthday", "Conference"])
        self.event_type.currentTextChanged.connect(self.load_categories)

        self.list_widget = QListWidget()

        layout.addWidget(self.event_type)
        layout.addWidget(self.list_widget)

        self.setLayout(layout)

        self.load_categories("Wedding")

    def load_categories(self, event):
        self.list_widget.clear()
        self.list_widget.addItems(EventStore.get_categories(event))
