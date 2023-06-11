import math

#only works with layers [2,2,2]
def back_propagation(neuralNetwork, target_values,  learning_rate):
    true_values = target_values
    derivative_vector_weights = []
    for layerI in range(1, len(neuralNetwork.layers)):
        derivative_vector_weights.append([])
        for nodeJ in range(0, len(neuralNetwork.layers[layerI])):
            derivative_vector_weights[layerI-1].append([])
            for weightK in range(0, len(neuralNetwork.layers[layerI][nodeJ].weights)):
                if layerI == 1:
                    d0 = derivative_wm1(neuralNetwork, 2, 0, nodeJ, weightK, true_values)
                    d1 = derivative_wm1(neuralNetwork, 2, 1, nodeJ, weightK, true_values)
                    derivative_vector_weights[layerI - 1][nodeJ].append(((d0 + d1)/2)*learning_rate)
                elif layerI == 2:
                    d0 = derivative_w(neuralNetwork, 2, nodeJ, weightK, true_values)
                    derivative_vector_weights[layerI - 1][nodeJ].append(d0*learning_rate)
                else:
                    raise ValueError("No deeper that 2 allowed")
    derivative_vector_biases = []
    for layerI in range(1, len(neuralNetwork.layers)):
        if layerI == 1:
            d0 = derivative_bm1(neuralNetwork, 2, 0, 0, true_values)
            d1 = derivative_bm1(neuralNetwork, 2, 0, 1, true_values)
            d2 = derivative_bm1(neuralNetwork, 2, 1, 0, true_values)
            d3 = derivative_bm1(neuralNetwork, 2, 1, 1, true_values)
            derivative_vector_biases.append(((d0 + d1 + d2 + d3)/4)*learning_rate)
        elif layerI == 2:
            d0 = derivative_b(neuralNetwork, 2, 0, true_values)
            d1 = derivative_b(neuralNetwork, 2, 1, true_values)
            derivative_vector_biases.append(((d0 + d1)/2)*learning_rate)
        else:
            raise ValueError("No deeper that 2 allowed")
    return derivative_vector_weights, derivative_vector_biases

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
def derivative_w(nn, layerI, nodeJ, weightK, true_values):
    return aL(nn, layerI-1, weightK) * derivative_relu( zL(nn, layerI, nodeJ) ) * derivative_C0(nn, nodeJ, true_values)

def derivative_b(nn, nodeLayerI, nodeJ, true_values):
    return derivative_relu( zL(nn, nodeLayerI, nodeJ) ) * derivative_C0(nn, nodeJ, true_values)

#not useful since aL cannot be adjusted
def derivative_aLm1(nn, layerI, nodeJ, target_nodeJ, true_values):
    weight = nn.layers[layerI][nodeJ].weights[target_nodeJ]
    return weight * derivative_relu( zL(nn, layerI, nodeJ) ) * derivative_C0_multi(nn, true_values)

def derivative_bm1(nn, nodeLayerI, nodeJ, target_nodeJ, true_values):
    weight = nn.layers[nodeLayerI][nodeJ].weights[target_nodeJ]
    zLm1 = zL(nn, nodeLayerI - 1, target_nodeJ)
    return derivative_relu(zLm1) * weight * derivative_relu( zL(nn, nodeLayerI, nodeJ) ) * derivative_C0_multi(nn, true_values)

#nodeLayer: output node layer, nodeJ: output node, target node: node in middle layers, target_weight: node in first layer
def derivative_wm1(nn, nodeLayerI, nodeJ, target_nodeJ, target_weight, true_values):
    weight = nn.layers[nodeLayerI][nodeJ].weights[target_nodeJ]
    zLm1 = zL(nn, nodeLayerI - 1, target_nodeJ)
    return aL(nn, nodeLayerI - 1, target_weight) * derivative_relu(zLm1) * weight * derivative_relu( zL(nn, nodeLayerI, nodeJ) ) * derivative_C0_multi(nn, true_values)

def derivative_C0(nn, nodeJ, true_values):
    last_layer = nn.layers[-1]
    if len(last_layer) != len(true_values):
        raise ValueError("Len do not match")
    return 2 * (last_layer[nodeJ].value - true_values[nodeJ])

def derivative_C0_multi(nn, true_values):
    last_layer = nn.layers[-1]
    if len(last_layer) != len(true_values):
        raise ValueError("Len do not match")
    error_sum = 0
    for i in range(0, len(last_layer)):
        error_sum += 2 * (last_layer[i].value - true_values[i])
    return error_sum

def derivative_relu(x):
    """ if x == 0:
        raise ValueError("Derivation of Relu is undefined for x = 0") """
    return 0 if x < 0 else 1
