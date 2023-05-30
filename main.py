from tkinter import ttk
from nn_painter import paintNN
from window_layout import make_window
from neural_network import NeuralNetwork
from nn_controls import construct_controls

def main():
    nn = NeuralNetwork([2,2,2])
    root, canvas, controls = make_window()
    paintNN(canvas, nn)
    def repaint_function():
        canvas.delete("all")
        paintNN(canvas, nn)
    
    construct_controls(controls, nn, repaint_function)
    root.mainloop()

if __name__ == "__main__":
    main()