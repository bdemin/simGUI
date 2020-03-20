import numpy as np
import os


class Results(object):
    # Class for plotting various simulation data

    def __init__(self):
        
        self.build_data()

    def load_data(self):
        pass



    def build_data(self):

        self.data_folder = 'simulation_results//Simulation_1//'
        self.results_data = {}

        for filename in os.listdir(self.data_folder):
            if filename.endswith('.txt'):
                print('Added', filename)
                
                obj_type = filename.split('.')[0].lower()
                try:
                    self.results_data[obj_type] = np.loadtxt(self.data_folder + filename, delimiter=',')
                except:
                    print('Error: ' + filename, 'has invalid data.')

            else:
                print('Error: ' + filename, 'is not a .txt file.')


if __name__ == "__main__":
    results = Results()
