import customtkinter as ctk
from controller.model_controller import ModelController
import model.experimental_parameters as model_parameters
import view.plot_update_helper as plot
from view.widgets.spin_box import FloatSpinbox
import tkinter
from datetime import datetime
import math
import re

class ModelsFrame(ctk.CTkFrame):
    '''Frame to hold models display'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args,  **kwargs)

        self.grid_columnconfigure((0, 3), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.controller = ModelController.get_instance() # model controller instance

        # styling
        self.header_font = ctk.CTkFont(size=22, weight="bold", family="Proxima Nova")
        self.subheader_font = ctk.CTkFont(size=14, weight="bold", family="Monserrat")
        self.text_font = ctk.CTkFont(size=13, family="Monserrat")

        # header
        self.header = ctk.CTkLabel(self, text="Model Info:", font=self.header_font)
        self.header.grid(row=0, column=0, pady=10, padx=80)

        self.option_label_1 = ctk.CTkLabel(self, text="Name:", font=self.subheader_font)
        self.option_label_1.grid(row=1, column=0, pady=10, stick="nsew")
        self.value_label_1 = ctk.CTkLabel(self, text=self.controller.active_model.label, font=self.text_font)
        self.value_label_1.grid(row=1, column=1, pady=10, stick="nsew")

        self.option_label_2 = ctk.CTkLabel(self, text="Type:", font=self.subheader_font)
        self.option_label_2.grid(row=2, column=0, pady=10, stick="nsew")
        self.value_label_2 = ctk.CTkLabel(self, text="exp2", font=self.text_font)
        self.value_label_2.grid(row=2, column=1, pady=10, stick="nsew")

        self.option_label_3 = ctk.CTkLabel(self, text="Coefficient A:", font=self.subheader_font)
        self.option_label_3.grid(row=3, column=0, pady=10, stick="nsew")
        self.value_label_3 = ctk.CTkLabel(self, text=self.controller.active_model.c_A, font=self.text_font)
        self.value_label_3.grid(row=3, column=1, pady=10, stick="nsew")

        self.option_label_4 = ctk.CTkLabel(self, text="Coefficient B:", font=self.subheader_font)
        self.option_label_4.grid(row=4, column=0, pady=10, stick="nsew")
        self.value_label_4 = ctk.CTkLabel(self, text=self.controller.active_model.c_B, font=self.text_font)
        self.value_label_4.grid(row=4, column=1, pady=10, stick="nsew")

        self.option_label_5 = ctk.CTkLabel(self, text="Coefficient C:", font=self.subheader_font)
        self.option_label_5.grid(row=5, column=0, pady=10, stick="nsew")
        self.value_label_5 = ctk.CTkLabel(self, text=self.controller.active_model.c_C, font=self.text_font)
        self.value_label_5.grid(row=5, column=1, pady=10, stick="nsew")

        self.option_label_6 = ctk.CTkLabel(self, text="Coefficient D:", font=self.subheader_font)
        self.option_label_6.grid(row=6, column=0, pady=10, stick="nsew")
        self.value_label_6 = ctk.CTkLabel(self, text=self.controller.active_model.c_D, font=self.text_font)
        self.value_label_6.grid(row=6, column=1, pady=10, stick="nsew")