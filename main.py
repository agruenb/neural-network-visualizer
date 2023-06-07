from tkinter import ttk
from nn_painter import paintNN
from window_layout import make_window
from neural_network import NeuralNetwork
from nn_controls import construct_controls
from back_prop import back_propagation

def main():
    input_values_sample_1 = [1.0, 1.0]
    target_values_sample_1 = [2.0, 2.0]
    input_values_sample_2 = [1.0, 1.0]
    target_values_sample_2 = [2.0, 2.0]
    nn = NeuralNetwork([2,2,2])#only possible setup for backpropagation
    nn2 = NeuralNetwork([2,2,2])#for 2nd overservation/sample
    root, canvas, controls = make_window()
    def repaint_function(samples = 1):
        nn.comp()
        nn2.comp()
        canvas.delete("all")
        derivatives_weights, derivatives_biases = [], []
        if samples == 1:
            derivatives_weights, derivatives_biases = back_propagation(nn, target_values_sample_1, 1)
        if samples == 2:
            derivatives_weights_1, derivatives_biases_1 = back_propagation(nn, target_values_sample_1, 1)
            derivatives_weights_2, derivatives_biases_2 = back_propagation(nn2, target_values_sample_2, 1)
            # average over samples
            for i in range(0, len(derivatives_weights_1)):
                derivatives_weights.append([])
                for j in range(0, len(derivatives_weights_1[i])):
                    derivatives_weights[i].append([])
                    for k in range(0, len(derivatives_weights_1[i][j])):
                        avg = round((derivatives_weights_1[i][j][k] + derivatives_weights_2[i][j][k]) /2, 3)
                        derivatives_weights[i][j].append(avg)
            for i in range(0, len(derivatives_biases_1)):
                avg = round((derivatives_biases_1[i] + derivatives_biases_2[i]) /2, 3)
                derivatives_biases.append(avg)
        paintNN(canvas, nn, derivatives_weights, derivatives_biases, target_values_sample_1, target_values_sample_2, nn2)
    repaint_function()
    construct_controls(controls, nn, nn2, repaint_function, input_values_sample_1, input_values_sample_2, target_values_sample_1, target_values_sample_2)
    root.mainloop()
    
if __name__ == "__main__":
    main()