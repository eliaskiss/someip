# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainHSUUPJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from module.trans import getIds, hexStringToByte, ConvertPayloadToHexString
from module.form import SomeIpForm

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 480)
        MainWindow.setMinimumSize(QSize(720, 480))
        MainWindow.setMaximumSize(QSize(720, 480))

        font = QFont()
        font.setFamily(u"Open Sans")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        MainWindow.setIconSize(QSize(16, 16))
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Triangular)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFont(font)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(360, -10, 3, 600))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(580, 400, 121, 61))

        font1 = QFont()
        font1.setFamily(u"Open Sans")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.start.setFont(font1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 240, 30))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"border: 1px solid black")
        self.label.setAlignment(Qt.AlignCenter)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 150, 240, 30))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"border: 1px solid black")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(420, 20, 240, 30))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"border: 1px solid black")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(20, 60, 321, 32))

        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.label_7 = QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(True)
        self.label_7.setStyleSheet(u"border-bottom: 1px solid gray")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.address_sim = QTextEdit(self.horizontalLayoutWidget_3)
        self.address_sim.setObjectName(u"address_sim")
        self.address_sim.setEnabled(True)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.address_sim.sizePolicy().hasHeightForWidth())
        
        self.address_sim.setSizePolicy(sizePolicy)
        self.address_sim.setMaximumSize(QSize(16777215, 30))
        self.address_sim.setFont(font)

        self.horizontalLayout_4.addWidget(self.address_sim)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(20, 100, 321, 32))

        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.label_8 = QLabel(self.horizontalLayoutWidget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"border-bottom: 10px solid gray")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.port_sim = QTextEdit(self.horizontalLayoutWidget_4)
        self.port_sim.setObjectName(u"port_sim")
        self.port_sim.setEnabled(True)
        
        sizePolicy.setHeightForWidth(self.port_sim.sizePolicy().hasHeightForWidth())
        
        self.port_sim.setSizePolicy(sizePolicy)
        self.port_sim.setMaximumSize(QSize(16777215, 30))
        self.port_sim.setFont(font)

        self.horizontalLayout_5.addWidget(self.port_sim)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)
        
        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(20, 190, 321, 32))

        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.label_9 = QLabel(self.horizontalLayoutWidget_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.protocol = QTextEdit(self.horizontalLayoutWidget_5)
        self.protocol.setObjectName(u"protocol")
        self.protocol.setEnabled(True)

        sizePolicy.setHeightForWidth(self.protocol.sizePolicy().hasHeightForWidth())
        
        self.protocol.setSizePolicy(sizePolicy)
        self.protocol.setMaximumSize(QSize(16777215, 30))
        self.protocol.setFont(font)

        self.horizontalLayout_6.addWidget(self.protocol)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)

        self.horizontalLayoutWidget_6 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(20, 230, 321, 32))

        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.label_10 = QLabel(self.horizontalLayoutWidget_6)

        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 30))
        self.label_10.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.message_id = QTextEdit(self.horizontalLayoutWidget_6)
        self.message_id.setObjectName(u"message_id")
        self.message_id.setEnabled(True)

        sizePolicy.setHeightForWidth(self.message_id.sizePolicy().hasHeightForWidth())
        
        self.message_id.setSizePolicy(sizePolicy)
        self.message_id.setMaximumSize(QSize(16777215, 30))
        self.message_id.setFont(font)

        self.horizontalLayout_7.addWidget(self.message_id)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)

        self.horizontalLayoutWidget_7 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(20, 270, 321, 32))

        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.label_11 = QLabel(self.horizontalLayoutWidget_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 30))
        self.label_11.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_11)

        self.message_type = QComboBox(self.horizontalLayoutWidget_7)
        self.message_type.addItem("")
        self.message_type.addItem("")
        self.message_type.addItem("")
        self.message_type.addItem("")
        self.message_type.addItem("")
        self.message_type.addItem("")
        self.message_type.addItem("")
        self.message_type.addItem("")
        self.message_type.addItem("")
        self.message_type.addItem("")
        self.message_type.addItem("")
        self.message_type.addItem("")
        self.message_type.addItem("")
        self.message_type.addItem("")
        self.message_type.addItem("")
        self.message_type.setObjectName(u"message_type")
        
        sizePolicy.setHeightForWidth(self.message_type.sizePolicy().hasHeightForWidth())
        
        self.message_type.setSizePolicy(sizePolicy)
        self.message_type.setFont(font)
        self.message_type.setIconSize(QSize(16, 30))

        self.horizontalLayout_8.addWidget(self.message_type)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)

        self.horizontalLayoutWidget_8 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(20, 310, 321, 32))

        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.label_12 = QLabel(self.horizontalLayoutWidget_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 30))
        self.label_12.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_12)

        self.message_status = QComboBox(self.horizontalLayoutWidget_8)
        self.message_status.addItem("")
        self.message_status.addItem("")
        self.message_status.addItem("")
        self.message_status.addItem("")
        self.message_status.addItem("")
        self.message_status.addItem("")
        self.message_status.addItem("")
        self.message_status.addItem("")
        self.message_status.addItem("")
        self.message_status.addItem("")
        self.message_status.addItem("")
        self.message_status.setObjectName(u"message_status")

        sizePolicy.setHeightForWidth(self.message_status.sizePolicy().hasHeightForWidth())
        
        self.message_status.setSizePolicy(sizePolicy)
        self.message_status.setFont(font)

        self.horizontalLayout_9.addWidget(self.message_status)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 2)

        self.horizontalLayoutWidget_9 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(20, 350, 321, 32))

        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.label_13 = QLabel(self.horizontalLayoutWidget_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 30))
        self.label_13.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_13)

        self.client_id = QTextEdit(self.horizontalLayoutWidget_9)
        self.client_id.setObjectName(u"client_id")
        self.client_id.setEnabled(True)

        sizePolicy.setHeightForWidth(self.client_id.sizePolicy().hasHeightForWidth())
        
        self.client_id.setSizePolicy(sizePolicy)
        self.client_id.setMaximumSize(QSize(16777215, 30))
        self.client_id.setFont(font)

        self.horizontalLayout_10.addWidget(self.client_id)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 2)
        self.horizontalLayoutWidget_10 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(20, 390, 321, 32))

        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.label_14 = QLabel(self.horizontalLayoutWidget_10)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 30))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"border-bottom: 1px solid gray")

        self.horizontalLayout_11.addWidget(self.label_14)

        self.session_id = QTextEdit(self.horizontalLayoutWidget_10)
        self.session_id.setObjectName(u"session_id")
        self.session_id.setEnabled(True)
        sizePolicy.setHeightForWidth(self.session_id.sizePolicy().hasHeightForWidth())
        self.session_id.setSizePolicy(sizePolicy)
        self.session_id.setMaximumSize(QSize(16777215, 30))
        self.session_id.setFont(font)

        self.horizontalLayout_11.addWidget(self.session_id)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 2)
        self.horizontalLayoutWidget_11 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(20, 430, 321, 32))
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.horizontalLayoutWidget_11)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 30))
        self.label_15.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_15)

        self.payload = QTextEdit(self.horizontalLayoutWidget_11)
        self.payload.setObjectName(u"payload")
        self.payload.setEnabled(True)
        sizePolicy.setHeightForWidth(self.payload.sizePolicy().hasHeightForWidth())
        self.payload.setSizePolicy(sizePolicy)
        self.payload.setMaximumSize(QSize(16777215, 30))
        self.payload.setFont(font)

        self.horizontalLayout_12.addWidget(self.payload)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 2)
        self.horizontalLayoutWidget_12 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_12.setObjectName(u"horizontalLayoutWidget_12")
        self.horizontalLayoutWidget_12.setGeometry(QRect(380, 60, 321, 32))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.horizontalLayoutWidget_12)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 30))
        self.label_16.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_16)

        self.address_dest = QTextEdit(self.horizontalLayoutWidget_12)
        self.address_dest.setObjectName(u"address_dest")
        self.address_dest.setEnabled(True)

        sizePolicy.setHeightForWidth(self.address_dest.sizePolicy().hasHeightForWidth())
        
        self.address_dest.setSizePolicy(sizePolicy)
        self.address_dest.setMaximumSize(QSize(16777215, 30))
        self.address_dest.setFont(font)

        self.horizontalLayout_13.addWidget(self.address_dest)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 2)
        self.horizontalLayoutWidget_13 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_13.setObjectName(u"horizontalLayoutWidget_13")
        self.horizontalLayoutWidget_13.setGeometry(QRect(380, 100, 321, 32))
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.horizontalLayoutWidget_13)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 30))
        self.label_17.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_17)

        self.port_dest = QTextEdit(self.horizontalLayoutWidget_13)
        self.port_dest.setObjectName(u"port_dest")
        self.port_dest.setEnabled(True)
        sizePolicy.setHeightForWidth(self.port_dest.sizePolicy().hasHeightForWidth())
        self.port_dest.setSizePolicy(sizePolicy)
        self.port_dest.setMaximumSize(QSize(16777215, 30))
        self.port_dest.setFont(font)

        self.horizontalLayout_14.addWidget(self.port_dest)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 2)

        QWidget.setTabOrder(self.address_sim, self.port_sim)
        QWidget.setTabOrder(self.port_sim, self.protocol)
        QWidget.setTabOrder(self.protocol, self.message_id)
        QWidget.setTabOrder(self.message_id, self.message_type)
        QWidget.setTabOrder(self.message_type, self.message_status)
        QWidget.setTabOrder(self.message_status, self.client_id)
        QWidget.setTabOrder(self.client_id, self.session_id)
        QWidget.setTabOrder(self.session_id, self.payload)
        QWidget.setTabOrder(self.payload, self.address_dest)
        QWidget.setTabOrder(self.address_dest, self.port_dest)
        QWidget.setTabOrder(self.port_dest, self.start)

        self.address_sim.setTabChangesFocus(True)
        self.address_dest.setTabChangesFocus(True)

        self.port_sim.setTabChangesFocus(True)
        self.port_dest.setTabChangesFocus(True)

        self.protocol.setTabChangesFocus(True)
        self.message_id.setTabChangesFocus(True)
        self.client_id.setTabChangesFocus(True)
        self.session_id.setTabChangesFocus(True)
        self.payload.setTabChangesFocus(True)

        MainWindow.setCentralWidget(self.centralwidget)

        self.start.clicked.connect(self.send)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SOMEIP", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Simulation ECU Information", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Message Information", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Destination ECU Information", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Port number", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Protocol version", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Message ID", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Message Type", None))
        self.message_type.setItemText(0, QCoreApplication.translate("MainWindow", u"REQUEST", None))
        self.message_type.setItemText(1, QCoreApplication.translate("MainWindow", u"REQUEST_NO_RETURN", None))
        self.message_type.setItemText(2, QCoreApplication.translate("MainWindow", u"REQUEST_ACK", None))
        self.message_type.setItemText(3, QCoreApplication.translate("MainWindow", u"REQUEST_NO_RETURN_ACK", None))
        self.message_type.setItemText(4, QCoreApplication.translate("MainWindow", u"NOTIFICATION", None))
        self.message_type.setItemText(5, QCoreApplication.translate("MainWindow", u"RESPONSE", None))
        self.message_type.setItemText(6, QCoreApplication.translate("MainWindow", u"RESPONSE_ACK", None))
        self.message_type.setItemText(7, QCoreApplication.translate("MainWindow", u"ERROR", None))
        self.message_type.setItemText(8, QCoreApplication.translate("MainWindow", u"ERROR_ACK", None))
        self.message_type.setItemText(9, QCoreApplication.translate("MainWindow", u"TP_REQUEST", None))
        self.message_type.setItemText(10, QCoreApplication.translate("MainWindow", u"TP_REQUEST_NO_RETURN", None))
        self.message_type.setItemText(11, QCoreApplication.translate("MainWindow", u"TP_NOTIFICATION", None))
        self.message_type.setItemText(12, QCoreApplication.translate("MainWindow", u"TP_RESPONSE", None))
        self.message_type.setItemText(13, QCoreApplication.translate("MainWindow", u"TP_ERROR", None))
        self.message_type.setItemText(14, QCoreApplication.translate("MainWindow", u"NOTIFICATION_ACK", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Message Status", None))
        self.message_status.setItemText(0, QCoreApplication.translate("MainWindow", u"E_OK", None))
        self.message_status.setItemText(1, QCoreApplication.translate("MainWindow", u"E_NOT_OK", None))
        self.message_status.setItemText(2, QCoreApplication.translate("MainWindow", u"E_UNKNOWN_SERVICE", None))
        self.message_status.setItemText(3, QCoreApplication.translate("MainWindow", u"E_UNKNOWN_METHOD", None))
        self.message_status.setItemText(4, QCoreApplication.translate("MainWindow", u"E_NOT_READY", None))
        self.message_status.setItemText(5, QCoreApplication.translate("MainWindow", u"E_NOT_REACHABLE", None))
        self.message_status.setItemText(6, QCoreApplication.translate("MainWindow", u"E_TIMEOUT", None))
        self.message_status.setItemText(7, QCoreApplication.translate("MainWindow", u"E_WRONG_PROTOCOL_VERSION", None))
        self.message_status.setItemText(8, QCoreApplication.translate("MainWindow", u"E_WRONG_INTERFACE_VERSION", None))
        self.message_status.setItemText(9, QCoreApplication.translate("MainWindow", u"E_MALFORMED_MESSAGE", None))
        self.message_status.setItemText(10, QCoreApplication.translate("MainWindow", u"E_WRONG_MESSAGE_TYPE", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Client ID", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Session ID", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Payload", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Port Number", None))
    # retranslateUi

    def getVariables(self):
        address_sim = self.address_sim.toPlainText()
        address_dest = self.address_dest.toPlainText()

        try:
            port_sim = int(self.port_sim.toPlainText())
            port_dest = int(self.port_dest.toPlainText())
        except:
            raise Exception("포트 번호를 확인해 주세요.")
        
        try:
            protocol_ver = int(self.protocol.toPlainText())
        except:
            raise Exception("프로토콜 버전을 확인해 주세요.")
        
        try:
            message_id = self.message_id.toPlainText()
            service_id, method_id = getIds(message_id)
        except:
            raise Exception("메세지 ID를 확인해 주세요.")
        
        try:
            client_id = int(self.client_id.toPlainText())
        except:
            raise Exception("클라이언트 ID를 확인해 주세요.")
            
        try:
            session_id = int(self.session_id.toPlainText())
        except:
            raise Exception("세션 ID를 확인해 주세요.")
        
        try:
            payload = ConvertPayloadToHexString(self.payload.toPlainText())
            payload = hexStringToByte(payload)
        except:
            raise Exception("payload를 변환할 수 없습니다.\n입력값을 확인해주세요.")

        msg_type = self.message_type.currentText()
        msg_status = self.message_status.currentText()

        return address_sim, address_dest, port_sim, port_dest, protocol_ver, service_id, method_id, client_id, session_id, msg_type, msg_status, payload

    def send(self):
        try:
            address_sim, address_dest, port_sim, port_dest, protocol_ver, service_id, method_id, client_id, session_id, msg_type, msg_status, payload = self.getVariables()

        except ValueError as e:
            QMessageBox.critical(self, "오류가 발생했습니다.", f"올바르지 않은 입력 값입니다.\n입력 값을 확인해 주세요.\n{e}")
            return
        
        except Exception as e:
            QMessageBox.critical(self, "오류가 발생했습니다.", f"올바르지 않은 입력 값입니다.\n{e}")
            return
        
        try:
            form = SomeIpForm(
                proto = protocol_ver,
                msg_type = msg_type,
                ret_code = msg_status,
                srv_id = service_id,
                method_id = method_id,
                client_id = client_id,
                session_id = session_id,
                payload = payload
            )

            form.setIp(address_sim, address_dest)
            form.setUdp(port_sim, port_dest)
            form.setPacket()
            # form.viewPacket()
            form.send()

            QMessageBox.information(self, "전송 완료", "전송 완료")
            return

        except Exception as e:
            QMessageBox.critical(self, "오류가 발생했습니다.", f"전송중 오류가 발생했습니다.\n입력값을 확인한 뒤 다시 시도해주세요. \n{e}")
            return
