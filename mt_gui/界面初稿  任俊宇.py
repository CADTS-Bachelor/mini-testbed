# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class StockDialog(QDialog):
    def __init__(self,parent=None):
        super(StockDialog,self).__init__(parent)
        self.setWindowTitle(self.tr("窗口界面"))
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint)  #######允许窗体最大最小化
        mainSplitter=QSplitter(Qt.Horizontal)####创建一个水平分割窗，作为主布局框

        listWidget= QListWidget(mainSplitter)######在水平分割窗的左侧窗体中插入一个QListWidget作为条目选择框，
                                             # 并在列表框中依次插入相应的条目
        listWidget.insertItem(0,self.tr( "列表1"))
        listWidget.insertItem(1,self.tr( "列表2"))
        listWidget.insertItem(2,self.tr( "列表3"))

        frame=QFrame(mainSplitter)
        stack=QStackedWidget()  #####创建一个QStackWidget对象
        stack.setFrameStyle(QFrame.Panel|QFrame.Raised)#####调用setFrameStyle()方法对堆栈窗的显示风格进行设置

        ######顺序插入三个页面
        t1=T1()
        t2=T2()
        t3=T3()
        stack.addWidget(t1)
        stack.addWidget(t2)
        stack.addWidget(t3)

        closePushButton=QPushButton(self.tr("关闭"))#####添加按钮

        buttonLayout = QHBoxLayout()######创建按钮并用QHBoxLayout对其进行布局
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(closePushButton)

        mainLayout=QVBoxLayout(frame)#####QVBoxLayout生成主布局
        mainLayout.setMargin(10)
        mainLayout.setSpacing(6)
        mainLayout.addWidget(stack)
        mainLayout.addLayout(buttonLayout)

        self.connect(listWidget,SIGNAL("currentRowChanged(int)"),stack,SLOT( "setCurrentIndex(int)"))
        ######把列表框的currentRowChanged()信号与堆栈窗的setCurrentIndex()槽相连接，达到按选择的条目显示页面的要求。
        self.connect(closePushButton,SIGNAL("clicked()"),self,SLOT( "close()"))

        layout=QHBoxLayout(self)
        layout.addWidget(mainSplitter)
        self.setLayout(layout)

class T1(QWidget):
    def __init__(self,parent=None):
        super(T1,self).__init__(parent)
        label1=QLabel(self.tr("word:"))

        remarkTextEdit=QTextEdit()

        layout = QGridLayout(self)
        layout.addWidget(label1,3,0)
        layout.addWidget(remarkTextEdit,3,1)

class T2(QWidget):
    def __init__(self, parent=None):
        super(T2, self).__init__(parent)
        label2= QLabel(self.tr("word:"))

        remarkTextEdit = QTextEdit()

        layout = QGridLayout(self)
        layout.addWidget(label2, 3, 0)
        layout.addWidget(remarkTextEdit, 3, 1)

class T3(QWidget):
    def __init__(self, parent=None):
        super(T3, self).__init__(parent)
        label3= QLabel(self.tr("word:"))

        remarkTextEdit = QTextEdit()

        layout = QGridLayout(self)
        layout.addWidget(label3, 3, 0)
        layout.addWidget(remarkTextEdit, 3, 1)

app=QApplication(sys.argv)
main=StockDialog()
main.show( )
app.exec_()