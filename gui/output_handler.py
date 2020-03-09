def get_output(qt_app):
    out_dict = {}

    out_dict['vehicleName'] = qt_app.comboBoxVehicleType.currentText()
    out_dict['vehicleType'] = get_vehicle_type(out_dict['vehicleName'])

    out_dict['differential'] = qt_app.checkBoxDifferential.isChecked()
    
    index = qt_app.comboBoxTerrainTypeOptions.currentText()
    out_dict['terrainProfileType'] = qt_app.terrain_types[index]
    
    out_dict['terrainSlopeAngle'] = qt_app.spinBoxSlope.value()

    out_dict['terrainGroundType'] = qt_app.comboBoxTerrainTypeOptions.currentText()

    out_dict['terrainMu'] = qt_app.terrain_types[index]

    # TO BE ADDED:
    # out_dict['simulationTime'] = qt_app.comboBoxTerrainTypeOptions.currentText()

    output = json.dumps(out_dict)
    print(output)


def get_vehicle_type(vehicle):
    if vehicle in ['M113', 'MK4', 'Namer']:
        return 'Wheeled'
    return 'Tracked'
