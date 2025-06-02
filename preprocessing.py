import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("./dataset/games.csv")

dataset = dataset.dropna(subset="release_dates")
dataset = dataset.drop_duplicates()
dataset = dataset.sort_values(by="release_dates")

values = ["Unity", "Unreal Engine 1", "Unreal Engine 2, Unreal Engine 3", "Unreal Engine 4"]
dataset = dataset[dataset["engine"].isin(values)]

for index in dataset.index:
    for i in range(1, 5):
        if dataset.loc[index, "engine"] == f"Unreal Engine {i}":
            dataset.loc[index, "engine"] = "Unreal"

dataset.to_csv("./dataset/cleaned.csv", index=False)
