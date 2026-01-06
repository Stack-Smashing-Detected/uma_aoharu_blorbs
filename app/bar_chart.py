import matplotlib.pyplot as plt


class BarChart:
    def __init__(self, data: dict, title="Aoharu Blorbs", xlabel="Skills", ylabel="Skill Frequency", bins=10):
        self.data = data
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.bins = bins

    def plot(self):
        plt.barh(self.data.keys(), self.data.values(), width=0.4)
        plt.figure(figsize=(10,6))
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.gca().invert_yxis()
        plt.tight_layout()
        plt.show()
        
    