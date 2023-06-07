from tkinter import ttk
import tkinter as tk

def on_slider_change(param):
    return 0

def construct_controls(controls, neuralNetwork, neuralNetwork2, repaint_function, input_values_1, input_values_2, target_values_1, target_values_2):
    
    controls_left = ttk.Frame(controls)
    controls_left.pack(side="left", padx=5, pady=5)
    controls_right = ttk.Frame(controls)
    controls_right.pack(side="right", padx=5, pady=5)
    control_num = 0
    for i in range(0, len(neuralNetwork.layers)):
        for j in range(0, len(neuralNetwork.layers[i])):
            node = neuralNetwork.layers[i][j]
            if i == 0:
                #input nodes
                pass
            else:
                for k in range(0, len(neuralNetwork.layers[i-1])):
                    def build_on_input_change(node, weight_index):
                        def on_input_change(value):
                            node.weights[weight_index] = round(float(value), 3)
                            repaint_function()
                        return on_input_change
                    ttk.Label(controls_left, text="Weight L"+str(i)+" "+str(k+1)+"."+str(j+1)).grid(column=0, row=control_num*2)
                    ttk.Scale(controls_left, value=node.weights[k], from_=-1, to=1, orient="horizontal", command=build_on_input_change(node, k)).grid(column=0, row= control_num*2+1)
                    control_num += 1
    #bias
    for i in range(1, len(neuralNetwork.layers)):
        def build_on_input_change(neuralNetwork, bias_index):
            def on_input_change(value):
                neuralNetwork.biases[bias_index] = round(float(value), 3)
                repaint_function()
            return on_input_change
        ttk.Label(controls_left, text="Bias "+str(i)).grid(column=0, row=control_num*2)
        ttk.Scale(controls_left, value=neuralNetwork.biases[i], from_=0, to=2, orient="horizontal", command=build_on_input_change(neuralNetwork, i)).grid(column=0, row= control_num*2+1)
        control_num += 1
    
    control_num_r = 0
    #right panel
    #input 1
    for i in range(0, len(input_values_1)):
        node = neuralNetwork.layers[0][i]
        def build_on_input_change(node):
            def on_input_change(value):
                node.value = round(float(value), 3)
                repaint_function()
            return on_input_change
        ttk.Label(controls_right, text="Sample 1 Input "+str(i+1)).grid(column=0, row=control_num_r*2)
        ttk.Scale(controls_right, value=input_values_1[i], from_=0, to=1, orient="horizontal", command=build_on_input_change(node)).grid(column=0, row= control_num_r*2+1)
        control_num_r += 1
    #output 1
    for i in range(0, len(target_values_1)):
        def build_on_input_change(target_index):
            def on_input_change(value):
                target_values_1[target_index] = round(float(value), 3)
                repaint_function()
            return on_input_change
        ttk.Label(controls_right, text="Sample 1 Output "+str(i+1)).grid(column=0, row=control_num_r*2)
        ttk.Scale(controls_right, value=target_values_1[i], from_=0, to=2, orient="horizontal", command=build_on_input_change(i)).grid(column=0, row= control_num_r*2+1)
        control_num_r += 1
    var = tk.IntVar()
    var.set(1)
    def build_on_sample_change():
        def on_input_change():
            repaint_function(var.get())
        return on_input_change
    ttk.Label(controls_right, text="Include Sample 2").grid(column=0, row=control_num_r*2)
    ttk.Checkbutton(controls_right, variable=var, onvalue=2, offvalue=1, command=build_on_sample_change()).grid(column=0, row= control_num_r*2+1)
    control_num_r += 1
    #input 2
    for i in range(0, len(input_values_2)):
        node = neuralNetwork2.layers[0][i]
        def build_on_input_change(node):
            def on_input_change(value):
                node.value = round(float(value), 3)
                repaint_function(var.get())
            return on_input_change
        ttk.Label(controls_right, text="Sample 2 input "+str(i+1)).grid(column=0, row=control_num_r*2)
        ttk.Scale(controls_right, value=input_values_2[i], from_=0, to=1, orient="horizontal", command=build_on_input_change(node)).grid(column=0, row= control_num_r*2+1)
        control_num_r += 1
    #output 2
    for i in range(0, len(target_values_2)):
        def build_on_input_change(target_index):
            def on_input_change(value):
                target_values_2[target_index] = round(float(value), 3)
                repaint_function(var.get())
            return on_input_change
        ttk.Label(controls_right, text="Sample 2 Output "+str(i+1)).grid(column=0, row=control_num_r*2)
        ttk.Scale(controls_right, value=target_values_2[i], from_=0, to=2, orient="horizontal", command=build_on_input_change(i)).grid(column=0, row= control_num_r*2+1)
        control_num_r += 1
