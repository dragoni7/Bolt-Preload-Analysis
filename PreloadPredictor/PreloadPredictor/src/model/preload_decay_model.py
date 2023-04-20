import numpy as np
from matplotlib.figure import Figure

class PreloadDecayModel():

    def __init__(self, label: str, c_A = float(1.0), c_B = float(1.0), c_C = float(1.0), c_D = float(1.0)):
        self._label = label
        self._threshold_point = [None, None, None]
        self._figure = None
        self._x_values = np.arange(1)
        self._y_values = np.arange(1)
        self.c_A = c_A
        self.c_B = c_B
        self.c_C = c_C
        self.c_D = c_D
        
    def get_threshold_point(self, i):
        '''Get the threshold points'''
        return self._threshold_point[i]
    
    def insert_threshold_point(self, value, i):
        '''Set the threshold points'''
        self._threshold_point[i] = value

    @property
    def label(self) -> str:
        '''Get model label'''
        return self._label
    
    @label.setter
    def label(self, value):
        '''Set model label'''
        self._label = value

    @property
    def x_values(self):
        '''Get the x values'''
        return self._x_values
    
    @x_values.setter
    def x_values(self, value):
        '''Set the x values'''
        self._x_values = value

    @property
    def y_values(self):
        '''Get the y values'''
        return self._y_values
    
    @y_values.setter
    def y_values(self, value):
        '''Set the y values'''
        self._y_values = value

    @property
    def figure(self) -> Figure:
        '''Get the model figure'''
        return self._figure
    
    @figure.setter
    def figure(self, value):
        '''Set the model figure'''
        self._figure = value


    def exp_model(self, p_A, p_B, p_C, p_D, p_E):
        '''Calculates the y values of the exp2 model, applying parameters to coefficients'''
        a_new = self.c_A * p_A
        b_new = self.c_B * p_B
        c_new = self.c_C * p_C
        d_new = self.c_D * p_D
        
        return (a_new*np.exp(b_new * self.x_values)) + ((c_new)*np.exp(d_new * self.x_values)) * p_E
    
