from PyQt4 import QtGui
import forms.design_signup
import db
import bcrypt
from misc import redirect_window


class SignupWindow(QtGui.QDialog, forms.design_signup.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.label_4.setText("")
        redirect_window(self, "LoginWindow")
        event.accept()


    def center_on_screen(self):
        resolution =QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                (resolution.height() / 2) - (self.frameSize().height() / 2))


    def click_signup(self):
        db.create_table()
        user = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if user.isalpha() and password != "":
            if not db.verify_user(user, password):
                password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                db.create_user(user, password)
                msg = """User successfully registered!\nYou will be redirected to login screen"""
                QtGui.QMessageBox.question(self, 'Application Message',
                    msg, QtGui.QMessageBox.Yes)
                redirect_window(self, "LoginWindow")
                return True
            else:
                self.label_4.setText("This username already exists.\nTry again with other name.")
                return False
        else:
            self.label_4.setText("This username can't have only numbers\nand can't be composed only spaces. The password can't be empty.")
