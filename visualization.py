import matplotlib.pyplot as plt
import numpy as np

class Visualization:
    def __init__(self, ndarray):
        self.width = 0.5
        self.arr = ndarray
        self.x = list(set(np.array(self.arr["release_dates"], dtype=float).tolist()))
        self.y1 = self.arr[self.arr["engine"] == "Unity"]
        self.y2 = self.arr[self.arr["engine"] == "Unreal"]

        self._y1 = [0 for _ in range(len(self.x))]
        self._y2 = [0 for _ in range(len(self.x))]
        for index in self.y1.index:
            for i in range(len(self.x)):
                if self.y1.loc[index, "release_dates"] == self.x[i]:
                    self._y1[i] += 1
        
        for index in self.y2.index:
            for i in range(len(self.x)):
                if self.y2.loc[index, "release_dates"] == self.x[i]:
                    self._y2[i] += 1

    def bar(self):
        plt.title("Unity vs Unreal Engine")
        plt.bar(np.array(self.x) - self.width / 2.0, self._y1, self.width, color='blue')
        plt.bar(np.array(self.x) + self.width / 2.0, self._y2, self.width, color='orange')
        plt.xlabel("Year")
        plt.ylabel("Games")
        plt.legend(["Unity", "Unreal Engine"])
        plt.savefig("./exports/figure.png")
        plt.show()