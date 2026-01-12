import matplotlib

try:
    import PyQt6
    matplotlib.use("qtagg")
except ImportError:
    import tkinter
    matplotlib.use("tkagg")

import matplotlib.pyplot as plt


class BarChart:
    def __init__(self, data: dict,  type: str, title="Aoharu Blorbs", xlabel="Frequency(%)", ylabel="", bins=10):
        self.type = type
        self.data = self.evaluate_skill_chance(data)
        self.title = title + " - " + self.type
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.bins = bins

    def plot_chart(self):
        # calculate the percentage of each item.
        plt.figure(figsize=(16,9)) 
        plt.barh(self.data.keys(), self.data.values(), height=0.4)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.gca().invert_yaxis()  # Invert y-axis to have the highest values on top
        plt.tight_layout()
        plt.show()
        
    
    def evaluate_skill_chance(self, skill_counts: dict) -> dict: 
        total_skills = sum(skill_counts.values())
        skill_chances = {skill: (count / total_skills) * 100 for skill, count in skill_counts.items()}
        return skill_chances