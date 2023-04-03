import numpy as np

class PreloadDecayModel(object):

    def __init__(self, label, c_A = float(1.0), c_B = float(1.0), c_C = float(1.0), c_D = float(1.0)):
        self.label = label
        self.__fig = None
        self.__x_values = [] 
        self.__y_values = []
        self.c_A = c_A
        self.c_B = c_B
        self.c_C = c_C
        self.c_D = c_D

    def label(self):
        return self.label
    
    def xValues(self):
        return self.__x_values
    
    def yValues(self):
        return self.__y_values
    
    def setXValues(self, new_x):
        if (new_x == self.__x_values):
            return
        else:
            self.__x_values = new_x

    def setYValues(self, new_y):
        if (new_y == self.__y_values):
            return
        else:
            self.__y_values = new_y

    def getFig(self):
        return self.__fig
    
    def setFig(self, new_fig):
        self.__fig = new_fig


    def exp_model(self, p_A, p_B, p_C, p_D):
        a_new = self.c_A * p_A
        b_new = self.c_B * p_B
        c_new = self.c_C * p_C
        d_new = self.c_D * p_D
        
        return (a_new*np.exp(b_new * self.__x_values)) + ((c_new)*np.exp(d_new * self.__x_values))
    
