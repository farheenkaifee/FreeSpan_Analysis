import os 
import sys
import time
from typing_extensions import Self
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *                                                                   
from PyQt5.QtPrintSupport import *
import PyQt5.QtGui as QtGui
from PyQt5.QtGui import *
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import * 
import sys
from app import Ui_MainWindow



class MainWindow(QtWidgets.QMainWindow):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        # self.window1 = QtWidgets.QMainWindow()
        # self.ui = Ui_MainWindow1()
        # self.ui.setupUi(self.window1)
        # self.window1.show()
        # self.window2 = QtWidgets.QMainWindow()
        # self.ui = Ui_FreeSpan_Inputs()
        # self.ui.setupUi(self.window2)
        # self.window2.show()
    

    # def newWindow(self):
    #     self.window1 = QtWidgets.QMainWindow()
    #     self.ui = Ui_MainWindow1()
    #     self.ui.setupUi(self.window1)
    #     self.window1.show()

        


    def __init__(self):
        super(MainWindow,self).__init__()


        self.setWindowTitle("MainWindow")
        self.resize(1641, 863)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets\Window_icon.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setToolTip("main screen")
        self.centralwidget = QtWidgets.QWidget(self)
        # self.centralwidget.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")

        self.loadimage= QLabel(self.centralwidget)
        Pixmap = QPixmap("bbbbbbbbbbbbbbbb.jpg")
        self.loadimage.setPixmap(Pixmap.scaled(1350,770)) 


        self.information = QtWidgets.QLabel(self.centralwidget)
        self.information.setGeometry(QtCore.QRect(30, 30, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.information.setFont(font)
        self.information.setObjectName("information")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(700, 280, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        # self.widget.setGeometry(QtCore.QRect(20, 70, 151, 181))
        self.widget.setGeometry(QtCore.QRect(500, 100, 151, 181))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.project_name = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)

        # Project Name
        self.project_name.setFont(font)
        self.project_name.setObjectName("project_name")
        self.verticalLayout.addWidget(self.project_name)
        self.project_manager = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)

        #Project Manager
        self.project_manager.setFont(font)
        self.project_manager.setObjectName("project_manager")
        self.verticalLayout.addWidget(self.project_manager)
        self.client_name = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)

        #Client Name
        self.client_name.setFont(font)
        self.client_name.setObjectName("client_name")
        self.verticalLayout.addWidget(self.client_name)
        self.start_date = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)

        # Start Date
        self.start_date.setFont(font)
        self.start_date.setObjectName("start_date")
        self.verticalLayout.addWidget(self.start_date)
        self.end_date = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)

        # End Date
        self.end_date.setFont(font)
        self.end_date.setObjectName("end_date")
        self.verticalLayout.addWidget(self.end_date)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        # self.widget1.setGeometry(QtCore.QRect(190, 70, 141, 181))
        self.widget1.setGeometry(QtCore.QRect(650, 100, 151, 181))
        self.widget1.setObjectName("widget1")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.pro_name_edit = QtWidgets.QLineEdit(self.widget1)
        self.pro_name_edit.setObjectName("pro_name_edit")
        self.verticalLayout_2.addWidget(self.pro_name_edit)

        self.pro_manag_edit = QtWidgets.QLineEdit(self.widget1)
        self.pro_manag_edit.setObjectName("pro_manag_edit")
        self.verticalLayout_2.addWidget(self.pro_manag_edit)

        self.client_name_edit = QtWidgets.QLineEdit(self.widget1)
        self.client_name_edit.setObjectName("client_name_edit")
        self.verticalLayout_2.addWidget(self.client_name_edit)

        self.dateEdit = QtWidgets.QDateEdit(self.widget1)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_2.addWidget(self.dateEdit)

        self.dateEdit_2 = QtWidgets.QDateEdit(self.widget1)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.verticalLayout_2.addWidget(self.dateEdit_2)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 564, 21))
        self.menubar.setObjectName("menubar")

        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")

        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(self)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./assets/new.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon1)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(self)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./assets/open.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(self)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./assets/close_dis.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon3)
        self.actionClose.setObjectName("actionClose")
        self.actionExit = QtWidgets.QAction(self)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./assets/close.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        self.actionExit.setObjectName("actionExit")
        self.actionhelp = QtWidgets.QAction(self)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./assets/help.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionhelp.setIcon(icon5)
        self.actionhelp.setObjectName("actionhelp")
        self.actionAbout_Software = QtWidgets.QAction(self)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./assets/about.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_Software.setIcon(icon6)
        self.actionAbout_Software.setObjectName("actionAbout_Software")
        self.actionMximise = QtWidgets.QAction(self)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./assets/maximise.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMximise.setIcon(icon7)
        self.actionMximise.setObjectName("actionMximise")
        self.actionMinimise = QtWidgets.QAction(self)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./assets/minimise.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMinimise.setIcon(icon8)
        self.actionMinimise.setObjectName("actionMinimise")
        self.actionSave = QtWidgets.QAction(self)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("./assets/save.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon9)
        self.actionSave.setObjectName("actionSave")
        self.actionPrint = QtWidgets.QAction(self)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("./assets/print.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon10)
        self.actionPrint.setObjectName("actionPrint")
        self.menuMenu.addAction(self.actionNew)
        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addAction(self.actionOpen)
        self.menuMenu.addAction(self.actionClose)
        self.menuMenu.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionhelp)
        self.menuHelp.addAction(self.actionAbout_Software)
        self.menuSettings.addAction(self.actionMximise)
        self.menuSettings.addAction(self.actionMinimise)
        self.menuSettings.addAction(self.actionPrint)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(self)
        self.actionNew.triggered.connect(self.openWindow)
        self.actionOpen.triggered.connect(self.openWindow)
        self.actionExit.triggered.connect(self.close) # type: ignore
        self.actionMinimise.triggered.connect(self.showMinimized) # type: ignore
        self.actionMximise.triggered.connect(self.showMaximized) # type: ignore
        self.actionClose.triggered.connect(self.close) # type: ignore
        self.actionPrint.triggered.connect(self.print_info) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)
        self.submit_button.clicked.connect(self.openWindow)
        # self.ui.actionPrint.triggered.connect(self.print_info)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "FreeSpan"))
        self.setStatusTip(_translate("MainWindow", "MainWindow"))
        # self.information.setText(_translate("MainWindow", "Information"))
        self.submit_button.setStatusTip(_translate("MainWindow", "Submit "))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.project_name.setText(_translate("MainWindow", "Project No :"))
        self.project_manager.setText(_translate("MainWindow", "Project Manager:"))
        self.client_name.setText(_translate("MainWindow", "Client Name:"))
        self.start_date.setText(_translate("MainWindow", "Project start date:"))
        self.end_date.setText(_translate("MainWindow", "Project End Date:"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "New Project"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setStatusTip(_translate("MainWindow", "Close file"))
        self.actionClose.setShortcut(_translate("MainWindow", "Shift+Q"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Quit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionhelp.setText(_translate("MainWindow", "Help"))
        self.actionhelp.setStatusTip(_translate("MainWindow", "Help you need"))
        self.actionAbout_Software.setText(_translate("MainWindow", "About Software"))
        self.actionAbout_Software.setStatusTip(_translate("MainWindow", "About this software"))
        self.actionMximise.setText(_translate("MainWindow", "Maximise"))
        self.actionMximise.setStatusTip(_translate("MainWindow", "Maximise Window"))
        self.actionMximise.setShortcut(_translate("MainWindow", "Shift+M"))
        self.actionMinimise.setText(_translate("MainWindow", "Minimise"))
        self.actionMinimise.setStatusTip(_translate("MainWindow", "Minimise Window"))
        self.actionMinimise.setShortcut(_translate("MainWindow", "Shift+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save File"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint.setStatusTip(_translate("MainWindow", "Print"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
    

    def print_info(self):
        print("Project Name : {0}".format(self.pro_name_edit.text()))
        print("Client Name : {0}".format(self.client_name_edit.text()))
        print("Project Manager : {0}".format(self.pro_manag_edit.text()))
        print("Project Start Date : {0}".format(self.dateEdit.text()))
        print("Project End Date : {0}".format(self.dateEdit_2.text()))
        # self.window = QtWidgets.QMainWindow()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self.window)
        # self.window.show()





class SplashScreen(QWidget):

	def __init__(self):
		super().__init__()
		self.setWindowTitle('FREESPAN ANALYSIS CALCULATION')
		self.setGeometry(350,50,700,700)
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)
		
		self.msgBox = QMessageBox()
		self.msgBox.setIcon(QMessageBox.Information)
		self.msgBox.setText("Please Enter Quantity")
		self.msgBox.setWindowTitle("ERROR")
		self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		
		self.counter = 0
		self.n = 300000

		self.initUI()
		self.timer = QTimer()
		self.timer.timeout.connect(self.loading)
		self.timer.start(0)
	
	def initUI(self):
		layout = QVBoxLayout()
		self.setLayout(layout)
		self.frame = QFrame()
		layout.addWidget(self.frame)
		self.labelTitle = QLabel(self.frame)
		self.labelTitle.setObjectName('LabelTitle')

        # center labels believe in yrself
		self.labelTitle.resize(600, 400)
		self.labelTitle.move(0, 40) # x, y
		self.labelTitle.setPixmap(QPixmap('FinalSPlashScreen.png'))
		self.labelTitle.setAlignment(Qt.AlignCenter)

		self.labelDescription = QLabel(self.frame)
		self.labelDescription.resize(self.width() - 10, 50)
		self.labelDescription.move(0, self.labelTitle.height())
		self.labelDescription.setObjectName('LabelDesc')
		self.labelDescription.setText('.')
		self.labelDescription.setAlignment(Qt.AlignCenter)

		self.progressBar = QProgressBar(self.frame)
		self.progressBar.resize(self.width() - 200-10, 5)
		self.progressBar.move(100, self.labelDescription.y() + 130)
		self.progressBar.setAlignment(Qt.AlignCenter)
		self.progressBar.setFormat('%p%')
		self.progressBar.setTextVisible(True)
		self.progressBar.setRange(0, self.n)
		self.progressBar.setValue(20)
		self.progressBar.setStyleSheet("QProgressBar::chunk "
                          "{"
                          "background-color: #134868;"
                          "}")
		 
	def loading(self):
		self.progressBar.setValue(self.counter)
		if self.counter == int(self.n * 0.3):
			self.labelDescription.setText('.')
		elif self.counter == int(self.n * 0.6):
			self.labelDescription.setText('.')
		elif self.counter >= self.n:
			self.timer.stop()
			self.close()
			time.sleep(1)
			
			self.myApp = MainWindow()
			self.myApp.show()
			
		self.counter += 1
    
    
    








if __name__ == "__main__":
  
    app = QtWidgets.QApplication(sys.argv)

    splash = SplashScreen()
    splash.show()

    #MainWindow = QtWidgets.QMainWindow()
    #ui = MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    try:
        sys.exit(app.exec_())
    
    except SystemExit:
        print("\n\t Application is closing...!!\n")
