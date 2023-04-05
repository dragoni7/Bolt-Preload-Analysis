from creator.model_factory import ModelFactory
from controller.model_controller import ModelController

def run():

    controller = ModelController.getInstance()

    factory = ModelFactory()
    model = factory.create_model("exp2", "Thor Model", float(9.802), float(-0.099), float(96.78), float(-0.000446))
    
    controller.addModel(model)
    controller.setActive("Thor Model")