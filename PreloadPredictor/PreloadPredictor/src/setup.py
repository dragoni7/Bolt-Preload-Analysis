from creator.model_factory import ModelFactory
from controller.model_controller import ModelController

def run():

    controller = ModelController.get_instance()

    factory = ModelFactory()
    # create our model and add it to the model controller      a                b             c                 d
    #model = factory.create_model("exp2", "Thor Model", float(5.811), float(-0.02105), float(88.14), float(-2.003e-05)) # from base line noseal .250 aluminum
    model = factory.create_model("exp2", "Thor Model", float(0.8541), float(-0.007126), float(93.78), float(-1.385e-06)) # from base line noseal .250 aluminum
    controller.add_model(model)
    controller.select_model("Thor Model") # set out model as the selected one