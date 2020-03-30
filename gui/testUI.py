import sys

from PyQt5 import QtGui, QtWidgets

from gui.main_window import Ui_MainWindow
from gui.simulation_trigger import run_matlab_exec
from gui.output_handler import prepare_output


def run_simulation_ui():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyQtApp(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    
class MyQtApp(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)
        self.set_terrain_types()

        self.window = MainWindow

        self.connect_all_widget_pairs()

        self.checkBoxDifferential.setEnabled(False)
        self.comboBoxVehicleType.textHighlighted.connect(self.on_vehicle_type_change)
        self.comboBoxVehicleType.currentTextChanged.connect(self.on_vehicle_type_change)

        self.comboBoxTerrainProfileType.textHighlighted.connect(self.on_terrain_profile_change)
        


    def invoke_sim_trigger(self):
        # Slot for triggering a simulation run

        self.tabWidget.setDisabled(True) # Grey out the GUI

        # Get vehicle data
        vehicle = self.comboBoxVehicleType.currentText()
        self.vehicle_type = self.get_vehicle_type(vehicle)
        
        # Prepare and save output for matlab
        prepare_output(self)

        # Run simulation
        if run_matlab_exec(self.vehicle_type):
            self.tabWidget.setDisabled(False)

    def widget_binding_handler(self, val):
        # Slot to handle Slider-SpinBox widget pair bindings

        sender_name = self.window.sender().objectName()

        if 'Box' in sender_name:
            method = 'slider_' + sender_name.split('_')[-1]
            if 'Offset' in method:
                val *= 10
        elif 'slider' in sender_name:
            method = 'spinBox_' + sender_name.split('_')[-1]
            if 'Offset' in method:
                method = 'doubleS' + method[1:]
                val /= 10
        result = getattr(self, method).setValue(val)
        
    def connect_all_widget_pairs(self):
        self.spinBox_StartPoint.valueChanged.connect(self.widget_binding_handler)
        self.slider_StartPoint.valueChanged.connect(self.widget_binding_handler)
        self.spinBox_EndPoint.valueChanged.connect(self.widget_binding_handler)
        self.slider_EndPoint.valueChanged.connect(self.widget_binding_handler)
        self.doubleSpinBox_Offset.valueChanged.connect(self.widget_binding_handler)
        self.slider_Offset.valueChanged.connect(self.widget_binding_handler)
        self.spinBox_Vel.valueChanged.connect(self.widget_binding_handler)
        self.slider_Vel.valueChanged.connect(self.widget_binding_handler)
        self.spinBox_SimTime.valueChanged.connect(self.widget_binding_handler)
        self.slider_SimTime.valueChanged.connect(self.widget_binding_handler)

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

    def get_vehicle_type(self, vehicle):
        if vehicle in ['M113', 'MK4', 'Namer']:
            return 'wheeled'
        return 'tracked'


if __name__ == "__main__":
    run_simulation_ui()
