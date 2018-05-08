class Neuron:
    def __init__(self, inputs=[], bias=0):
        self.DEFAULT_WEIGHT = 1.
        # [func, func, func]
        self.bias = bias
        self.inputs = []
        for inp in inputs:
            self.inputs.append((inp, self.DEFAULT_WEIGHT))

    def output(self):
        r = 0.
        for inp in self.inputs:
            r += inp[0].__call__() * inp[1]
        r += self.bias
        if r > 0:
            return 1
        return 0

    def changeWeights(self):
        pass

    def clearInputs(self):
        self.inputs = []

    def setInputs(self):
        self.inputs = []
        for inp in inputs:
            self.inputs.append((inp, self.DEFAULT_WEIGHT))

    def getInputs(self):
        return [inp for (inp, weight) in self.inputs]

    def setBias(self, bias):
        self.bias = bias

    def getBias(self):
        return self.bias

    def toString(self):
        ret = "bias: " + str(self.bias) + "\n"
        for inp in self.inputs:
            ret += "input: " + str(inp[0].__call__()) + " weight: " + str(inp[1]) + "\n"
        return ret
