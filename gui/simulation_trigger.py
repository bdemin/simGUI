from os import getcwd, chdir


def run_exec(vehicle):
    import subprocess
    
    cmd = 'matlab_executables\\test1\\sim_test.exe'
    subprocess.call(cmd)

    # subp = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    # (output, err) = subp.communicate()
    # subp_status = subp.wait()


if __name__ == "__main__":
    run_exec()
