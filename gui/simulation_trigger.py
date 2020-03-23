import subprocess


def run_matlab_exec(vehicle_type):
    # Run main solver matlab executable

    cmd = '..\\mobility_predictor\\'
    cmd += vehicle_type + '_vehicle\\'
    cmd += 'exec\\MainFile.exe'

    try:
        subprocess.call(cmd)
    except:
        raise Exception('Invalid vehicle type')

    return True


def run_test_exec(vehicle):
    # Test-run simple matlab executable
    
    cmd = 'matlab_executables\\test1\\sim_test.exe'
    subprocess.call(cmd)

    # subp = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    # (output, err) = subp.communicate()
    # subp_status = subp.wait()
    return True


if __name__ == "__main__":
    run_test_exec()
