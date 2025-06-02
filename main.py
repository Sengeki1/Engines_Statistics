import pandas as pd
from classification import Classifier
from visualization import Visualization

def main():
    dataset = pd.read_csv("./dataset/cleaned.csv")
    input = dataset[["title", "release_dates"]]
    output = dataset["engine"]

    classifier = Classifier(input, output)
    classifier.train()
    classifier.predict()
    classifier.accuracy()

    visualization = Visualization(dataset)
    visualization.plot()

if __name__ == "__main__":
    main()