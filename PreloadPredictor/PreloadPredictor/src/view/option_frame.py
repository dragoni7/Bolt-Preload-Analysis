import customtkinter as ctk

class OptionFrame(ctk.CTkFrame):
    '''Frame to hold options'''
    def __init__(self, *args, header_name = "Options", **kwargs):
        super().__init__(*args,  **kwargs)

        self.header_name = header_name

        self.header = ctk.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=0)