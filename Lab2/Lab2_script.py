import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import logical_or

data = pd.read_csv('data/patients.txt', delimiter=";", header= None)
list_of_columns = data.columns = ['patientNo', 'gender', 'vist', 'HR', 'SBP', 'DBP', 'DX', 'AE']

print(data)

#replace all empty cells with NAN
# data.replace(r'^\s*$', np.nan, regex=True, inplace=True)

#AE column
data['AE'].replace(r'\D', np.nan, regex=True, inplace=True)
data['AE'].fillna(0, inplace=True)

#DX column
data['DX'].replace(r'[a-zA-Z]', np.nan, regex=True, inplace=True)
data['DX'].replace(r'^\s*$', np.nan, regex=True, inplace=True)
data['DX'].fillna(999, inplace=True)
print(data)
print('\n')
#DBP
data['DBP'].replace(r'^\s*$', 0, regex=True, inplace=True)
data['DBP'] = data['DBP'].astype(str).astype(int)
a = np.array(data['DBP'].values.tolist())
data['DBP'] = np.where(logical_or(a < 60, a > 120), 60, a).tolist()
# print(data)


#SBP
data['SBP'].replace(r'^\s*$', 0, regex=True, inplace=True)
data['SBP'] = data['SBP'].astype(str).astype(int)
a = np.array(data['SBP'].values.tolist())
data['DBP'] = np.where(logical_or(a < 80, a > 200), 80, a).tolist()
# print(data)

#SBP
data['HR'].replace(r'^\s*$', 0, regex=True, inplace=True)
data['DX'].replace(r'[a-zA-Z]', 0, regex=True, inplace=True)
# data['HR'] = data['HR'].astype(str).astype(int)
# a = np.array(data['HR'].values.tolist())
# data['HR'] = np.where(logical_or(a < 40, a > 100), 40, a).tolist()
# print(data)




