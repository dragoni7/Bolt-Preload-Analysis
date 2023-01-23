#!/usr/bin/env python

"""__init__.py: Entry point for the application."""

__author__      = "Samuel Gibson"

import customtkinter
import preload_predictor_app

# initialize application
if __name__ == "__main__":
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

    app = preload_predictor_app.App()
    app.mainloop()
    