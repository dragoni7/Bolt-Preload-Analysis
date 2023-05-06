__author__      = "Samuel Gibson"

import customtkinter as ctk
from controller.model_controller import ModelController
from view.main_tabview import MainTabview
from view.plot_frame import PlotFrame
from config import APP_PATH
from PIL import Image

# main application, imports frames to create the user interface
class App(ctk.CTk):

    def __init__(self):
        
        super().__init__()

        self.controller = ModelController.get_instance() # get controller instance
        # styling
        self.console_font = ctk.CTkFont(family="Consolas", size=16)
        ctk.set_default_color_theme("dark-blue")
        self.configure(fg_color="#222224")
        # configure window
        self.title("Thor Preload Predictor")

        # configure grid layout (6x6)
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # configure and draw initial plot
        self.controller.update_model("none", "NA", "NA", "NA", "NA") # create the graph with these initial parameters
        self.plotframe = PlotFrame(self, border_width=10)
        self.plotframe.configure(border_color="#003060")
        self.plotframe.grid(row=0, column=1, rowspan=4, padx=5, pady=5, sticky="nsew")
        
        # image header
        self.logo = ctk.CTkImage(light_image=Image.open(APP_PATH + "\\resources\\data\\image\\logo.png"), size=(146, 52))
        self.header = ctk.CTkLabel(self, text="     Preload Predictor v 0.0.1", image=self.logo, compound="left", fg_color="#9599a1", anchor="w")
        self.header.grid(row=0, column=0, padx=5, pady=2, sticky="new")

        # add tab view
        self.tab_view = MainTabview(self, border_width=10)
        self.tab_view.configure(border_color="#003060")
        self.tab_view.grid(row=0, column=0, rowspan=6, pady=50, sticky="nsew")

        # configure empty text box
        self.textbox = ctk.CTkTextbox(self, border_width=10, wrap="word")
        self.textbox.configure(state="disabled", border_color="#003060", fg_color="black", font=self.console_font)
        self.textbox.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")