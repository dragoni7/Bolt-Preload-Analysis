import customtkinter as ctk

class ModelsFrame(ctk.CTkFrame):
    def __init__(self, *args, header_name = "Models", **kwargs):
        super().__init__(*args,  **kwargs)

        self.header_name = header_name

        self.header = ctk.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=0)