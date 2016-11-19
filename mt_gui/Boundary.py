# -*- coding:utf-8 -*-
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

        self.setWindowTitle(u"测试平台")     #u"XXX"格式可输入中文
        self.resize(1000, 500)

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
        self.fileMenu.addSeparator()      #添加分割线
        self.fileMenu.addAction(self.exitAct)

        self.helpMenu = QtGui.QMenu("&Help", self)
        self.helpMenu.addAction(self.aboutAct)

        self.menuBar().addMenu(self.fileMenu)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.helpMenu)


class StockDialog(QDialog):
    def __init__(self, parent=None):
        super(StockDialog, self).__init__(parent)

        mainSplitter = QSplitter(Qt.Horizontal)     #水平窗口切分条，改变多窗口部件的大小

        Contentlist = QListWidget(mainSplitter)
        Contentlist.insertItem(0, self.tr("列表1"))
        Contentlist.insertItem(1, self.tr("列表2"))
        Contentlist.insertItem(2, self.tr("列表3"))

        frame = QFrame(mainSplitter)
        ChangeablePart=QGridLayout(frame)
        rightpart1=Rightpart1()
        ChangeablePart.addWidget(rightpart1)

        mainLayout = QHBoxLayout(self)
        mainLayout.addWidget(mainSplitter)
        self.setLayout(mainLayout)


class Rightpart1(QDialog):
    def __init__(self,parent=None):
        super(Rightpart1,self).__init__(parent)

        Introduction = QStackedWidget()
        Introduction.setFrameStyle(QFrame.Panel | QFrame.Raised)
        text1 = Text1()
        text2 = Text2()
        text3 = Text3()
        Introduction.addWidget(text1)
        Introduction.addWidget(text2)
        Introduction.addWidget(text3)

        MianCombo = QComboBox()
        MianCombo.addItem(u"节点信息")
        MianCombo.addItem(u"拓扑结构")

        Information = QStackedWidget()
        Information.setFrameStyle(QFrame.Panel | QFrame.Raised)
        text4 = Text4()
        text5 = Text5()
        Information.addWidget(text4)
        Information.addWidget(text5)

        NewPushButton = QPushButton(self.tr("新建"))
        TestPushButton = QPushButton(self.tr("实验"))
        DeletePushButton = QPushButton(self.tr("删除"))

        ComboLayout = QVBoxLayout()  # 布局，原则是从最小分割开始直到主布局
        ComboLayout.addWidget(MianCombo)
        ComboLayout.addWidget(Information)

        UpLayout = QHBoxLayout()
        UpLayout.addWidget(Introduction)
        UpLayout.addLayout(ComboLayout)

        DownLayout = QHBoxLayout()
        DownLayout.addWidget(NewPushButton)
        DownLayout.addWidget(TestPushButton)
        DownLayout.addWidget(DeletePushButton)

        RightLayout = QVBoxLayout()
        RightLayout.addLayout(UpLayout)
        RightLayout.addLayout(DownLayout)
        self.setLayout(RightLayout)


class Text1(QWidget):
    def __init__(self, parent=None):
        super(Text1, self).__init__(parent)
        remarkTextEdit = QTextEdit()
        layout = QGridLayout(self)
        layout.addWidget(remarkTextEdit)


class Text2(QWidget):
    def __init__(self, parent=None):
        super(Text2, self).__init__(parent)
        remarkTextEdit = QTextEdit()
        layout = QGridLayout(self)
        layout.addWidget(remarkTextEdit)


class Text3(QWidget):
    def __init__(self, parent=None):
        super(Text3, self).__init__(parent)
        remarkTextEdit = QTextEdit()
        layout = QGridLayout(self)
        layout.addWidget(remarkTextEdit)


class Text4(QWidget):
    def __init__(self, parent=None):
        super(Text4, self).__init__(parent)
        remarkTextEdit = QTextEdit()
        layout = QGridLayout(self)
        layout.addWidget(remarkTextEdit)


class Text5(QWidget):
    def __init__(self, parent=None):
        super(Text5, self).__init__(parent)
        remarkTextEdit = QTextEdit()
        layout = QGridLayout(self)
        layout.addWidget(remarkTextEdit)




if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
