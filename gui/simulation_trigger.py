from os import getcwd, chdir

import matlab.engine


def run():
    print('Matlab Engine is running\n')

    cwd = getcwd()
    chdir(cwd + "\\matlab_code_test")

    eng = matlab.engine.start_matlab()
    output = eng.sim_test('input_args')
    print('Matlab output: ', output)

    print('Done')


def run_m113():
    print('Running M113 Simulation\n')

    cwd = getcwd()
    chdir(cwd + "\\..\\M113_tests")

    eng = matlab.engine.start_matlab()
    eng.M113_MainFile(nargout = 0)

    print('Done')

def run_async(tabWidget):
    cwd = getcwd()
    chdir(cwd + "\\matlab_code_test")

    eng = matlab.engine.start_matlab()

    import io
    out = io.StringIO()
    ret = eng.sim_test('input_args', background=True, stdout=out)
    print(out.getvalue())
    print(ret)
    tabWidget.setDisabled(False)

def run_exec(vehicle):
    import subprocess
    
    cmd = 'matlab_executables\\test1\\sim_test.exe'
    subprocess.call(cmd)

    # subp = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    # (output, err) = subp.communicate()
    # subp_status = subp.wait()


if __name__ == "__main__":
    run_exec()
