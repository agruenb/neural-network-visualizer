from nn_node import Node
import numpy as np

class NeuralNetwork:

    def __init__(self, layerStructure):
        self.layers = []
        self.biases = []
        self.constructNodes(layerStructure)
        self.targets = list(np.ones(layerStructure[len(layerStructure) - 1]))

    def constructNodes(self, layerStructure):
        np.random.seed(123)
        for layerI in range(0, len(layerStructure)):
            layer = []
            for nodeI in range(0, layerStructure[layerI]):
                weights = []
                if layerI == 0:
                    weights = [1]
                else:
                    weights = list(np.random.uniform(-1, 1, layerStructure[layerI - 1]).round(3))
                node = Node(weights, lambda x:max(0,x))
                layer.append(node)
            self.layers.append(layer)
            self.biases.append(1.0)
    
    def comp(self):
        for layerI in range(1, len(self.layers)):
            for nodeI in range(0, len(self.layers[layerI])):
                inputs = []
                for prev_nodeI in range(0, len(self.layers[layerI - 1])):
                    inputs.append(self.layers[layerI - 1][prev_nodeI].value)
                self.layers[layerI][nodeI].comp(inputs, self.biases[layerI])

    def print(self):
        for layer in self.layers:
            print(len(layer))
