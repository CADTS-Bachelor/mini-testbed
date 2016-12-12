#  -*- coding:utf-8 -*-
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

        self.setWindowTitle(u"测试平台")  # u"XXX"格式可输入中文
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
        self.fileMenu.addSeparator()  # 添加分割线
        self.fileMenu.addAction(self.exitAct)

        self.helpMenu = QtGui.QMenu("&Help", self)
        self.helpMenu.addAction(self.aboutAct)

        self.menuBar().addMenu(self.fileMenu)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.helpMenu)


class StockDialog(QTabWidget):
    def __init__(self, parent=None):
        super(StockDialog, self).__init__(parent)

        self.mainSplitter = QSplitter(Qt.Horizontal)  # 水平窗口切分条，改变多窗口部件的大小

        contentlist = QListWidget(self.mainSplitter)
        contentlist.insertItem(0, self.tr("列表1"))
        contentlist.insertItem(1, self.tr("列表2"))

        changeablePart = QTabWidget(self.mainSplitter)
        rightpart2 = CreatPart()
        rightpart3 = TestPart()
        changeablePart.addTab(rightpart2, u"新建")
        changeablePart.addTab(rightpart3, u"实验")

        self.connect(contentlist, SIGNAL("currentRowChanged(int)"),
                     rightpart2.introductionEdit, SLOT("setCurrentIndex(int)"))

        self.connect(contentlist, SIGNAL("currentRowChanged(int)"),
                     rightpart2.topoEdit, SLOT("setCurrentIndex(int)"))

        self.connect(contentlist, SIGNAL("currentRowChanged(int)"),
                     rightpart3.introductionShow, SLOT("setCurrentIndex(int)"))

        self.connect(contentlist, SIGNAL("currentRowChanged(int)"),
                     rightpart3.informationShow, SLOT("setCurrentIndex(int)"))

        self.connect(contentlist, SIGNAL("currentRowChanged(int)"),
                     rightpart3.topoShow, SLOT("setCurrentIndex(int)"))

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.mainSplitter)
        self.mainSplitter.setStretchFactor(0, 1)
        self.mainSplitter.setStretchFactor(1, 2)
        self.setLayout(mainLayout)


class TestPart(QDialog):
    def __init__(self, parent=None):
        super(TestPart, self).__init__(parent)

        self.introLabel = QLabel(u"实验背景")
        self.introLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.introductionShow = QStackedWidget()
        self.introductionShow.setFrameStyle(QFrame.Panel | QFrame.Raised)
        introductionText1 = IntroductionText1()
        introductionText2  = IntroductionText2()
        self.introductionShow.addWidget(introductionText1)
        self.introductionShow.addWidget(introductionText2)
        self.introLabel.setBuddy(self.introductionShow)

        LeftLayout = QVBoxLayout()
        LeftLayout.addWidget(self.introLabel)
        LeftLayout.addWidget(self.introductionShow)

        self.testCombo = QComboBox()
        self.testCombo.addItem(u"节点信息")
        self.testCombo.addItem(u"拓扑结构")

        self.informationShow = QStackedWidget()
        self.informationShow.setFrameStyle(QFrame.Panel | QFrame.Raised)
        infoText1 = InfoText1()
        infoText2 = InfoText2()
        self.informationShow.addWidget(infoText1)
        self.informationShow.addWidget(infoText2)

        self.topoShow = QStackedWidget()
        self.topoShow.setFrameStyle(QFrame.Panel | QFrame.Raised)
        topoText1 = TopoText1()
        topoText2 = TopoText2()
        self.topoShow.addWidget(topoText1)
        self.topoShow.addWidget(topoText2)

        RightLayout = QVBoxLayout()
        RightLayout.addWidget(self.testCombo)
        RightLayout.addWidget(self.informationShow)

        TestLayout = QHBoxLayout()
        TestLayout.addLayout(LeftLayout)
        TestLayout.addLayout(RightLayout)
        self.setLayout(TestLayout)


