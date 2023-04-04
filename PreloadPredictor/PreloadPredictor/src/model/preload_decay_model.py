import numpy as np
from matplotlib.figure import Figure

class PreloadDecayModel():

    def __init__(self, label: str, c_A = float(1.0), c_B = float(1.0), c_C = float(1.0), c_D = float(1.0)):
        self.label = label
        self.fig = None
        self.x_values = np.arange(1)
        self.y_values = np.arange(1)
        self.c_A = c_A
        self.c_B = c_B
        self.c_C = c_C
        self.c_D = c_D

    def label(self) -> str:
        return self.label
    
    def xValues(self):
        return self.x_values
    
    def yValues(self):
        return self.y_values
    
    def setXValues(self, new_x):
        self.x_values = new_x

    def setYValues(self, new_y):
        self.y_values = new_y

    def getFig(self) -> Figure:
        return self.fig
    
    def setFig(self, new_fig):
        self.fig = new_fig


    def exp_model(self, p_A, p_B, p_C, p_D):
        a_new = self.c_A * p_A
        b_new = self.c_B * p_B
        c_new = self.c_C * p_C
        d_new = self.c_D * p_D
        
        return (a_new*np.exp(b_new * self.x_values)) + ((c_new)*np.exp(d_new * self.x_values))
    
