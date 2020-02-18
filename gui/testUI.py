# from PySide2 import QtWidgets
from PyQt5 import QtWidgets

from main_window import Ui_MainWindow

class MyQtApp(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyQtApp(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())