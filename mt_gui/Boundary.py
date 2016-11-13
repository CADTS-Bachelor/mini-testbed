# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui, QtCore
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.stockdialog = StockDialog()
        self.setCentralWidget(self.stockdialog)
        self.createActions()
        self.createMenus()

        self.setWindowTitle("测试平台")
        self.resize(800, 500)

        self.setWindowFlags(Qt.WindowMinMaxButtonsHint)  #######允许窗体最大最小化

    def open(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                                                     '/home')
        fname = open(filename)
        data = fname.read()
        self.remarkTextEdit.setText(data)

    def save(self):
        fileName = QtGui.QFileDialog.getSaveFileName(self)


    def about(self):
        QtGui.QMessageBox.about(self, "About test",
                "This is the Pyqt test! ")

    def createActions(self):
        self.openAct = QtGui.QAction("&Open...", self, shortcut="Ctrl+O",
                triggered=self.open)

        self.exitAct = QtGui.QAction("&Exit", self, shortcut="Ctrl+Q",
                triggered=self.close)

        self.aboutAct = QtGui.QAction("&About", self, triggered=self.about)

        self.saveAct = QtGui.QAction("Save", self, shortcut="Ctrl+S",
                                     triggered=self.save)


    def createMenus(self):


        self.fileMenu = QtGui.QMenu("&File", self)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.helpMenu = QtGui.QMenu("&Help", self)
        self.helpMenu.addAction(self.aboutAct)

        self.menuBar().addMenu(self.fileMenu)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.helpMenu)


class StockDialog(QDialog):
    def __init__(self,parent=None):
        super(StockDialog,self).__init__(parent)
        mainSplitter=QSplitter(Qt.Horizontal,self)

        LeftlistWidget= QListWidget(mainSplitter)
        LeftlistWidget.insertItem(0,self.tr( "列表1"))
        LeftlistWidget.insertItem(1,self.tr( "列表2"))
        LeftlistWidget.insertItem(2,self.tr( "列表3"))

        RightSplitter=QSplitter(Qt.Horizontal,mainSplitter)
        RightSplitter.setOpaqueResize(True)


        Middlestacktext=QStackedWidget()  #####创建一个QStackWidget对象
        Middlestacktext.setFrameStyle(QFrame.Panel|QFrame.Raised)#####调用setFrameStyle()方法对堆栈窗的显示风格进行设置

        text1=Text1()
        text2=Text2()
        text3=Text3()
        Middlestacktext.addWidget(text1)
        Middlestacktext.addWidget(text2)
        Middlestacktext.addWidget(text3)

        self.connect(LeftlistWidget,SIGNAL("currentRowChanged(int)"),Middlestacktext,SLOT( "setCurrentIndex(int)"))
        ######把列表框的currentRowChanged()信号与堆栈窗的setCurrentIndex()槽相连接，达到按选择的条目显示页面的要求。



        Rightstacktext = QStackedWidget()
        Rightstacktext.setFrameStyle(QFrame.Panel | QFrame.Raised)

        text4 = Text4()
        text5 = Text5()
        text6 = Text6()
        Rightstacktext.addWidget(text4)
        Rightstacktext.addWidget(text5)
        Rightstacktext.addWidget(text6)


        mainLayout = QHBoxLayout(mainSplitter) #####QVBoxLayout生成主布局
        mainLayout.setMargin(10)
        mainLayout.setSpacing(6)
        mainLayout.addWidget(Middlestacktext)
        mainLayout.addWidget(Rightstacktext)


        self.connect(LeftlistWidget, SIGNAL("currentRowChanged(int)"), Rightstacktext, SLOT("setCurrentIndex(int)"))
        ######把列表框的currentRowChanged()信号与堆栈窗的setCurrentIndex()槽相连接，达到按选择的条目显示页面的要求。

        layout = QHBoxLayout(self)
        layout.addWidget(mainSplitter)
        self.setLayout(layout)

class Text1(QWidget):
    def __init__(self,parent=None):
        super(Text1,self).__init__(parent)
        label1=QLabel()

        remarkTextEdit=QTextEdit()

        layout = QGridLayout(self)
        layout.addWidget(label1,3,0)
        layout.addWidget(remarkTextEdit,5,1)


class Text2(QWidget):
    def __init__(self, parent=None):
        super(Text2, self).__init__(parent)
        label2= QLabel()

        remarkTextEdit = QTextEdit()

        layout = QGridLayout(self)
        layout.addWidget(label2, 3, 0)
        layout.addWidget(remarkTextEdit, 5, 1)


class Text3(QWidget):
    def __init__(self, parent=None):
        super(Text3, self).__init__(parent)
        label3= QLabel()

        remarkTextEdit = QTextEdit()

        layout = QGridLayout(self)
        layout.addWidget(label3, 3, 0)
        layout.addWidget(remarkTextEdit, 5, 1)


class Text4(QWidget):
    def __init__(self,parent=None):
        super(Text4,self).__init__(parent)
        label4=QLabel()

        remarkTextEdit=QTextEdit()

        layout = QGridLayout(self)
        layout.addWidget(label4,3,0)
        layout.addWidget(remarkTextEdit,5,1)


class Text5(QWidget):
    def __init__(self, parent=None):
        super(Text5, self).__init__(parent)
        label5= QLabel()

        remarkTextEdit = QTextEdit()

        layout = QGridLayout(self)
        layout.addWidget(label5, 3, 0)
        layout.addWidget(remarkTextEdit, 5, 1)


class Text6(QWidget):
    def __init__(self, parent=None):
        super(Text6, self).__init__(parent)
        label6= QLabel()

        remarkTextEdit = QTextEdit()

        layout = QGridLayout(self)
        layout.addWidget(label6, 3, 0)
        layout.addWidget(remarkTextEdit, 5, 1)


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
