import pandas as pd

file = open('conversion_rates.json')
data_frame = pd.read_json(file)

data_frame = data_frame.transpose()
data_frame.sort_values('inverseRate', inplace=True, ascending=False)
# print(data_frame)
# print(data_frame['rate'].mean())
# new_df = pd.concat([data_frame['rate'], data_frame['inverseRate']])
# print(new_df)
# print(new_df.corr())
data_frame.to_excel('conversion_rates.xlsx', 'conversion')

