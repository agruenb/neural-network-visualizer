from tkinter import *
from tkinter import ttk

def make_window():
    root = Tk()
    root.resizable(width=False, height=False)
    root.title("AAA Neural Network")

    wrapper = ttk.Frame(root, padding=0)
    wrapper.pack()

    canvas_width = 800
    canvas_height = 600
    canvas = Canvas(wrapper, width=canvas_width, height=canvas_height)
    canvas.pack(side="left")

    controls = ttk.Frame(wrapper)
    controls.pack(side="right", padx=5, pady=5)

    return root, canvas, controls
