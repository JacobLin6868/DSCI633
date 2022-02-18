import math

import data as data
import numpy as np
import matplotlib.pyplot as plt
import re
import random
import pandas as pd
from numpy import logical_or

data = pd.read_csv('data/patients.txt', delimiter=";", header=None)
list_of_columns = data.columns = ['patientNo', 'gender', 'vist', 'HR', 'SBP', 'DBP', 'DX', 'AE']
print('\n')
print('Raw Data')


# replace all empty cells with NAN
# data.replace(r'^\s*$', np.nan, regex=True, inplace=True)

# AE column
data['AE'].replace(r'\D', np.nan, regex=True, inplace=True)
data['AE'].fillna(0, inplace=True)

# DX column
data['DX'].replace(r'[a-zA-Z]', np.nan, regex=True, inplace=True)
data['DX'].replace(r'^\s*$', np.nan, regex=True, inplace=True)
data['DX'].fillna(999, inplace=True)
# print(data)
# print('\n')


# DBP
data['DBP'].replace(r'^\s*$', 60, regex=True, inplace=True)
data['DX'].replace(r'[a-zA-Z]', 60, regex=True, inplace=True)
data['DBP'] = data['DBP'].astype(str).astype(int)
data['DBP'] = data['DBP'].apply(lambda x: [80 if x < 60 else (120 if x > 120 else x)])
data['DBP'] = data['DBP'].astype(str)
data['DBP'] = data['DBP'].replace(r'\D', '', regex=True)


# print(data)


# SBP
data['SBP'].replace(r'^\s*$', 0, regex=True, inplace=True)
data['SBP'] = data['SBP'].astype(str).astype(int)
data['SBP'] = data['SBP'].apply(lambda x: [80 if x < 80 else (200 if x > 200 else x)])
data['SBP'] = data['SBP'].astype(str)
data['SBP'] = data['SBP'].replace(r'\D', '', regex=True)

# HR
data['HR'].replace(r'^\s*$', 0, regex=True, inplace=True)
data['HR'].replace(r'[a-zA-Z]', 0, regex=True, inplace=True)
data['HR'] = data['HR'].astype(str).astype(int)
data['HR'] = data['HR'].apply(lambda x: [80 if x < 40 else (100 if x > 100 else x)])
data['HR'] = data['HR'].astype(str)
data['HR'] = data['HR'].replace(r'\D', '', regex=True)

print(data)


# vist
data['vist'].astype(str)
data['vist'].replace(r'^\s*$', '01011900', regex=True, inplace=True)
# print(data)
# handles row 12 and 27
data['vist'].replace(r'[a-zA-Z]+', np.nan, regex=True, inplace=True)
data['vist'].fillna('01011900', inplace=True)
# print(data)
# new dataframe for breaking down MM DD YYYY
date_data = pd.DataFrame(columns=['reference', 'MM', 'DD', 'YYYY'])
date_data.astype(str)
date_data['reference'] = data['vist']
date_data['MM'] = date_data['reference'].str[:2].astype(int)
date_data['DD'] = date_data['reference'].str[2:4].astype(int)
date_data['YYYY'] = date_data['reference'].str[4:].astype(int)
# print(date_data)

date_data['MM'] = date_data['MM'][date_data['MM'].between(1, 12)]
date_data['MM'] = date_data['MM'].fillna(12)
# print(date_data)
date_data['DD'] = date_data['DD'][date_data['DD'].between(1, 31)]
date_data['DD'] = date_data['DD'].fillna(31)
# print(date_data)
date_data['YYYY'] = date_data['YYYY'][date_data['YYYY'].between(0, 1999)]
date_data['YYYY'] = date_data['YYYY'].fillna(1999)
date_data['YYYY'] = date_data['YYYY'].apply(lambda x: x + 1900 if x < 100 else (x + 1000 if x < 1000 else x))
date_data = date_data.astype(int).astype(str)
date_data['MM'] = date_data['MM'].apply(lambda x: '{0:0>2}'.format(x))
date_data['DD'] = date_data['DD'].apply(lambda x: '{0:0>2}'.format(x))
# print(date_data)

data['vist'] = date_data['MM'] + date_data['DD'] + date_data['YYYY']
# print(data)

# patientNo
data['patientNo'].replace(r'[a-zA-Z]', 199, regex=True, inplace=True)
data['patientNo'].replace(r'^\s*$', 199, regex=True, inplace=True)
data['patientNo'] = data['patientNo'].astype(str).astype(int)
max_value = data['patientNo'].max()


data['patientNo'] = data['patientNo'].where(~data['patientNo'].duplicated(), random.randint(200, 200))
data['patientNo'] = data['patientNo'].where(~data['patientNo'].duplicated(), random.randint(201, 201))
data['patientNo'] = data['patientNo'].where(~data['patientNo'].duplicated(), random.randint(202, 202))
data['patientNo'] = data['patientNo'].where(~data['patientNo'].duplicated(), random.randint(203, 203))
data['patientNo'] = data['patientNo'].astype(int).astype(str)
data['patientNo'] = data['patientNo'].apply(lambda x: '{0:0>3}'.format(x))
print('\n')
print('Cleaned Data')
print(data)


