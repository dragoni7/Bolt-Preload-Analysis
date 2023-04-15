from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from controller.model_controller import ModelController

__canvas = None

def draw_plot(self):
        '''Draws the active model's plot figure onto a canvas'''
        global __canvas
        if __canvas: __canvas.get_tk_widget().pack_forget()
        __canvas = FigureCanvasTkAgg(ModelController.get_instance().active_model.figure, master=self)
        __canvas.draw()
        __canvas.get_tk_widget().grid(row=0, column=0, rowspan=5, columnspan=5, padx=15, pady=15, sticky="nsew")