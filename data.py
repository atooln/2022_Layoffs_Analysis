# imports
import pandas as pd
import numpy as np


# dataset: https://www.kaggle.com/datasets/swaptr/layoffs-2022


class dataset:
    def __init__(self, path_to_csv):
        data = pd.read_csv(path_to_csv)
        print(data)


# test
if __name__ == '__main__':
    pwd = '/Users/hammer/repos/cogs_project/datasets'
    file = 'layoffs.csv'
    path = pwd + '/' + file

    dataset(path)
