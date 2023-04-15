import customtkinter as ctk
from controller.model_controller import ModelController
import model.experimental_parameters as model_parameters
import view.plot_update_helper as plot
import tkinter
from datetime import datetime
import re

class PredictionFrame(ctk.CTkFrame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args,  **kwargs)

        self.controller = ModelController.get_instance()
        self.header_font = ctk.CTkFont(size=22, weight="bold", family="Proxima Nova")
        self.subheader_font = ctk.CTkFont(size=14, weight="bold", family="Monserrat")
        self.text_font = ctk.CTkFont(size=13, family="Monserrat")
        self.parent = parent
        self.t2_enabled = tkinter.StringVar(self, "on")
        self.t3_enabled = tkinter.StringVar(self, "on")

        # Model header
        self.model_header = ctk.CTkLabel(self, text="Model:", font=self.header_font)
        self.model_header.grid(row=0, column=0)

        # Parameter and values header
        self.c_label1 = ctk.CTkLabel(self, text="Parameter", font=self.subheader_font)
        self.c_label1.grid(row=1, column=0, pady=10, stick="nsew")
        self.c_label2 = ctk.CTkLabel(self, text="Value", font=self.subheader_font)
        self.c_label2.grid(row=1, column=1, pady=10, stick="nsew")

        # Create a widget and label for each experimental parameter:
        # sealant
        self.p1_label = self.set_parameter_label(model_parameters.SEALANT + ":")
        self.p1_label.grid(row=2, column=0)
        self.p1_options = self.set_parameter_options(model_parameters.get_values(model_parameters.SEALANT))
        self.p1_options.grid(row=2, column=1, padx=20, pady=5, sticky= "nsew")

        # plate material
        self.p2_label = self.set_parameter_label(model_parameters.PLATE_MATERIAL + ":")
        self.p2_label.grid(row=3, column=0)
        self.p2_options = self.set_parameter_options(model_parameters.get_values(model_parameters.PLATE_MATERIAL))
        self.p2_options.grid(row=3, column=1, padx=20, pady=5, sticky= "nsew")

        # parameter3
        self.p3_label = self.set_parameter_label(model_parameters.BOLT_DIAMETER + ":")
        self.p3_label.grid(row=4, column=0)
        self.p3_options = self.set_parameter_options(model_parameters.get_values(model_parameters.BOLT_DIAMETER))
        self.p3_options.grid(row=4, column=1, padx=20, pady=5, sticky= "nsew")

        # parameter4
        self.p4_label = self.set_parameter_label(model_parameters.FASTENER_MATERIAL + ":")
        self.p4_label.grid(row=5, column=0)
        self.p4_options = self.set_parameter_options(model_parameters.get_values(model_parameters.FASTENER_MATERIAL))
        self.p4_options.grid(row=5, column=1, padx=20, pady=5, sticky= "nsew")

        # parameter4
        self.p5_label = self.set_parameter_label(model_parameters.FASTENER_THREAD_SIZE + ":")
        self.p5_label.grid(row=6, column=0)
        self.p5_options = self.set_parameter_options(model_parameters.get_values(model_parameters.FASTENER_THREAD_SIZE))
        self.p5_options.grid(row=6, column=1, padx=20, pady=5, sticky= "nsew")

        # time cycle
        self.cycle_header = ctk.CTkLabel(self, text="Time Cycle:", font=self.header_font)
        self.cycle_header.grid(row=7, column=0, pady=20)
        self.displayed_cycles_header = ctk.CTkLabel(self, text="Cycles to Display:", font=self.text_font)
        self.displayed_cycles_header.grid(row=8, column=0)
        # time cycle entry
        self.cycle_entry = ctk.CTkEntry(master=self, placeholder_text="time cycles", width=20)
        self.cycle_entry.insert("0", "10000")
        self.cycle_entry.grid(row=8, column=1, pady=5, sticky= "nsew")

        # preload threshold
        self.cycle_header = ctk.CTkLabel(self, text="Preload Loss Thresholds:", font=self.header_font)
        self.cycle_header.grid(row=9, column=0, pady=20)
        self.displayed_cycles_header_1 = ctk.CTkLabel(self, text="Threshold Marker 1:", font=self.text_font)
        self.displayed_cycles_header_1.grid(row=10, column=0)

        self.displayed_cycles_header_2 = ctk.CTkLabel(self, text="Threshold Marker 2:", font=self.text_font)
        self.displayed_cycles_header_2.grid(row=11, column=0)
        self.displayed_cycles_header_3 = ctk.CTkLabel(self, text="Threshold Marker 3:", font=self.text_font)
        self.displayed_cycles_header_3.grid(row=12, column=0)
        # preload threshold entry
        self.threshold_entry_1 = ctk.CTkEntry(master=self, placeholder_text="preload threshold 1", width=20)
        self.threshold_entry_1.insert("0", "50")
        self.threshold_entry_1.grid(row=10, column=1, pady=5, padx=5, sticky= "nsew")
        self.threshold_entry_2 = ctk.CTkEntry(master=self, placeholder_text="preload threshold 2", width=20)
        self.threshold_entry_2.insert("0", "60")
        self.threshold_entry_2.grid(row=11, column=1, pady=5, padx=5, sticky= "nsew")
        self.threshold_entry_3 = ctk.CTkEntry(master=self, placeholder_text="preload threshold 3", width=20)
        self.threshold_entry_3.insert("0", "70")
        self.threshold_entry_3.grid(row=12, column=1, pady=5, padx=5, sticky= "nsew")
        # preload threshold checkbox
        self.threshold_checkbox_1 = ctk.CTkCheckBox(master=self, text="enable", command=self.checkbox_event, variable=self.t2_enabled, onvalue="on", offvalue="off")
        self.threshold_checkbox_1.grid(row=11, column=2, pady=5, sticky= "nsew")

        self.threshold_checkbox_2 = ctk.CTkCheckBox(master=self, text="enable", command=self.checkbox_event,variable=self.t3_enabled, onvalue="on", offvalue="off")
        self.threshold_checkbox_2.grid(row=12, column=2, pady=5, sticky= "nsew")

        # run button
        self.input_model_button = ctk.CTkButton(master=self, text="Generate Prediction", command=self.run_prediction_button_event, fg_color="green", hover_color="dark green")
        self.input_model_button.grid(row=13, column=1, columnspan=2, pady=40, sticky= "nsew")

    def set_parameter_label(self, name):
        '''Configures a label widget'''
        return ctk.CTkLabel(self, text= name, font=self.text_font)
    
    def set_parameter_options(self, values):
        '''Configures a menu with parameter values'''
        return ctk.CTkOptionMenu(self, values=values)
    
    # handle events
    def checkbox_event(self):
        if (self.t2_enabled.get() == "off"):
            self.threshold_entry_2.configure(state="disabled", fg_color="#262729")
            self.threshold_entry_2.select_clear()
        else:
            self.threshold_entry_2.configure(state="normal", fg_color="#343638")

        if (self.t3_enabled.get() == "off"):
            self.threshold_entry_3.configure(state="disabled", fg_color="#262729")
            self.threshold_entry_3.select_clear()
        else:
            self.threshold_entry_3.configure(state="normal", fg_color="#343638")

    def run_prediction_button_event(self):
        cycle_entry_str = self.cycle_entry.get()
        threshold_entry_str_1 = self.threshold_entry_1.get()
        threshold_entry_str_2 = self.threshold_entry_2.get()
        threshold_entry_str_3 = self.threshold_entry_3.get()

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
        threshold_1 = 0
        threshold_2 = 0
        threshold_3 = 0

        threshold_1 = self.get_threshold_value(threshold_entry_str_1)
        if (threshold_1 == 0):
            return
        if (self.t2_enabled.get() == "on"):
            threshold_2 = self.get_threshold_value(threshold_entry_str_2)
            if (threshold_2 == 0):
                return
        if (self.t3_enabled.get() == "on"):
            threshold_3 = self.get_threshold_value(threshold_entry_str_3)
            if (threshold_3 == 0):
                return

        self.controller.update_model(self.p1_options._current_value,
                                     self.p2_options._current_value,
                                     self.p3_options._current_value, 
                                     self.p4_options._current_value,
                                     self.p5_options._current_value,
                                     cycles,
                                     threshold_1, threshold_2, threshold_3)
        
        
        reportStr = self.get_report(threshold_1, threshold_2, threshold_3)
        
        self.parent.textbox.configure(state="normal", text_color="orange", border_color="#0E86D4")
        self.parent.textbox.delete("0.0", "end")
        self.parent.textbox.insert("0.0", reportStr)
        self.parent.textbox.configure(state="disabled")
        
        plot.draw_plot(self.parent.plotframe)

    def get_threshold_value(self, threshold_entry_str):
        threshold = -1
        try:
                threshold = int(re.search(r'\d+', threshold_entry_str).group())
        except:
                self.parent.textbox.configure(state="normal", text_color="red", border_color="red")
                self.parent.textbox.delete("0.0", "end")
                self.parent.textbox.insert("0.0", "Non integer input detected for threshold\n")
                self.parent.textbox.configure(state="disabled")
                return threshold
        
        if (threshold < 1 or threshold > 100):
            self.parent.textbox.configure(state="normal", text_color="red", border_color="red")
            self.parent.textbox.delete("0.0", "end")
            self.parent.textbox.insert("0.0", "Invalid threshold input\n")
            self.parent.textbox.configure(state="disabled")
        
        return threshold

    def get_report(self, threshold_1, threshold_2, threshold_3):
        genTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        threshold_str_1 = "-Threshold 1 at " + str(threshold_1) + "% preload loss\n"
        if (threshold_2 < 1):
            threshold_str_2 = ""
        else:
            threshold_str_2 = "-Threshold 2 at " + str(threshold_2) + "% preload loss\n"
        if (threshold_3 < 1):
            threshold_str_3 = ""
        else:
            threshold_str_3 = "-Threshold 3 at " + str(threshold_3) + "% preload loss\n"

        configStr = "Config:\n" + threshold_str_1 + threshold_str_2 + threshold_str_3 + "-Sealant: " + str(self.p1_options._current_value) + "\n-Plate Material: " + str(self.p2_options._current_value) + "\n-Bolt Diameter: " + str(self.p3_options._current_value) + "\n-Fastener Material: " + str(self.p4_options._current_value) + "\n-Fastener Thread Size: " + str(self.p5_options._current_value)
        return "Report:\nGeneration Time: " + genTime + "\nPreload decay threshold met at: " + str(self.controller.active_model.threshold_point) + " time cycles\n" + configStr    
        