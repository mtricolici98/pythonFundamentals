import pandas as pd

dataframe = pd.read_json('employee_list.json')
print(dataframe)
dataframe = dataframe.sort_values('salary')

salaries = dataframe['salary']
print(salaries)

positions = dataframe['position']
print(positions.drop_duplicates())

print(dataframe.groupby('position').mean())
print(positions.value_counts())
print(salaries.idxmin())

