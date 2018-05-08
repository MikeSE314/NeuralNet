import Neuron

class Net:
    def __init__(self):
        self.rows = []

    def addNeuron(self, neuron):
        self.rows[-1].append(neuron)

    def addRow(self):
        self.rows.append([])

    def last(self):
        self.rows.append([])
        self.rows[-1].append(Neuron.Neuron([retFunc.output for retFunc in self.rows[-2]]))

    def output(self):
        return self.rows[-1][0].output()

    def toString(self):
        ret = ""
        for row in self.rows:
            for neuron in row:
                ret += neuron.toString()
            ret += "\n"
        return ret
