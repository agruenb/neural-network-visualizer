from tkinter import ttk
from nn_painter import paintNN
from window_layout import make_window
from neural_network import NeuralNetwork
from nn_controls import construct_controls
from back_prop import back_propagation

def main():
    target_values = [2, 2]
    nn = NeuralNetwork([2,2, 2])
    root, canvas, controls = make_window()
    nn.comp()
    derivatives_weights, derivatives_biases = back_propagation(nn, target_values, 1)
    paintNN(canvas, nn, derivatives_weights, derivatives_biases)
    def repaint_function():
        nn.comp()
        canvas.delete("all")
        derivatives_weights, derivatives_biases = back_propagation(nn, target_values, 1)
        paintNN(canvas, nn, derivatives_weights, derivatives_biases)
    
    construct_controls(controls, nn, repaint_function)
    root.mainloop()
    

if __name__ == "__main__":
    main()