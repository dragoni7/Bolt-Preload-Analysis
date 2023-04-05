from model.preload_decay_model import PreloadDecayModel
import matplotlib.pyplot as plt
import model.model_parameters as p
import numpy as np

class ModelController:
    __instance = None

    @staticmethod
    def getInstance():
        if ModelController.__instance == None:
            ModelController()
        return ModelController.__instance
    
    def __init__(self):
        if ModelController.__instance != None:
            raise Exception("Singleton Class!")
        else:
            ModelController.__instance = self
            self.models = []
            self.active_model = None

    def activeModel(self) -> PreloadDecayModel:
        return self.active_model

    def setActive(self, label):
        for model in self.models:
            if model.label == label:
                self.active_model = model
    
    def addModel(self, newModel: PreloadDecayModel):
        self.models.append(newModel)

    def updateModel(self, p_A, p_B, p_C, p_D, cycles=10000, threshold=50):
        plt.close("all")

        self.active_model.setXValues(np.arange(cycles))
        self.active_model.setYValues(self.active_model.exp_model(p.values[p.SEALANT][p_A], p.values[p.PLATE_MATERIAL][p_B], p.values[p.PARAMETER3][p_C], p.values[p.PARAMETER4][p_D]))
        cycle_prediction = (np.abs(self.active_model.yValues() - threshold)).argmin()

        fig = plt.figure(figsize=(8,8))
        plt.ylim([0,100])
        plt.plot(self.active_model.xValues(), self.active_model.yValues(), color='g', label=self.active_model.label)
        plt.axhline(y=threshold, color='r', linestyle='-')
        plt.plot([cycle_prediction], [threshold], 'o', color="r")
        plt.xlabel("Time Cycle")
        plt.ylabel("% Force")
        plt.legend()

        
        self.active_model.set_threshold_point(cycle_prediction.item())

        self.active_model.setFig(fig)

