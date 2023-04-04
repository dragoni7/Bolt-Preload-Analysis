import customtkinter as ctk
from controller.model_controller import ModelController
import model.model_parameters as model_parameters
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import view.plot_view as plot
import re

class PredictionFrame(ctk.CTkFrame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args,  **kwargs)

        self.controller = ModelController.getInstance()

        self.parent = parent

        # Model header
        self.model_header = ctk.CTkLabel(self, text="Model:", font=ctk.CTkFont(size=20, weight="bold"))
        self.model_header.grid(row=0, column=0)

        # create widgets for parameter settings
        self.c_label1 = self.set_parameter_label("Parameters")
        self.c_label1.grid(row=1, column=1, padx=20, pady=10, stick="nsew")
        self.c_label2 = ctk.CTkLabel(self, text="Value", font=ctk.CTkFont(size=14, weight="bold"))
        self.c_label2.grid(row=1, column=2, padx=20, pady=10, stick="nsew")

        # sealent
        self.p1_label = self.set_parameter_label(model_parameters.SEALANT + ":")
        self.p1_label.grid(row=2, column=1)
        self.p1_options = self.set_parameter_options(model_parameters.get_values(model_parameters.SEALANT))
        self.p1_options.grid(row=2, column=2, padx=20, pady=10, sticky= "nsew")

        # plate material
        self.p2_label = self.set_parameter_label(model_parameters.PLATE_MATERIAL + ":")
        self.p2_label.grid(row=3, column=1)
        self.p2_options = self.set_parameter_options(model_parameters.get_values(model_parameters.PLATE_MATERIAL))
        self.p2_options.grid(row=3, column=2, padx=20, pady=10, sticky= "nsew")

        # parameter3
        self.p3_label = self.set_parameter_label(model_parameters.PARAMETER3 + ":")
        self.p3_label.grid(row=4, column=1)
        self.p3_options = self.set_parameter_options(model_parameters.get_values(model_parameters.PARAMETER3))
        self.p3_options.grid(row=4, column=2, padx=20, pady=10, sticky= "nsew")

        # parameter4
        self.p4_label = self.set_parameter_label(model_parameters.PARAMETER4 + ":")
        self.p4_label.grid(row=5, column=1)
        self.p4_options = self.set_parameter_options(model_parameters.get_values(model_parameters.PARAMETER4))
        self.p4_options.grid(row=5, column=2, padx=20, pady=10, sticky= "nsew")

        # time cycle
        self.cycle_header = ctk.CTkLabel(self, text="Time Cycle:", font=ctk.CTkFont(size=20, weight="bold"))
        self.cycle_header.grid(row=6, column=0)

        # entry
        self.cycle_entry = ctk.CTkEntry(master=self, placeholder_text="time cycles")
        self.cycle_entry.insert("0", "10000")
        self.cycle_entry.grid(row=7, column=1, pady=20, sticky= "nsew")

        # preload threshold
        self.cycle_header = ctk.CTkLabel(self, text="Preload Threshold:", font=ctk.CTkFont(size=20, weight="bold"))
        self.cycle_header.grid(row=8, column=0)

        # entry
        self.threshold_entry = ctk.CTkEntry(master=self, placeholder_text="preload threshold")
        self.threshold_entry.insert("0", "60")
        self.threshold_entry.grid(row=9, column=1, pady=20, sticky= "nsew")

        # run button
        self.input_model_button = ctk.CTkButton(self, text="Run Prediction", command=self.run_prediction_button_event,fg_color="green", hover_color="dark green")
        self.input_model_button.grid(row=10, column=1, pady=20, sticky= "nsew")


    def slider_event(self, value):
        print(value)

    def set_parameter_label(self, name):
        return ctk.CTkLabel(self, text= name, font=ctk.CTkFont(size=14, weight="bold"))
    
    def set_parameter_options(self, values):
        return ctk.CTkOptionMenu(self, values=values)
    
    def draw_plot(self, fig):
        canvas = FigureCanvasTkAgg(ModelController.getInstance().activeModel().getFig(), master=self.parent)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=2, rowspan=4, columnspan=4, padx=15, pady=15, sticky="nsew")
    
    # handle events
    def run_prediction_button_event(self):
        cycle_entry_str = self.cycle_entry.get()
        threshold_entry_str = self.threshold_entry.get()

        if (len(cycle_entry_str) < 7 and len(cycle_entry_str) > 0):
            try:
                cycles = int(re.search(r'\d+', cycle_entry_str).group())
            except:
                self.parent.textbox.configure(state="normal", text_color="red", border_color="red")
                self.parent.textbox.delete("0.0", "end")
                self.parent.textbox.insert("0.0", "Non integer input detected for cycles\n")
                self.parent.textbox.configure(state="disabled")
                return
        else:
            self.parent.textbox.configure(state="normal", text_color="red", border_color="red")
            self.parent.textbox.delete("0.0", "end")
            self.parent.textbox.insert("0.0", "Invalid cycles input length\n")
            self.parent.textbox.configure(state="disabled")
            return            

        self.controller.updateModel(self.p1_options._current_value,
                                     self.p2_options._current_value,
                                     self.p3_options._current_value, 
                                     self.p4_options._current_value,
                                     cycles)
        self.parent.textbox.configure(state="normal", text_color="orange", border_color="grey")
        self.parent.textbox.delete("0.0", "end")
        self.parent.textbox.insert("0.0", "Preload decay threshold met at:\nWith:\n" +  cycle_entry_str + " cycles\n" + "threshold of " + threshold_entry_str + "%\n")
        self.parent.textbox.configure(state="disabled")
        
        plot.draw_plot(self.parent)
        