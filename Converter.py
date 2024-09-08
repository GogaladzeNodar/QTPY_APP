from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QComboBox, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal
from Config import conversion_rates

class ConvertPage(QWidget):

    logout_requested = pyqtSignal()

    def __init__(self):
        super(ConvertPage, self).__init__()
        loadUi("UI_Files/converter.ui", self)
        self.setFixedSize(800, 600)

        # Log Out Button
        self.LogOutButt = self.findChild(QPushButton, "pushButton_3")

        # Amount Button
        self.ConvertButt = self.findChild(QPushButton, "pushButton")

        # Clear Button
        self.ClearButt = self.findChild(QPushButton, "pushButton_2")

        # Amount line 
        self.Amount = self.findChild(QLineEdit, name="lineEdit")

        #Converted Amount
        self.ConvertedAmount = self.findChild(QLineEdit, "lineEdit_2")

        # FROM ComboBox 
        self.FromComboBox = self.findChild(QComboBox, "comboBox")
        self.FromComboBox.addItems(list(conversion_rates.keys()))
        # set current index 
        self.FromComboBox.setCurrentIndex(0)  
        

        # TO ComboBox
        self.ToComboBox = self.findChild(QComboBox, "comboBox_2")
        self.ToComboBox.addItems(list(conversion_rates.keys()))
        self.ToComboBox.setCurrentIndex(1)  


        # define conection of LOGOUT button and LOGOUT function  
        self.LogOutButt.clicked.connect(self.LogOut)  
        self.ClearButt.clicked.connect(self.ClearFields)   
        self.ConvertButt.clicked.connect(self.HandleConvert)



    def HandleConvert(self):
        try:
            # Get the amount entered by the user
            amount = float(self.Amount.text())

            # Get the selected currencies
            from_currency = self.FromComboBox.currentText()
            to_currency = self.ToComboBox.currentText()


            # Perform the conversion
            if from_currency == to_currency:
                converted_amount = amount
            else:
                if from_currency in conversion_rates and to_currency in conversion_rates[from_currency]:
                    rate = conversion_rates[from_currency][to_currency]
                    converted_amount = amount * rate
                else:
                    raise ValueError("Conversion rate not available")

            # Display the converted amount
            self.ConvertedAmount.setText(f"{converted_amount:.2f}")

        except ValueError as ve:
            QMessageBox.warning(self, "Conversion Error", str(ve))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {str(e)}")


    def ClearFields(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()



    def LogOut(self):
        #Signal that logout is required
        self.logout_requested.emit()
