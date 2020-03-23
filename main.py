import sys

from gui.testUI import run_simulation_ui


class App(object):
    def __init__(self):
        run_simulation_ui()

        print('Now what?')


if __name__ == "__main__":
    app = App()
