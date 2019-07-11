'''
evaluation_measures -- Additional metrics used in learn_model not implemented in
sklearn.


@author:     Jose' de Souza
        
@copyright:  2012. All rights reserved.
        
@license:    Apache License 2.0

@contact:    jose.camargo.souza@gmail.com
@deffield    updated: Updated
'''
from sklearn.metrics import mean_squared_error
from sklearn.metrics.pairwise import manhattan_distances
import numpy as np

def root_mean_squared_error(x, y):
    mse = mean_squared_error(x, y)
    rmse = np.sqrt(mse)
    return rmse



if __name__ == '__main__':
    pass
