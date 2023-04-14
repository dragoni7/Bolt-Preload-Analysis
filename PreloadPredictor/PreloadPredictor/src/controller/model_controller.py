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

    def update_model(self, p_A, p_B, p_C, p_D, cycles=10000, threshold=50):
        '''Updates a models data according to user inputs'''
        plt.close("all")

        self._active_model.x_values = np.arange(cycles)
        self._active_model.y_values = self._active_model.exp_model(p.values[p.SEALANT][p_A], p.values[p.PLATE_MATERIAL][p_B], p.values[p.PARAMETER3][p_C], p.values[p.PARAMETER4][p_D])
        cycle_prediction = (np.abs(self._active_model.y_values - threshold)).argmin()

        fig = plt.figure(figsize=(8,8), facecolor="#003060")
        plt.ylim([0,100])
        plt.plot(self._active_model.x_values, self._active_model.y_values, color='g', label=self._active_model.label)
        plt.axhline(y=threshold, color='r', linestyle='-')
        plt.plot([cycle_prediction], [threshold], 'o', color="r")
        plt.xlabel("Time Cycle", fontweight='bold')
        plt.ylabel("% Force", fontweight='bold')
        plt.legend()

        
        self._active_model.threshold_point = cycle_prediction.item()

        self._active_model.figure = (fig)

