"""__preloadpredictor__.py: Presentation layer of the application. Utilizes customtkinter."""

__author__      = "Samuel Gibson"

import customtkinter as ctk
import tkinter
from controller.model_controller import ModelController
from view.main_tabview import MainTabview
from view.plot_frame import PlotFrame
from config import APP_PATH
from PIL import Image

# main application
class App(ctk.CTk):

    def __init__(self):
        
        super().__init__()

        self.controller = ModelController.get_instance()
        self.console_font = ctk.CTkFont(family="Consolas", size=16)
        self.configure(fg_color="#003060")

        # configure window
        self.title("Thor Preload Predictor")
        self.geometry(f"{1920}x{1080}")

        # configure grid layout (6x6)
        self.grid_columnconfigure((0, 5), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # configure and draw initial plot
        self.controller.update_model("BMS 5-45", "aluminum", "v1", "steel", "1/4in")
        self.plotframe = PlotFrame(self, border_width=10)
        self.plotframe.configure(border_color="#0E86D4", fg_color="#003060")
        self.plotframe.grid(row=0, column=2, rowspan=4, columnspan=4, padx=15, pady=15, sticky="nsew")

        # add tab view
        self.tab_view = MainTabview(self, border_width=10)
        self.tab_view.configure(border_color="#0E86D4", fg_color="#242424")
        self.tab_view.grid(row=1, column=0, rowspan=4, columnspan=2, padx=10, pady=5, sticky="nsew")

        # configure empty text box
        self.textbox = ctk.CTkTextbox(self, border_width=10, wrap="word")
        self.textbox.configure(state="disabled", border_color="#0E86D4", fg_color="black", font=self.console_font)
        self.textbox.grid(row=4, column=2, rowspan=5, columnspan=4, padx=15, pady=15,sticky="new")

        # image header
        self.logo = ctk.CTkImage(light_image=Image.open(APP_PATH + "\\resources\\data\\image\\logo.png"),
                                  size=(146, 52))

        self.logo_button = ctk.CTkButton(self, image=self.logo, text=" Preload Predictor  v 0.0.1", fg_color="#B3B3B3", hover=False, anchor="w", compound="left")
        self.logo_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")