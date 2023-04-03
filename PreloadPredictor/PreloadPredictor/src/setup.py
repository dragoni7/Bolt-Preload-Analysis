from creator.model_factory import ModelFactory
from controller.model_controller import ModelController
import model.model_parameters as p
import numpy as np
import matplotlib.pyplot as plt

def run():

    controller = ModelController.getInstance()

    factory = ModelFactory()
    model = factory.create_model("exp2", "Thor Model", float(9.802), float(-0.099), float(96.78), float(-0.000446))

    model.setXValues(np.arange(10000))
    model.setYValues(model.exp_model(p.values[p.SEALANT]["v1"], p.values[p.PLATE_MATERIAL]["aluminum"], p.values[p.PARAMETER3]["v1"], p.values[p.PARAMETER4]["v1"]))

    fig = plt.figure(figsize=(1, 1))
    plt.ylim([0,100])
    plt.axhline(y=50, color='r', linestyle='-')
    plt.plot(model.xValues(), model.yValues(),'-g', label=model.label)
    plt.xlabel("Time Cycle")
    plt.ylabel("% Force")
    plt.legend()

    model.setFig(fig)

    controller.addModel(model)
    controller.setActive("Thor Model")
