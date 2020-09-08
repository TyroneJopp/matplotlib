import csv
import numpy as np
from matplotlib import pyplot as plt 


plt.style.use('seaborn-ticks')

with open('data.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)


	row = next(csv_reader)
	print(row['LanguagesWorkedWith'].split(';'))







# plt.xlabel('Ages')
# plt.ylabel('Median Salary (USD)')
# plt.title('Median Salay by (USD) by Age')

# plt.legend()



# # plt.grid(True) ## adds a grid to the graph

# plt.tight_layout() ## adds padding to your graph

# plt.show()