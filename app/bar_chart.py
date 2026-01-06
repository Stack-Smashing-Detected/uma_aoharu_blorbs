import matplotlib.pyplot as plt


class Histogram:
    def __init__(self, data, title="Histogram", xlabel="Value", ylabel="Frequency", bins=10):
        self.data = data
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.bins = bins

    def plot(self):
        plt.hist(self.data, bins=self.bins, edgecolor='black')
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()