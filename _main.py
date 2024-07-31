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

'6ab00cb38589   10.196.18.72/tas-rs-hotel   "/sbin/init"   18 hours ago   Up 18 hours   0.0.0.0:80->80/tcp, :::80->80/tcp, 0.0.0.0:27017->27017/tcp, :::27017->27017/tcp   tas-hotel'
'8033cbec0   10.196.18.72/tas-rs-signage   "/sbin/init"   10 months ago   Up 18 hours   0.0.0.0:80->80/tcp, :::80->80/tcp, 0.0.0.0:27017->27017/tcp, :::27017->27017/tcp   tas-signage'