import customtkinter as ctk
from controller.model_controller import ModelController
import model.experimental_parameters as model_parameters
import view.plot_update_helper as plot
from view.widgets.spin_box import FloatSpinbox
import tkinter
from datetime import datetime
import math
import re

class OptionFrame(ctk.CTkFrame):
    '''Frame to hold options'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args,  **kwargs)

        self.grid_columnconfigure((0, 3), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # styling
        self.header_font = ctk.CTkFont(size=22, weight="bold", family="Proxima Nova")
        self.subheader_font = ctk.CTkFont(size=14, weight="bold", family="Monserrat")
        self.text_font = ctk.CTkFont(size=13, family="Monserrat")

        # header
        self.header = ctk.CTkLabel(self, text="Options:", font=self.header_font)
        self.header.grid(row=0, column=0, pady=10, padx=90)

        self.option_label = ctk.CTkLabel(self, text="Text Scaling", font=self.subheader_font)
        self.option_label.grid(row=1, column=0, pady=10, stick="nsew")
        self.value_label = ctk.CTkLabel(self, text="Value", font=self.subheader_font)
        self.value_label.grid(row=1, column=1, pady=10, stick="nsew")

        self.scaling_optionemenu = ctk.CTkOptionMenu(self, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.set("100%")
        self.scaling_optionemenu.grid(row=2, column=1, columnspan=3, pady=20)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)