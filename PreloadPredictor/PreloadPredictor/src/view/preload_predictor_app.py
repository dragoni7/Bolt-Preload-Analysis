"""__preloadpredictor__.py: Presentation layer of the application. Utilizes customtkinter."""

__author__      = "Samuel Gibson"

import customtkinter as ctk
from controller.model_controller import ModelController
from view.main_tabview import MainTabview
import view.plot_view as plot

# main application
class App(ctk.CTk):

    def __init__(self):
        
        super().__init__()

        self.controller = ModelController.get_instance()
        self.console_font = ctk.CTkFont(family="Consolas", size=16)

        # configure window
        self.title("Thor Preload Predictor")
        self.geometry(f"{1920}x{1080}")

        # configure grid layout (6x6)
        self.grid_columnconfigure((0, 5), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # configure and draw initial plot
        self.controller.update_model("v1", "aluminum", "v1", "v1")
        plot.draw_plot(self)

        # configure empty text box
        self.textbox = ctk.CTkTextbox(self, border_width=10, wrap="word")
        self.textbox.configure(state="disabled", border_color="#0E86D4", fg_color="black", font=self.console_font)
        self.textbox.grid(row=4, column=2, rowspan=5, columnspan=4, padx=15, pady=15,sticky="new")
        
        # add tab view
        self.tab_view = MainTabview(self, border_width=10)
        self.tab_view.configure(border_color="#0E86D4", fg_color="#003060")
        self.tab_view.grid(row=0, column=0, rowspan=6, columnspan=2, padx=10, pady=5, sticky="nsew")