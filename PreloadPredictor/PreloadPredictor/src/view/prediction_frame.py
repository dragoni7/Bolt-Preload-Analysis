import customtkinter as ctk
from controller.model_controller import ModelController
import model.experimental_parameters as model_parameters
import view.plot_view as plot
import re

class PredictionFrame(ctk.CTkFrame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args,  **kwargs)

        self.controller = ModelController.get_instance()
        self.header_font = ctk.CTkFont(size=20, weight="bold", family="Proxima Nova")
        self.sub_header_font = ctk.CTkFont(size=14, weight="bold", family="Monserrat")
        self.parent = parent

        # Model header
        self.model_header = ctk.CTkLabel(self, text="Model:", font=self.header_font)
        self.model_header.grid(row=0, column=0)

        # Parameter and values header
        self.c_label1 = self.set_parameter_label("Parameters")
        self.c_label1.grid(row=1, column=1, padx=20, pady=10, stick="nsew")
        self.c_label2 = ctk.CTkLabel(self, text="Value", font=self.sub_header_font)
        self.c_label2.grid(row=1, column=2, padx=20, pady=10, stick="nsew")

        # Create a widget and label for each experimental parameter:
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
        self.cycle_header = ctk.CTkLabel(self, text="Time Cycle:", font=self.header_font)
        self.cycle_header.grid(row=6, column=0)

        # entry
        self.cycle_entry = ctk.CTkEntry(master=self, placeholder_text="time cycles")
        self.cycle_entry.insert("0", "10000")
        self.cycle_entry.grid(row=7, column=1, pady=20, sticky= "nsew")

        # preload threshold
        self.cycle_header = ctk.CTkLabel(self, text="Preload Threshold:", font=self.header_font)
        self.cycle_header.grid(row=8, column=0)

        # entry
        self.threshold_entry = ctk.CTkEntry(master=self, placeholder_text="preload threshold")
        self.threshold_entry.insert("0", "50")
        self.threshold_entry.grid(row=9, column=1, pady=20, sticky= "nsew")

        # run button
        self.input_model_button = ctk.CTkButton(self, text="Run Prediction", command=self.run_prediction_button_event,fg_color="green", hover_color="dark green")
        self.input_model_button.grid(row=10, column=1, pady=20, sticky= "nsew")

    def set_parameter_label(self, name):
        '''Configures a label widget'''
        return ctk.CTkLabel(self, text= name, font=self.sub_header_font)
    
    def set_parameter_options(self, values):
        '''Configures a menu with parameter values'''
        return ctk.CTkOptionMenu(self, values=values)
    
    # handle events
    def run_prediction_button_event(self):
        cycle_entry_str = self.cycle_entry.get()
        threshold_entry_str = self.threshold_entry.get()

        # check cycle input
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
        
        # check threshold input
        try:
                threshold = int(re.search(r'\d+', threshold_entry_str).group())
        except:
                self.parent.textbox.configure(state="normal", text_color="red", border_color="red")
                self.parent.textbox.delete("0.0", "end")
                self.parent.textbox.insert("0.0", "Non integer input detected for threshold\n")
                self.parent.textbox.configure(state="disabled")
                return
        
        if (threshold < 1 or threshold > 100):
            self.parent.textbox.configure(state="normal", text_color="red", border_color="red")
            self.parent.textbox.delete("0.0", "end")
            self.parent.textbox.insert("0.0", "Invalid threshold input\n")
            self.parent.textbox.configure(state="disabled")
            return

        self.controller.update_model(self.p1_options._current_value,
                                     self.p2_options._current_value,
                                     self.p3_options._current_value, 
                                     self.p4_options._current_value,
                                     cycles,
                                     threshold)
        
        self.parent.textbox.configure(state="normal", text_color="orange", border_color="grey")
        self.parent.textbox.delete("0.0", "end")
        self.parent.textbox.insert("0.0", "Preload decay threshold met at: " + str(self.controller.active_model.threshold_point) + " cycles\nConfig:\n" +  cycle_entry_str + " cycles\n" + "threshold of " + threshold_entry_str + "%\n")
        self.parent.textbox.configure(state="disabled")
        
        plot.draw_plot(self.parent)
        