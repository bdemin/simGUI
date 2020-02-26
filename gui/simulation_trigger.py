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

def progress(progressBar, tabWidget):
    for i in range(1, 101):
        progressBar.setValue(i)
    tabWidget.setDisabled(False)

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

if __name__ == "__main__":
    run()
