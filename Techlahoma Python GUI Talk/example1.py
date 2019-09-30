#! /usr/bin/python3

import sys
from PySide2.QtWidgets import (QApplication, QLabel, QWidget,
                               QVBoxLayout)

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()
label = QLabel("<font size=40> Hello Techlahoma! </font>")
layout.addWidget(label)
window.setLayout(layout)
window.setWindowTitle("Hello Techlahoma!")
window.show()
app.exec_()
