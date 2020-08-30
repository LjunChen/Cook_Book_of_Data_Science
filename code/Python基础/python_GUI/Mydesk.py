# coding=utf-8
'''
author : Liujun Chen
date : 2020/8/7 23:35
'''

from Mydeskui import Ui_MainWindow
import os
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.Qt import QMainWindow

class Sven_Desk(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def runup(self):
        self.pushButton.clicked.connect(self.open_dir)

    def open_dir(self):
        if self.comboBox.currentText()=='Cookbooks':
            os.system('explorer.exe %s' % r'D:\Cookbooks')
            os.system("start %s %s" % (r'D:\Software\typora\Typora\Typora.exe', r'D:\Cookbooks\SUMMARY.md'))
        if self.comboBox.currentText()=='Sven':
            os.system('explorer.exe %s' % r'D:\Sven')
        if self.comboBox.currentText()=='Books':
            os.system("start  %s %s" % (r'D:\Software\adobe\Acobat\Acroba~1\Acrobat\Acrobat.exe', r'D:\Sven\books\books.pdf'))
        if self.comboBox.currentText()=='Paper':
            os.system('explorer.exe %s' % r'D:\Sven\Paper')
        if self.comboBox.currentText()=='Secrets':
            os.system("start %s %s" % (r'EXCEL.EXE', r'D:\Sven\Sven\secret.csv'))
            #os.system('powershell cat D:/Sven/Sven/secret.csv')

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = QMainWindow()
    myUI = Sven_Desk()
    myUI.setupUi(myDlg)
    myUI.runup()
    myDlg.show()
    sys.exit(myapp.exec_())