import inspect
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QThread, pyqtSlot, pyqtSignal

import logging
from datetime import datetime
import os
import sys
import time

from main_ui import Ui_Dialog as Main_Ui

class MainDialog(QDialog):
    def __init__(self):
        # Display minimize, close button
        super().__init__()
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, True)

        self.main_ui = Main_Ui()
        self.main_ui.setupUi(self)
        self.setWindowTitle('QT Sample Dialog')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MainDialog()
    myWindow.show()
    app.exec()