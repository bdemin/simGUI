# from PySide2 import QtWidgets
from PyQt5 import QtGui, QtWidgets

from main_window import Ui_MainWindow

class MyQtApp(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)

        self.comboBoxVehicleType.textHighlighted.connect(self.on_vehicle_type_change)
        self.comboBoxVehicleType.currentTextChanged.connect(self.on_vehicle_type_change)
    def on_vehicle_type_change(self, val):
        image = ":/Vehicles/" + val + ".jpg"
        self.labelVehicleImg.setPixmap(QtGui.QPixmap(image))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyQtApp(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
