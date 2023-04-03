import customtkinter as ctk
from PIL import Image
from view.prediction_frame import PredictionFrame
from view.option_frame import OptionFrame
from view.models_frame import ModelsFrame

class MainTabview(ctk.CTkTabview):

    def __init__(self, master, **kwargs):

        super().__init__(master, **kwargs)

        self.add("Prediction")
        self.add("Models")
        self.add("Options")

        self.prediction_frame = PredictionFrame(master, master=self.tab("Prediction"))
        self.prediction_frame.grid(row=0, column=0)

        self.models_frame = ModelsFrame(master=self.tab("Models"))
        self.models_frame.grid(row=0, column=0)

        self.options_frame = OptionFrame(master=self.tab("Options"))
        self.options_frame.grid(row=0, column=0)