from PyQt5.QtWidgets import QApplication, QStackedWidget
import sys
from LogIn import LoginPage
from Converter import ConvertPage

class App(QStackedWidget):
    def __init__(self):
        super(App, self).__init__()

        # Create instances of the pages
        self.login_page = LoginPage()
        self.converter_page = ConvertPage()
        

        # Add pages to the stack
        self.addWidget(self.login_page)  # Index 0
        self.addWidget(self.converter_page)  # Index 1

        # Connect signals
        self.login_page.login_successful.connect(self.show_converter_page)
        self.converter_page.logout_requested.connect(self.show_login_page)

    def show_converter_page(self):
        # Switch to the converter page
        self.setCurrentIndex(1)

    def show_login_page(self):
        # Switch to the login page
        self.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
