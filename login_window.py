from PyQt4 import QtGui
import sys
import forms.design_login
import db
from misc import redirect_window


class LoginWindow(QtGui.QMainWindow, forms.design_login.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


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


    def click_login(self):
        db.create_table()
        user = self.lineEdit
        password = self.lineEdit_2
        if db.verify_user(user.text(), password.text(), True):
            redirect_window(self, "MainWindow")
        else:
            self.label_4.setText("Your credentials, are incorrect.\nTry Again.")
            user.setText("")
            password.setText("")
