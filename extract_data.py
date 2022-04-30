import json
import os

import pandas as pd
import numpy as np
with open(os.path.join("payload.json"), encoding="utf-8") as f:
    raw_data = json.load(f)
covid_data = pd.DataFrame()
temp_data = []
column_stack = []
for element in raw_data:
    column_stack.append(element["tinh"].split("Tỉnh")[-1])
    temp_data.append(element["data"])
data = np.zeros(len(temp_data[0])).reshape(-1,1)
# print(data.shape)
# print((list(temp_data[0].values())))

for dt in temp_data:
    index = dt.keys()
    # print(np.array(list(dt.values())).reshape(-1,1))
    data = np.concatenate((data,np.array(list(dt.values())).reshape(-1,1) ), axis=1)

data = np.delete(data,0,1)
data = np.delete(data,63,1)
data_dict = dict(zip(index,data))
# print(data_dict.keys())
df = pd.DataFrame.from_dict(data_dict,orient="index", columns=column_stack[:-1])
df.to_csv("covid_data.csv", encoding = "utf-8")