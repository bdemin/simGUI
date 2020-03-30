import json


save_folder = '..//mobility_predictor//input//'

def prepare_output(qt_app):
    vehicle = {}
    terrain = {}
    simulation = {}
    control = {}

    vehicle['Name'] = qt_app.comboBoxVehicleType.currentText()
    vehicle['Type'] = qt_app.vehicle_type
    vehicle['Differential_Mode'] = qt_app.checkBoxDifferential.isChecked()
    vehicle['Damper'] = '111111' # what is this?

    # index = qt_app.comboBoxTerrainProfileType.currentText() # Update needed
    # terrain['Type'] = qt_app.terrain_types[index] # Can be simplified?
    # terrain['mu'] = qt_app.terrain_types[index]
    terrain['Profile'] = qt_app.comboBoxTerrainTypeOptions.currentText()
    terrain['Road_Start'] = -10
    terrain['Road_End'] = 600
    terrain['Offset'] = -0.9

    terrain['Slope_Angle'] = qt_app.spinBoxSlope.value()

    simulation['Time'] = qt_app.spinBoxSimTime.value()

    control['Velocity_Spline'] = 0

    # Prepare a dict container for JSON output
    output_data = {}
    output_data['vehicle'] = vehicle
    output_data['terrain'] = terrain
    output_data['simulation'] = simulation
    output_data['control'] = control

    fake_data_test(output_data) # TESTING

    # Output parameters into JSON files
    with open(save_folder + 'input2matlab' + '.txt', 'w') as out_file:
            json.dump(output_data, out_file)


def fake_data_test(data):
    data['vehicle']['Type'] = 'Track'
    data['vehicle']['Name'] = 'Namer'
    
    data['terrain']['Type'] = 'Road'
    data['terrain']['mu'] = 0.2
    data['terrain']['Profile'] = 'Slope_And_Step'
    data['terrain']['Road_Start'] = -10
    data['terrain']['Road_End'] = 600
    data['terrain']['Offset'] = -0.9

    data['simulation']['Time'] = 60

    import numpy as np
    data['control']['Velocity_Spline'] = np.zeros((2, 6))
    data['control']['Velocity_Spline'][2:-1] = 5.55
    data['control']['Velocity_Spline'][0,1] = 5
    data['control']['Velocity_Spline'][0,2] = 10
    data['control']['Velocity_Spline'][0,3] = 35
    data['control']['Velocity_Spline'][0,4] = 40
    data['control']['Velocity_Spline'][0,5] = 100
    data['control']['Velocity_Spline'] = data['control']['Velocity_Spline'].tolist()

    # Fix key names
    data['Vehicle'] = data['vehicle']
    del data['vehicle']

    data['Terrain'] = data['terrain']
    del data['terrain']

    data['Simulation'] = data['simulation']
    del data['simulation']

    data['Control'] = data['control']
    del data['control']
