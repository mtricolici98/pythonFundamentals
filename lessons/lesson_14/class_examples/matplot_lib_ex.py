import pandas as pd
import matplotlib.pyplot as plt

employees = pd.read_json('employee_list.json')
average_by_position = employees.groupby('position').mean()
print(average_by_position)
average_by_position.plot(kind='bar', )
plt.savefig('example.png')
