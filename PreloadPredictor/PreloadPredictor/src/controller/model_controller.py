from model.preload_decay_model import PreloadDecayModel
import matplotlib.pyplot as plt
import model.experimental_parameters as p
import numpy as np

class ModelController:
    __instance = None

    @staticmethod
    def get_instance():
        '''Get the controller singleton instance'''
        if ModelController.__instance == None:
            ModelController()
        return ModelController.__instance
    
    def __init__(self):
        if ModelController.__instance != None:
            raise Exception("Singleton Class!")
        else:
            ModelController.__instance = self
            self._models = []
            self._active_model = None
    @property
    def active_model(self) -> PreloadDecayModel:
        '''Gets the selected model'''
        return self._active_model
    
    def select_model(self, label):
        '''Selects an active model by label'''
        for model in self._models:
            if model.label == label:
                self._active_model = model
    
    def add_model(self, new_model: PreloadDecayModel):
        '''Adds a new model to the list of models'''
        self._models.append(new_model)

    def update_model(self, p_A, p_B, p_C, p_D, p_E, cycles=10000, threshold_1=50, threshold_2=50, threshold_3=50):
        '''Updates a models data according to user inputs'''
        plt.close("all")

        self._active_model.x_values = np.arange(cycles)
        self._active_model.y_values = self._active_model.exp_model(p.values[p.SEALANT][p_A], p.values[p.PLATE_MATERIAL][p_B], p.values[p.BOLT_DIAMETER][p_C], p.values[p.FASTENER_MATERIAL][p_D], p.values[p.FASTENER_THREAD_SIZE][p_E])
        
        cycle_prediction_1 = (np.abs(self._active_model.y_values - threshold_1)).argmin()
        cycle_prediction_2 = cycle_prediction_1
        cycle_prediction_3 = cycle_prediction_1
        
        if (threshold_2 < 0):
            cycle_prediction_2 = (np.abs(self._active_model.y_values - threshold_2)).argmin()
        if (threshold_3 < 0):            
            cycle_prediction_3 = (np.abs(self._active_model.y_values - threshold_3)).argmin()

        # color by threshold
        ylower = np.ma.masked_where(self._active_model.y_values < threshold_1, self._active_model.y_values)
        yupper = np.ma.masked_where(self._active_model.y_values > threshold_1, self._active_model.y_values)
        fig, ax = plt.subplots(facecolor="#242424")
        ax.plot(self._active_model.x_values, ylower, self._active_model.x_values, yupper, label=self._active_model.label)
        plt.ylim([0,100])
        ax.grid(axis = 'x')
        ax.axhline(y=threshold_1, color='r', linestyle='dashed')
        ax.plot([cycle_prediction_1], [threshold_1], 'o', color="r")
        if (threshold_2 > 1):
            ax.axhline(y=threshold_2, color='r', linestyle='dashed')
            ax.plot([cycle_prediction_2], [threshold_2], 'o', color="r")
        if (threshold_3 > 1):
            ax.axhline(y=threshold_3, color='r', linestyle='dashed')
            ax.plot([cycle_prediction_3], [threshold_3], 'o', color="r")
            
        # axes styling
        ax.tick_params(labelcolor='#F2F2F2')
        ax.set_facecolor('#eafff5')
        # labels
        plt.xlabel("Time Cycles", fontweight='bold', color='#F2F2F2')
        plt.ylabel("% Force", fontweight='bold', color='#F2F2F2')

        self._active_model.threshold_point = cycle_prediction_1.item()
        self._active_model.figure = (fig)

