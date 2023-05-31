from tkinter import ttk
from nn_painter import paintNN
from window_layout import make_window
from neural_network import NeuralNetwork
from nn_controls import construct_controls
from back_prop import back_propagation

def main():
    nn = NeuralNetwork([1,2, 1])
    root, canvas, controls = make_window()
    nn.comp()
    paintNN(canvas, nn)
    def repaint_function():
        nn.comp()
        canvas.delete("all")
        paintNN(canvas, nn)
        back_propagation(nn)
    
    construct_controls(controls, nn, repaint_function)
    root.mainloop()
    

if __name__ == "__main__":
    main()