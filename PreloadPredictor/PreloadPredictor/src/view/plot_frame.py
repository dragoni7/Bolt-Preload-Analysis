import customtkinter as ctk
import view.plot_update_helper as plot

class PlotFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,  **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        plot.draw_plot(self)
