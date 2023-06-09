from tkinter import *
from tkinter import ttk

def make_window():
    root = Tk()
    root.title("AAA Neural Network (ReLU)")

    wrapper = ttk.Frame(root, padding=0)
    wrapper.pack()

    canvas_width = 880
    canvas_height = 600
    canvas = Canvas(wrapper, width=canvas_width, height=canvas_height)
    canvas.pack(side="left")

    controlsWrapper = ttk.Frame(wrapper)
    controlsWrapper.pack(side="right", padx=5, pady=5)

    return root, canvas, controlsWrapper
