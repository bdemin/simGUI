# from PySide2 import QtWidgets
from PyQt5 import QtGui, QtWidgets

from main_window import Ui_MainWindow

import simulation_trigger
from output_handler import get_output


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

        self.spinBoxSimTime.valueChanged.connect(self.on_spinboxSimTime_val_change)
        self.sliderSimTime.valueChanged.connect(self.on_sliderSimTime_move)
    
        self.pushbtnRunSim.clicked.connect(self.invoke_sim_trigger)

    def invoke_sim_trigger(self):
        # Slot for triggering a simulation run

        self.tabWidget.setDisabled(True) # Grey out the GUI

        # Get vehicle data
        vehicle = self.comboBoxVehicleType.currentText()
        vehicle_type = self.get_vehicle_type(vehicle)
        
        # Prepare output for matlab
        get_output(self)

        # Run simulation
        if run_matlab_exec(vehicle_type):
            self.tabWidget.setDisabled(False)

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

    def on_sliderSimTime_move(self, val):
        self.spinBoxSimTime.setValue(val)

    def on_spinboxSimTime_val_change(self, val):
        self.sliderSimTime.setValue(val)

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

    @property
    def get_vehicle_type(vehicle):
        if vehicle in ['M113', 'MK4', 'Namer']:
            return 'wheeled'
        return 'tracked'

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyQtApp(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
