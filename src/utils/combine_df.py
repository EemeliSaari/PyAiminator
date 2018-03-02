import os

import pandas as pd

from src.paths import DataPath


def combine_batch(index, path):

    files = [os.path.join(path, x) for x in os.listdir(path) if index in x]
    dataframes = [pd.read_csv(x) for x in files]

    return pd.concat(dataframes, axis=1)


def combine_all():

    dp = DataPath()

    for directory in os.listdir(dp.collected):
        df = combine_batch(directory, dp.collected)
        df.to_csv(os.path.join(dp.combined, '{:s}.csv'.format(directory)))
