import json


def get_output(qt_app):
    sim_params_dict = {}

    sim_params_dict['vehicleName'] = qt_app.comboBoxVehicleType.currentText()
    sim_params_dict['vehicleType'] = get_vehicle_type(sim_params_dict['vehicleName'])

    sim_params_dict['differential'] = qt_app.checkBoxDifferential.isChecked()
    
    index = qt_app.comboBoxTerrainTypeOptions.currentText()
    sim_params_dict['terrainProfileType'] = qt_app.terrain_types[index]
    
    sim_params_dict['terrainSlopeAngle'] = qt_app.spinBoxSlope.value()

    sim_params_dict['terrainGroundType'] = qt_app.comboBoxTerrainTypeOptions.currentText()

    sim_params_dict['terrainMu'] = qt_app.terrain_types[index]

    # TO BE ADDED:
    sim_params_dict['simulationTime'] = qt_app.spinBoxSimTime.value()

    json_string = json.dumps(sim_params_dict)
    prepare_sim_output(json_string)

def get_vehicle_type(vehicle):
    if vehicle in ['M113', 'MK4', 'Namer']:
        return 'Wheeled'
    return 'Tracked'

def prepare_sim_output(json_string):
    output_file = 'simulation_input\\' + 'model_input_params.json'
    with open(output_file, 'w') as f:
        json.dump(output, f)
