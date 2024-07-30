import sys
from PyQt5 import QtWidgets
from module.ui import Ui_MainWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()

    sys.exit(app.exec_())

