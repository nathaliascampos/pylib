import pandas as pd


def read_excel(path):
    dataset = pd.read_excel(path)
    return dataset
