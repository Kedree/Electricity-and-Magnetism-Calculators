from PyQt5 import QtCore, QtGui, QtWidgets
from subWindowOne import Ui_SubWindow1
from ThreeDPlot import Ui_ThreeDPlot
from PyQt5.QtGui import QPixmap

class Ui_MainWindow(object):
    def openDialog2D(self): # Open our dialog window for options for 2D plot
        self.window1 = QtWidgets.QMainWindow()
        self.ui1 = Ui_SubWindow1()
        self.ui1.setupUi(self.window1)
        self.window1.show()

    def open3D(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui2 = Ui_ThreeDPlot()
        self.ui2.setupUi(self.window2)
        self.window2.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 700)
        MainWindow.setMinimumSize(QtCore.QSize(700, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setBaseSize(QtCore.QSize(1000, 1000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/myPre/TitlePic.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.pic = QtWidgets.QLabel()
        self.pixMap = QPixmap('TitlePic.JPG')
        self.pic.setPixmap(self.pixMap)
        self.pic.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.pic)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openDialog2D())
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.open3D())
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "\"Electric Field Calculator (Ring Charges)"))
        self.label.setText(_translate("MainWindow", "Electric FIeld at a point along the Z axis From Two Ring Charges (Z Axis Centered)"))
        self.pushButton.setText(_translate("MainWindow", "2D Plot with Known r / h Ratio"))
        self.pushButton_2.setText(_translate("MainWindow", "3D Plot with Many r / h Ratios"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
