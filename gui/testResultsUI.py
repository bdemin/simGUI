# from PySide2 import QtWidgets
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

    def invoke_plot(self):
        sender_name = self.window.sender().objectName()

        if sender_name == 'pushBtnChsPosTime':
            data = ([0,1,2,3,4], [10,1,20,3,40])
            self.canvas.axes.clear()
            self.canvas.axes.plot(data, '*-')
            self.canvas.draw()

        elif sender_name == 'pushBtnChsVelTime':
            self.canvas.axes.clear()
            self.canvas.draw()


import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        
        super(MplCanvas, self).__init__(fig)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = MyQtApp(window)
    window.show()
    sys.exit(app.exec_())
