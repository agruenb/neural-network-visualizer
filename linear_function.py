class LinearFunc:

    transform_value = 1
    
    def __init__(self, transform_value):
        self.transform_value = transform_value

    def comp(self, x):
        return self.transform_value*x
