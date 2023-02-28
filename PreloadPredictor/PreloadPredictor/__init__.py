#!/usr/bin/env python

"""__init__.py: Entry point for the application."""

__author__      = "Samuel Gibson"

import customtkinter as ctk
import preload_predictor_app as app

# initialize application
if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

    CTK_Window = app.App()
    CTK_Window.mainloop()
    