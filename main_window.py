from PyQt4 import QtGui
import sys
import forms.design_main


class MainWindow(QtGui.QMainWindow, forms.design_main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start_search_ac = [0]
        self.start_search_av = [0]
        self.start_search_cm = [0]
        self.start_search_dm = [0]
        self.start_search_fic = [0]
        self.start_search_cr = [0]
        self.start_search_rm = [0]
        self.start_search_hr = [0]


    def closeEvent(self, event):
        quit_msg = "Are you sure you want to quit?"
        reply = QtGui.QMessageBox.question(self, 'Application Message',
                quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def center_on_screen(self):
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                (resolution.height() / 2) - (self.frameSize().height() / 2))
