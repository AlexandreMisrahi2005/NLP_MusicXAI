import pandas as pd
import random

data = pd.read_csv('processed/total.csv')

data_aug = data.copy()
n = len(data)
for i in range(n):
	print(f"{round(100*i/n,2)}% done",end='\t\t\r')

	col123 = [data.iloc[i]["user"],10*data.iloc[i]["dataID"],"aug_"+data.iloc[i]["filename"]]
	col_mid = [data.iloc[i,j+3]+round(random.gauss(0,0.5)) if data.iloc[i,j+3] is not None else None for j in range(28)]
	col_end = [data.iloc[i]["work_length"],data.iloc[i]["message"]]
	data_aug.loc[len(data_aug.index)] = col123 + col_mid + col_end

data_aug.to_csv("processed/total_augmented.csv",index=False)