from PyQt5 import QtGui, QtWidgets
from PyQt5 import QtCore

from results_window import Ui_MainWindow


class MyQtApp(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.window = window

        self.canvas = MplCanvas(self.framePlot, width=50, height=4, dpi=100)
        self.verticalLayout_3.addWidget(self.canvas)

        self.pushBtnChsPosTime.clicked.connect(self.invoke_plot)
        self.pushBtnChsVelTime.clicked.connect(self.invoke_plot)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = MyQtApp(window)
    window.show()
    sys.exit(app.exec_())
