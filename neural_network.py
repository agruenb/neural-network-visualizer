from nn_node import Node
import numpy as np

class NeuralNetwork:

    layers = []
    biases = []
    targets = [0,0]

    def __init__(self, layerStructure):
        self.constructNodes(layerStructure)

    def constructNodes(self, layerStructure):
        for layerI in range(0, len(layerStructure)):
            layer = []
            for nodeI in range(0, layerStructure[layerI]):
                weights = []
                if layerI == 0:
                    weights = [1]
                else:
                    weights = list(np.ones(layerStructure[layerI - 1]))
                node = Node(weights, lambda x:max(0,x))
                layer.append(node)
            self.layers.append(layer)
            self.biases.append(1)

    def print(self):
        for layer in self.layers:
            print(len(layer))
