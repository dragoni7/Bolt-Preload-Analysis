from model.preload_decay_model import PreloadDecayModel
import matplotlib.pyplot as plt
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

    def updateFig(self):
        self.active_model.setXValues(np.arange(10000))
        self.active_model.setYValues(self.active_model.exp_model(1, 1, 1, 1)) # TODO: get params

        fig = plt.figure(figsize=(8,8))
        plt.ylim([0,100])
        plt.axhline(y=50, color='r', linestyle='-')
        plt.plot(self.active_model.xValues(), self.active_model.yValues(),'-g', label=self.active_model.label())
        plt.xlabel("Time Cycle")
        plt.ylabel("% Force")
        plt.legend()

        self.active_model.setFig(fig)

    # TODO: params
