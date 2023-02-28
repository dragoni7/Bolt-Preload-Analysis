"""__preloadpredictor__.py: Handles plotting for the application."""

__author__      = "Samuel Gibson"

import numpy as np
import matplotlib.pyplot as plt
import thor_model as model

__fig_size = (8,8)

def reset_plot():
    plot_x = np.arange(10000)
    plot_y = model.exp_model(plot_x)
    fig = plt.figure(figsize=__fig_size)
    plt.ylim([0,100])
    plt.axhline(y=60, color='r', linestyle='-')
    plt.plot(plot_x, plot_y,'-g', label="Thor Model")
    plt.xlabel("Time")
    plt.ylabel("% Force")
    
    plt.legend()
    return fig

def plot(a, b, c, d):
    plot_x = np.arange(10000)
    plot_y = model.exp_model(plot_x, a, b, c, d)
    fig = plt.figure(figsize=__fig_size)
    plt.ylim([0,100])
    plt.axhline(y=60, color='r', linestyle='-')
    plt.plot(plot_x, plot_y,'-g', label="Thor Model")
    plt.xlabel("Time")
    plt.ylabel("% Force")
    return fig
