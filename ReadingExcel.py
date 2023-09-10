import pandas as pd

data = pd.read_csv('C:\Temp\panda.csv')
for i in range(len(data)):
    print(data.iloc[i, 0],data.iloc[i, 1],data.iloc[i, 2])
    print('----------------------------------------------------------')
