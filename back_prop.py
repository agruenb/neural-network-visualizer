import math


def back_propagation(neuralNetwork):
    learning_rate = 1
    output_layer = neuralNetwork.layers[len(neuralNetwork.layers) - 1]
    y = neuralNetwork.targets
    wL = 0.5
    aL0 = 1.5
    bL = 1
    sigma = derivative_relu
    zL = wL * aL0 + bL
    #aL = sigma(zL)
    print(derivative_cost_w(neuralNetwork, 2, 0, 0, 2))
    weights_adjustments = [[]]

def zL(nn, layerI, nodeJ):
    node = nn.layers[layerI][nodeJ]
    zL = nn.biases[layerI]
    for j in range(0, len(nn.layers[layerI - 1])):
        zL += node.weights[j]*aL(nn, layerI - 1, j)
    return zL

def aL(nn, layerI, nodeJ):
    node = nn.layers[layerI][nodeJ]
    #input nodes
    if layerI == 0:
        return nn.layers[0][nodeJ].value
    #relu
    return max(0, zL(nn, layerI, nodeJ))

#calculates the effect of weightK of nodeJ on the cost (node.value - true value)**2
def derivative_cost_w(nn, layerI, nodeJ, weightK, true):
    return aL(nn, layerI-1, weightK) * derivative_relu( zL(nn, layerI, nodeJ) ) * 2 * ( aL(nn, layerI, nodeJ) - true)
    
    


    

def derivative_relu(x):
    """ if x == 0:
        raise ValueError("Derivation of Relu is undefined for x = 0") """
    return 0 if x < 0 else 1
