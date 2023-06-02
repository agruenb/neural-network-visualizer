from tkinter import ttk
from nn_painter import paintNN
from window_layout import make_window
from neural_network import NeuralNetwork
from nn_controls import construct_controls
from back_prop import back_propagation

def main():
    target_values_sample_1 = [2.0, 2.0]
    target_values_sample_2 = [2.0, 2.0]
    nn = NeuralNetwork([2,2,2])#only possible setup for backpropagation
    root, canvas, controls = make_window()
    def repaint_function():
        nn.comp()
        canvas.delete("all")
        derivatives_weights, derivatives_biases = back_propagation(nn, target_values_sample_1, 1)
        paintNN(canvas, nn, derivatives_weights, derivatives_biases, target_values_sample_1)
    repaint_function()
    construct_controls(controls, nn, repaint_function, target_values_sample_1, target_values_sample_2)
    root.mainloop()
    

if __name__ == "__main__":
    main()