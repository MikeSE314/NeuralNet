import Neuron
import Net

import os

# def __init__(self, inputs=[], bias=0):

def main(inputs):
    net = Net.Net()
    net.addRow()
    for inp in inputs:
        net.addNeuron(Neuron.Neuron(bias=float(inp)))
    net.last()
    print(net.output())
    print(net.toString())

if __name__ == "__main__":
    main(os.sys.argv[1:])

