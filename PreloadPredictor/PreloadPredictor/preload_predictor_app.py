"""__preloadpredictor__.py: Presentation layer of the application. Utilizes customtkinter."""

__author__      = "Samuel Gibson"

import customtkinter as ctk
import preload_predictor_plotting as plotting
import thor_model as model
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# main application
class App(ctk.CTk):
    def __init__(self):
        
        super().__init__()

        # configure window
        self.title("Preload Predictor")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x11)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 5), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
        
        # configure and draw empty plot
        self.draw_plot(plotting.reset_plot())

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=10, columnspan=2, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Model Configuration", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky= "nsew")

        # create widgets for coefficient settings
        self.c_label1 = self.set_parameter_label("Coefficient")
        self.c_label1.grid(row=1, column=0, padx=20, pady=10, stick="nsew")
        self.c_label2 = ctk.CTkLabel(self.sidebar_frame, text="Value", font=ctk.CTkFont(size=14, weight="bold"))
        self.c_label2.grid(row=1, column=1, padx=20, pady=10, stick="nsew")

        #sealent
        self.p1_label = self.set_parameter_label(model._SEALANT)
        self.p1_label.grid(row=2, column=0)
        self.p1_options = self.set_parameter_options(model.get_values(model._SEALANT))
        self.p1_options.grid(row=2, column=1, padx=20, pady=20, sticky= "nsew")

        #plate material
        self.p2_label = self.set_parameter_label(model._PLATE_MATERIAL)
        self.p2_label.grid(row=3, column=0)
        self.p2_options = self.set_parameter_options(model.get_values(model._PLATE_MATERIAL))
        self.p2_options.grid(row=3, column=1, padx=20, pady=20, sticky= "nsew")

        #parameter3
        self.p3_label = self.set_parameter_label(model._PARAMETER3)
        self.p3_label.grid(row=4, column=0)
        self.p3_options = self.set_parameter_options(model.get_values(model._PARAMETER3))
        self.p3_options.grid(row=4, column=1, padx=20, pady=20, sticky= "nsew")

        #parameter4
        self.p4_label = self.set_parameter_label(model._PARAMETER4)
        self.p4_label.grid(row=5, column=0)
        self.p4_options = self.set_parameter_options(model.get_values(model._PARAMETER4))
        self.p4_options.grid(row=5, column=1, padx=20, pady=20, sticky= "nsew")

        # run button
        self.input_model_button = ctk.CTkButton(self.sidebar_frame, text="Run Prediction", command=self.run_prediction_button_event,fg_color="orange", hover_color="dark orange")
        self.input_model_button.grid(row=6, column=1, pady=20, sticky= "nsew")

    def set_parameter_label(self, name):
        return ctk.CTkLabel(self.sidebar_frame, text= name, font=ctk.CTkFont(size=14, weight="bold"))
    
    def set_parameter_options(self, values):
        return ctk.CTkOptionMenu(self.sidebar_frame, values=values)
    
    def draw_plot(self, fig):
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=4, rowspan=10, columnspan=5, sticky= "nsew")
    
    # handle events
    def run_prediction_button_event(self):
        self.draw_plot(plotting.plot(self.p1_options._current_value, 
                                     self.p2_options._current_value, 
                                     self.p3_options._current_value, 
                                     self.p4_options._current_value))