from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from controller.model_controller import ModelController

canvas = None

def draw_plot(self):
        global canvas
        if canvas: canvas.get_tk_widget().pack_forget()
        canvas = FigureCanvasTkAgg(ModelController.getInstance().activeModel().getFig(), master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=2, rowspan=4, columnspan=4, padx=15, pady=15, sticky="nsew")