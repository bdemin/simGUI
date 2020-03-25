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

    index = qt_app.comboBoxTerrainTypeOptions.currentText()
    terrain['Type'] = qt_app.terrain_types[index] # Can be simplified?
    terrain['mu'] = qt_app.terrain_types[index]
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

    # Output parameters into JSON files
    with open(save_folder + 'input2matlab' + '.txt', 'w') as out_file:
            json.dump(output_data, out_file)

    
    out_dict['terrainSlopeAngle'] = qt_app.spinBoxSlope.value()

    out_dict['terrainGroundType'] = qt_app.comboBoxTerrainTypeOptions.currentText()

    out_dict['terrainMu'] = qt_app.terrain_types[index]

    # TO BE ADDED:
    out_dict['simulationTime'] = qt_app.spinBoxSimTime.value()

    output = json.dumps(out_dict)
    print(output)


def get_vehicle_type(vehicle):
    if vehicle in ['M113', 'MK4', 'Namer']:
        return 'Wheeled'
    return 'Tracked'
