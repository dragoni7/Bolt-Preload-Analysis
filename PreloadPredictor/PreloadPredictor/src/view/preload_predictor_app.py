"""__preloadpredictor__.py: Presentation layer of the application. Utilizes customtkinter."""

__author__      = "Samuel Gibson"

import customtkinter as ctk
from controller.model_controller import ModelController
import model.thor_model as model
from view.main_tabview import MainTabview
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import view.plot_view as plot

# main application
class App(ctk.CTk):

    def __init__(self):
        
        super().__init__()

        self.controller = ModelController.getInstance()
        self.console_font = ctk.CTkFont(family="Consolas", size=16)

        # configure window
        self.title("Thor Preload Predictor")
        self.geometry(f"{1920}x{1080}")

        # configure grid layout (6x6)
        self.grid_columnconfigure((0, 5), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # configure and draw initial plot
        self.controller.updateModel("v1", "aluminum", "v1", "v1")
        plot.draw_plot(self)

        # configure empty text box
        self.textbox = ctk.CTkTextbox(self, border_width=10, wrap="word")
        self.textbox.configure(state="disabled", border_color="grey", fg_color="black", font=self.console_font)
        self.textbox.grid(row=4, column=2, rowspan=5, columnspan=4, padx=15, pady=15,sticky="new")

        self.tab_view = MainTabview(self, border_width=10)
        self.tab_view.grid(row=0, column=0, rowspan=6, columnspan=2, padx=10, pady=5, sticky="nsew")
    
    def draw_plot(self):
        self.canvas = FigureCanvasTkAgg(self.controller.activeModel().getFig(), master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=2, rowspan=4, columnspan=4, padx=15, pady=15, sticky="nsew")