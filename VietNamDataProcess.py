import json
import os

import pandas as pd
import numpy as np
with open(os.path.join("VietNam.json"), encoding="utf-8") as f:
    raw_data = json.load(f)

vietnam_covid_data = raw_data["report"][0]['data']
dates = pd.date_range('1/1/2021', periods=485)
vietnam_covid_data_df = pd.DataFrame(vietnam_covid_data, columns=['timestamp','local_case'], index=dates)
vietnam_covid_data_df.drop(['timestamp'],axis = 1, inplace = True)
vietnam_quarantine_data = raw_data["report"][1]['data']
vietnam_quarantine_data_df = pd.DataFrame(vietnam_quarantine_data, columns=['timestamp','quarantine_case'], index=dates)
vietnam_quarantine_data_df.drop(['timestamp'],axis = 1, inplace = True)
vietnam_death_data = raw_data["report"][2]['data']
vietnam_death_data_df = pd.DataFrame(vietnam_death_data, columns=['timestamp','death_case'], index=dates)
vietnam_death_data_df.drop(['timestamp'],axis = 1, inplace = True)
vietnam_df=pd.concat([vietnam_covid_data_df,vietnam_quarantine_data_df,vietnam_death_data_df], axis = 1)
vietnam_df.to_csv("covid_data_vietnam_overall.csv", encoding = "utf-8")