class CreatPart(QDialog):
    def __init__(self, parent=None):
        super(CreatPart, self).__init__(parent)

        self.nameLabel = QLabel(u"实验名称：")
        self.nameEdit = QLineEdit()
        self.nameLabel.setBuddy(self.nameEdit)

        self.formLabel = QLabel(u"实验类型：")
        self.formCombo = QComboBox()
        self.formCombo.addItem("WEB")
        self.formCombo.addItem("Misc")
        self.formLabel.setBuddy(self.formCombo)

        self.introductionLabel = QLabel(u"实验介绍：")
        self.introductionEdit = QStackedWidget()
        introTextEdit1 = IntroTextEdit1()
        introTextEdit2 = IntroTextEdit2()
        self.introductionEdit.addWidget(introTextEdit1)
        self.introductionEdit.addWidget(introTextEdit2)
        self.introductionLabel.setBuddy(self.introductionEdit)

        self.topoLabel = QLabel(u"拓扑绘制：")
        self.topoEdit = QStackedWidget()
        topoTextEdit1 = TopoTextEdit1()
        topoTextEdit2 = TopoTextEdit2()
        self.topoEdit.addWidget(topoTextEdit1)
        self.topoEdit.addWidget(topoTextEdit2)
        self.topoLabel.setBuddy(self.topoEdit)

        self.paintButton = QPushButton(self.tr("拓扑绘制"))
        self.saveButton = QPushButton(self.tr("保存"))

        ButtonLayout = QHBoxLayout()
        ButtonLayout.addWidget(self.paintButton)
        ButtonLayout.addWidget(self.saveButton)

        LeftLayout = QGridLayout()
        LeftLayout.addWidget(self.nameLabel, 0, 0)
        LeftLayout.addWidget(self.nameEdit, 0, 1)
        LeftLayout.addWidget(self.formLabel, 1, 0)
        LeftLayout.addWidget(self.formCombo, 1, 1)
        LeftLayout.addWidget(self.introductionLabel, 2, 0)
        LeftLayout.addWidget(self.introductionEdit, 2, 1)

        RightLayout = QVBoxLayout()
        RightLayout.addWidget(self.topoEdit)
        RightLayout.addLayout(ButtonLayout)

        GenLayout = QHBoxLayout()
        GenLayout.addLayout(LeftLayout)
        GenLayout.addWidget(self.topoLabel)
        GenLayout.addLayout(RightLayout)
        self.setLayout(GenLayout)


class IntroductionText1(QWidget):
    def __init__(self, parent=None):
        super(IntroductionText1, self).__init__(parent)
        remarkTextEdit = QTextEdit()
        layout = QGridLayout(self)
        layout.addWidget(remarkTextEdit)


class IntroductionText2(QWidget):
    def __init__(self, parent=None):
        super(IntroductionText2, self).__init__(parent)
        remarkTextEdit = QTextEdit()
        layout = QGridLayout(self)
        layout.addWidget(remarkTextEdit)


class InfoText1(QWidget):
    def __init__(self, parent=None):
        super(InfoText1, self).__init__(parent)
        remarkTextEdit = QTextEdit()
        layout = QGridLayout(self)
        layout.addWidget(remarkTextEdit)


class InfoText2(QWidget):
    def __init__(self, parent=None):
        super(InfoText2, self).__init__(parent)
        remarkTextEdit = QTextEdit()
        layout = QGridLayout(self)
        layout.addWidget(remarkTextEdit)


class TopoText1(QWidget):
    def __init__(self, parent=None):
        super(TopoText1, self).__init__(parent)
        remarkTextEdit = QTextEdit()
        layout = QGridLayout(self)
        layout.addWidget(remarkTextEdit)


class TopoText2(QWidget):
    def __init__(self, parent=None):
        super(TopoText2, self).__init__(parent)
        remarkTextEdit = QTextEdit()
        layout = QGridLayout(self)
        layout.addWidget(remarkTextEdit)


class InfoTextEdit1(QWidget):
    def __init__(self, parent=None):
        super(InfoTextEdit1, self).__init__(parent)
        remarkTextEdit = QTextEdit()
        layout = QGridLayout(self)
        layout.addWidget(remarkTextEdit)


class InfoTextEdit2(QWidget):
    def __init__(self, parent=None):
        super(InfoTextEdit2, self).__init__(parent)
        remarkTextEdit = QTextEdit()
        layout = QGridLayout(self)
        layout.addWidget(remarkTextEdit)


class TopoTextEdit1(QWidget):
    def __init__(self, parent=None):
        super(TopoTextEdit1, self).__init__(parent)
        remarkTextEdit = QTextEdit()
        layout = QGridLayout(self)
        layout.addWidget(remarkTextEdit)


class TopoTextEdit2(QWidget):
    def __init__(self, parent=None):
        super(TopoTextEdit2, self).__init__(parent)
        remarkTextEdit = QTextEdit()
        layout = QGridLayout(self)
        layout.addWidget(remarkTextEdit)


class IntroTextEdit1(QWidget):
    def __init__(self, parent=None):
        super(IntroTextEdit1, self).__init__(parent)
        remarkTextEdit = QTextEdit()
        layout = QGridLayout(self)
        layout.addWidget(remarkTextEdit)


class IntroTextEdit2(QWidget):
    def __init__(self, parent=None):
        super(IntroTextEdit2, self).__init__(parent)
        remarkTextEdit = QTextEdit()
        layout = QGridLayout(self)
        layout.addWidget(remarkTextEdit)


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
