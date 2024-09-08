from PyQt5.QtWidgets import QWidget, QMessageBox, QPushButton, QLineEdit
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal


class LoginPage(QWidget):

    login_successful = pyqtSignal()  # Define the signal

    def __init__(self):
        super(LoginPage, self).__init__()
        loadUi("UI_Files/form.ui", self) 
        self.setFixedSize(800, 600)

        # login button
        self.LogInButton = self.findChild(QPushButton, "pushButton")
        # Username line
        self.UserNameLine = self.findChild(QLineEdit, "lineEdit")
        # Password line 
        self.PassWordLine = self.findChild(QLineEdit, "lineEdit_2")


        self.LogInButton.clicked.connect(self.Authenticate)

    
    def Authenticate(self):
        # text from username line
        username = self.UserNameLine.text()
        # text from password line
        password = self.PassWordLine.text()


        if username == "admin" and password == "admin":
            self.login_successful.emit()

        else: QMessageBox.warning(self, "Error", "Invalid username or password")

