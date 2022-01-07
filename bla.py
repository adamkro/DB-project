import pandas as pd
import numpy as np


df = pd.read_csv(f"./data/movie.csv", index_col=False, delimiter = ',')
df = df.where(df.notnull(), None)
print(df.head)
