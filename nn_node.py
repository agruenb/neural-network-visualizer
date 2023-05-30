class Node:

    weights = []
    input_value = 1
    non_linear_transformer = lambda x: x
    
    def __init__(self, weights, non_linear_transformer):
        self.weights = weights
        self.non_linear_transformer = non_linear_transformer

    def comp(self, inputs, bias):
        weighted_sum = 0
        #check if lenghts fit
        if len(self.weights) != len(inputs):
            raise ValueError("Node number of inputs does not match length of weights")
        for index in range(0, len(inputs)):
            weighted_sum += self.weights[index]*inputs[index]
        return self.non_linear_transformer(weighted_sum + bias)

