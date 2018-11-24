import pandas as pd
data = pd.read_csv("name.csv",header=None)
del data[1]
del data[2]
del data[3]
data.to_csv('training.csv', index=False, header=None)
