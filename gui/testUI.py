# from PySide2 import QtWidgets
from PyQt5 import QtGui, QtWidgets

from main_window import Ui_MainWindow

class MyQtApp(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)
        self.set_terrain_types()

        self.checkBoxDifferential.setEnabled(False)
        self.comboBoxVehicleType.textHighlighted.connect(self.on_vehicle_type_change)
        self.comboBoxVehicleType.currentTextChanged.connect(self.on_vehicle_type_change)

        self.comboBoxTerrainProfileType.textHighlighted.connect(self.on_terrain_profile_change)
        
        self.comboBoxTerrainTypeOptions.currentTextChanged.connect(self.on_terrain_type_change)

        self.doubleSpinBoxHeight.valueChanged.connect(self.on_spinboxHeight_val_change)
        self.sliderHeight.valueChanged.connect(self.on_sliderHeight_move)

        self.doubleSpinBoxDistance.valueChanged.connect(self.on_spinboxDistance_val_change)
        self.sliderDistance.valueChanged.connect(self.on_sliderDistance_move)

        self.spinBoxSlope.valueChanged.connect(self.on_spinboxAngle_val_change)
        self.sliderSlope.valueChanged.connect(self.on_sliderSlope_move)

        self.pushbtnRunSim.clicked.connect(self.on_sim_trigger)
        
    def on_sim_trigger(self):
        self.tabWidget.setDisabled(True)

    def on_sliderHeight_move(self, val):
        self.doubleSpinBoxHeight.setValue(val / 10)

    def on_spinboxHeight_val_change(self, val):
        self.sliderHeight.setValue(val * 10)

    def on_sliderDistance_move(self, val):
        self.doubleSpinBoxDistance.setValue(val)

    def on_spinboxDistance_val_change(self, val):
        self.sliderDistance.setValue(val)

    def on_sliderSlope_move(self, val):
        self.spinBoxSlope.setValue(val)

    def on_spinboxAngle_val_change(self, val):
        self.sliderSlope.setValue(val)


    def on_vehicle_type_change(self, val):
        image = ":/Vehicles/" + val + ".jpg"
        self.labelVehicleImg.setPixmap(QtGui.QPixmap(image))

        if val == 'Eitan':
            self.checkBoxDifferential.setEnabled(True)
        else:
            self.checkBoxDifferential.setEnabled(False)


    def on_terrain_type_change(self, val):
        values = self.terrain_types[val] # list
        self.labelTerrainParams.setText(f"\u03BC = {values[0]} |  Ci = {values[1]} | Ri = {values[2]}")

    def on_terrain_profile_change(self, val):
        if val == 'Flat':
            pass
        elif val == 'Step':
            pass
        elif val == 'Slope':
            pass
        print(val)

    def set_terrain_types(self):
        self.terrain_types = {'LETE Sand': [1,2,3],
                            'Sand': [2,3,4],
                            'Clay': [3,4,5]}


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyQtApp(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
