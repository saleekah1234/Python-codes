# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import math 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 250, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 150, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 200, 67, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 150, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(240, 190, 113, 25))
        self.lineEdit2.setObjectName("lineEdit2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menumenu = QtWidgets.QMenu(self.menubar)
        self.menumenu.setObjectName("menumenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsquare = QtWidgets.QAction(MainWindow)
        self.actionsquare.setObjectName("actionsquare")
        self.actioncube = QtWidgets.QAction(MainWindow)
        self.actioncube.setObjectName("actioncube")
        self.actionsqr_root = QtWidgets.QAction(MainWindow)
        self.actionsqr_root.setObjectName("actionsqr_root")
        self.actioncuberoot = QtWidgets.QAction(MainWindow)
        self.actioncuberoot.setObjectName("actioncuberoot")
        self.menumenu.addAction(self.actionsquare)
        self.menumenu.addAction(self.actioncube)
        self.menumenu.addAction(self.actionsqr_root)
        self.menumenu.addAction(self.actioncuberoot)
        self.menubar.addAction(self.menumenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

	self.menuFile.triggered[QtWidgets.QAction].connect(self.menufunction)

  
	

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "calculate"))
        self.label.setText(_translate("MainWindow", "Number"))
        self.label_2.setText(_translate("MainWindow", "Result"))
        self.menumenu.setTitle(_translate("MainWindow", "menu"))
        self.actionsquare.setText(_translate("MainWindow", "square"))
        self.actioncube.setText(_translate("MainWindow", "cube"))
        self.actionsqr_root.setText(_translate("MainWindow", "sqrRoot"))
        self.actioncuberoot.setText(_translate("MainWindow", "cuberoot"))
    def menufunction(self,action):
	txt=(action.text())
	no=int(self.lineEdit.txt())
	print(txt,no)
	if txt=='square':
		self.lineEdit2.setText(str(no*no))
	if txt=='cube':
		self.lineEdit2.setText(str(no*no*no))
	if txt=='sqrRoot':
		self.lineEdit2.setText(str(math.sqrt(no)))
	if txt=='cuberoot':
		self.lineEdit2.setText(str(math.pow(no,1/3)))
	

	
	
	
	


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

