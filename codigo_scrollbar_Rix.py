import sys
from PySide6.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create the scroll area
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setGeometry(10, 10, 280, 180)

        # Create a widget for the scroll area
        widget = QWidget()
        widget.setGeometry(0, 0, 280, 180)

        # Create grid layout for the widget
        layout = QGridLayout(widget)

        # Create 20 labels and add them to the layout
        for i in range(20):
            label = QLabel(f"Label {i+1}")
            layout.addWidget(label, i, 0)

        # Set the widget for the scroll area
        scroll_area.setWidget(widget)

        # Set the layout of the main window
        self.setLayout(QVBoxLayout(self))
        self.layout().addWidget(scroll_area)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())