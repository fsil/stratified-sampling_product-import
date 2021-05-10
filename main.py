import numpy as np
import pandas as pd

df = pd.read_csv("C:\\Users\\ACER\\Desktop\\strata\\pop.csv", low_memory=False)
df_unique = df.drop_duplicates(subset=['vin_or_lp'], keep='first', inplace=False)

N=10

print(df_unique)

goal = df_unique.groupby(['product', 'import'], group_keys=False).apply(lambda x: x.sample(int(np.rint(N*len(x)/len(df_unique))))).sample(frac=1).reset_index(drop=True)
print(goal)
goal.to_csv (r'C:\Users\ACER\Desktop\export_dataframe.csv', index=False, header=True)
