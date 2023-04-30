import customtkinter as ctk
import typing

class FloatSpinbox(ctk.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 min: int = 0,
                 max: int = 200000,
                 step_size: typing.Union[int, float] = 1,
                 command: typing.Callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
    
        self.step_size = step_size
        self.min = min
        self.max = max
        self.command = command
        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = ctk.CTkButton(self, text="-", width=height-6, height=height-6,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = ctk.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = ctk.CTkButton(self, text="+", width=height-6, height=height-6,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "0.0")

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) + self.step_size

            if (value <= self.max and value >= self.min):
                self.entry.configure(state='normal')
                self.entry.delete(0, "end")
                self.entry.insert(0, value)
                self.entry.configure(state='disabled')
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) - self.step_size

            if (value <= self.max and value >= self.min):
                self.entry.configure(state='normal')
                self.entry.delete(0, "end")
                self.entry.insert(0, value)
                self.entry.configure(state='disabled')
        except ValueError:
            return

    def get(self) -> typing.Union[float, None]:
        try:
            return float(self.entry.get())
        except ValueError:
            return None

    def set(self, value: float):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(float(value)))
        self.entry.configure(state='disabled')