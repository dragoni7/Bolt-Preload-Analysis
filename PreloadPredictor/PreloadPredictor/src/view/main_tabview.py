import customtkinter as ctk
from view.prediction_frame import PredictionFrame
from view.option_frame import OptionFrame
from view.models_frame import ModelsFrame
from view.widgets.spin_box import FloatSpinbox

class MainTabview(ctk.CTkTabview):
    '''Tab view containing application frames'''

    def __init__(self, master, **kwargs):

        super().__init__(master, **kwargs)

        self.add("Prediction")
        self.add("Model")
        self.add("Option")

        self.tab("Prediction").configure(fg_color="#242424")
        self.tab("Model").configure(fg_color="#242424")
        self.tab("Option").configure(fg_color="#242424")

        self.prediction_frame = PredictionFrame(master, master=self.tab("Prediction"), fg_color="#242424")
        self.prediction_frame.grid(row=0, column=0, sticky="nsew")

        self.models_frame = ModelsFrame(master=self.tab("Model"), fg_color="#242424")
        self.models_frame.grid(row=0, column=0, sticky="nsew")

        self.options_frame = OptionFrame(master=self.tab("Option"), fg_color="#242424")
        self.options_frame.grid(row=0, column=0, sticky="nsew")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)    