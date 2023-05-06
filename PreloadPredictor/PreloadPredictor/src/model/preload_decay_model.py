import numpy as np
from matplotlib.figure import Figure

class PreloadDecayModel():
    '''Preload decay model object. Stores relevant data and equation of curve.'''

    def __init__(self, label: str, c_A = float(1.0), c_B = float(1.0), c_C = float(1.0), c_D = float(1.0)):
        self._label = label # model label
        self._threshold_point = [None, None, None] # stores up to 3 threshold points of interest
        self._figure = None # plot of the model curve
        self._x_values = np.arange(1.0, dtype=np.float64) # x values
        self._y_values = np.arange(1.0, dtype=np.float64) # y values
        # coefficients for exp2 model
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

    def clear_threshold_points(self):
        '''empties the threshold points list'''
        self._threshold_point.clear()
        self._threshold_point = [None, None, None]

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


    def exp_model(self, sealant_param, plate_material_param, bolt_type_param, fastener_mat_param, fastener_t_size_param):
        '''Calculates the y values of the exp2 model, applying parameters to each coefficient'''

        # repeated this modification for each parmeter
        a_new = self.c_A * sealant_param[0]
        b_new = self.c_B + sealant_param[1]
        c_new = self.c_C * sealant_param[2]
        d_new = self.c_D + sealant_param[3]
        
        return ((a_new)*np.exp(b_new * self.x_values)) + ((c_new)*np.exp(d_new * self.x_values))
    
