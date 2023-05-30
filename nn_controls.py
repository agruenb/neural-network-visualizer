from tkinter import ttk

def on_slider_change(param):
    return 0

def construct_controls(controls, neuralNetwork, repaint_function):
    
    control_num = 0
    for i in range(0, len(neuralNetwork.layers)):
        for j in range(0, len(neuralNetwork.layers[i])):
            node = neuralNetwork.layers[i][j]
            if i == 0:
                def build_on_input_change(node):
                    def on_input_change(value):
                        node.input_value = round(float(value), 3)
                        repaint_function()
                    return on_input_change
                ttk.Label(controls, text="Input "+str(j)).grid(column=0, row=control_num*2)
                ttk.Scale(controls, from_=-1, to=1, orient="horizontal", command=build_on_input_change(node)).grid(column=0, row= control_num*2+1)
                control_num += 1
            else:
                for k in range(0, len(neuralNetwork.layers[i-1])):
                    def build_on_input_change(node, weight_index):
                        def on_input_change(value):
                            node.weights[weight_index] = round(float(value), 3)
                            repaint_function()
                        return on_input_change
                    ttk.Label(controls, text="Weight L"+str(i)+" "+str(k+1)+"."+str(j+1)).grid(column=0, row=control_num*2)
                    ttk.Scale(controls, from_=-1, to=1, orient="horizontal", command=build_on_input_change(node, k)).grid(column=0, row= control_num*2+1)
                    control_num += 1
    #bias
    for i in range(1, len(neuralNetwork.layers)):
        def build_on_input_change(neuralNetwork, bias_index):
            def on_input_change(value):
                neuralNetwork.biases[bias_index] = round(float(value), 3)
                repaint_function()
            return on_input_change
        ttk.Label(controls, text="Bias "+str(i)).grid(column=0, row=control_num*2)
        ttk.Scale(controls, from_=-1, to=1, orient="horizontal", command=build_on_input_change(neuralNetwork, i)).grid(column=0, row= control_num*2+1)
        control_num += 1
    #output
    for i in range(0, len(neuralNetwork.layers[len(neuralNetwork.layers) -1])):
        def build_on_input_change(neuralNetwork, target_index):
            def on_input_change(value):
                neuralNetwork.targets[target_index] = round(float(value), 3)
                repaint_function()
            return on_input_change
        ttk.Label(controls, text="Output "+str(i)).grid(column=0, row=control_num*2)
        ttk.Scale(controls, from_=-1, to=1, orient="horizontal", command=build_on_input_change(neuralNetwork, i)).grid(column=0, row= control_num*2+1)
        control_num += 1
