import customtkinter as ctk
import controller.preload_predictor_plotting as plotting
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import model.thor_model as model

class PredictionFrame(ctk.CTkFrame):

    def __init__(self, parent, *args, header_name = "Model Configuration", **kwargs):
        super().__init__(*args,  **kwargs)

        self.parent = parent

        self.header_name = header_name

        self.header = ctk.CTkLabel(self, text=self.header_name, font=ctk.CTkFont(size=20, weight="bold"))
        self.header.grid(row=0, column=0)

        # create widgets for coefficient settings
        self.c_label1 = self.set_parameter_label("Parameters")
        self.c_label1.grid(row=1, column=0, padx=20, pady=10, stick="nsew")
        self.c_label2 = ctk.CTkLabel(self, text="Value", font=ctk.CTkFont(size=14, weight="bold"))
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
        self.input_model_button = ctk.CTkButton(self, text="Run Prediction", command=self.run_prediction_button_event,fg_color="green", hover_color="dark green")
        self.input_model_button.grid(row=6, column=1, pady=20, sticky= "nsew")
        
        # reset button
        self.input_model_button = ctk.CTkButton(self, text="Reset", command=self.run_reset_button_event,fg_color="orange", hover_color="dark orange")
        self.input_model_button.grid(row=6, column=0, pady=20, padx=10, sticky= "nsew")

    def set_parameter_label(self, name):
        return ctk.CTkLabel(self, text= name, font=ctk.CTkFont(size=14, weight="bold"))
    
    def set_parameter_options(self, values):
        return ctk.CTkOptionMenu(self, values=values)
    
    def draw_plot(self, fig):
        canvas = FigureCanvasTkAgg(fig, master=self.parent)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=2, rowspan=4, columnspan=4, padx=15, pady=15, sticky="nsew")
    
    # handle events
    def run_prediction_button_event(self):
        self.draw_plot(plotting.plot(self.p1_options._current_value, 
                                     self.p2_options._current_value, 
                                     self.p3_options._current_value, 
                                     self.p4_options._current_value))
        
    def run_reset_button_event(self):
        self.draw_plot(plotting.reset_plot())

        