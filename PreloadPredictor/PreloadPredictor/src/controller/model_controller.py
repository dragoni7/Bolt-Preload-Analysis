from model.preload_decay_model import PreloadDecayModel
import matplotlib.pyplot as plt
import numpy as np

class ModelController:
    __instance = None

    @staticmethod
    def getInstance():
        if ModelController.__instance == None:
            ModelController()
        return ModelController().__instance
    
    def __init__(self):
        if ModelController.__instance != None:
            raise Exception("Singleton Class!")
        else:
            ModelController.__instance = self
            self.__models = []
            self.__activeModel = None

    def activeModel(self):
        return self.__activeModel

    def setActive(self, label):
        for model in self.__models:
            if model.label == label:
                self.__activeModel = model
    
    def addModel(self, newModel: PreloadDecayModel):
        self.__models.append(newModel)

    def updateFig(self):
        self.__activeModel.setXValues(np.arange(10000))
        self.__activeModel.setYValues(self.__activeModel.exp_model(1, 1, 1, 1)) # TODO: get params

        fig = plt.figure(figsize=(8,8))
        plt.ylim([0,100])
        plt.axhline(y=50, color='r', linestyle='-')
        plt.plot(self.__activeModel.xValues(), self.__activeModel.yValues(),'-g', label=self.__activeModel.label())
        plt.xlabel("Time Cycle")
        plt.ylabel("% Force")
        plt.legend()

        self.__activeModel.setFig(fig)

    # TODO: params
