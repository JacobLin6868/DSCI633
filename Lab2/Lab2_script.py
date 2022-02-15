import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a = pd.read_csv('data/patients.csv')
df = a.iloc[:, 0].str.split(';', expand=True)
list_of_columns = df.columns = ['pateintNo', 'gender', 'vist', 'HR', 'SBP', 'DBP', 'DX', 'AE']
print(df)

# '0' or '1'
# if missing or invalid, 0




def recode_empty_cells(dataframe, column_list):
    for column in column_list:
        dataframe[column] = dataframe[column].replace('', np.nan, regex=True)
        dataframe[column] = dataframe[column].fillna(0)
    return df


recode_empty_cells(df, list_of_columns)
print(df)
