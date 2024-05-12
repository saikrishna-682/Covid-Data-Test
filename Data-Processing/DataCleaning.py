import pandas as pd
import numpy as np

csv_file_path = '/Users/saikrishnasomavarapu/Documents/pycharm-projects/C-19-Project-WHO/Project-WHO/data/WHO-COVID-19-global-data.csv'
csv_cc_path = '/Users/saikrishnasomavarapu/Documents/pycharm-projects/C-19-Project-WHO/Project-WHO/data/Country_Codes.csv'

'''Reading the csv file and finding the null values using numpy and replacing them based on their data type'''
data = pd.read_csv(csv_file_path, parse_dates=['Date_reported'])
data.replace('', np.nan_to_num, inplace=True)
'''Filtering the numeric value columns and filling the null values with 0'''
numeric_cols = ['New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths']
data[numeric_cols] = data[numeric_cols].fillna(0)

'''this returns the number of columns having null rows'''

'''null_columns = data.isnull().sum()

for column, count in null_columns.items():
    print(f"{column} has {count} null values")'''

# print(data.dtypes)
'''Finding unique values in the dataset '''
# print(data.head())
'''for columns in data.columns:
    print(data[columns].unique())'''

# print(data['Country_code'].unique())

''' Filtering data based on Country codes'''
unique_cc = data['Country_code'].unique()
# print(unique_cc)
unique_cc_data = pd.DataFrame({'CC': unique_cc})

output_CC = 'data/Country_Codes.csv'
unique_cc_data.to_csv(output_CC, index=False)
print(f"Successfully stored Country Codes to this location : {output_CC}")

cc = pd.read_csv(csv_cc_path)
# print(cc.head())
'''Writing files based on Country codes'''

'''for country_data in unique_cc:
    country_cc = data[data['Country_code'] == country_data]
    output_file = f'Data_CC/{country_data}.csv'
    country_cc.to_csv(output_file,index=False)'''


'''Filtering data on a condition where if all the numeric columns are euqal to 0 then drop all those rows and save 
that data into different folder bases on country codes'''
mask = data[numeric_cols].apply(lambda x: all(x == 0), axis=1)
data_empty = data[mask]
data_filtered = data[~mask]

'''for cc in unique_cc:
    filtered_data = data_filtered[data_filtered['Country_code'] == cc]
    filter_output = f'Data_Empty/{cc}.csv'
    filtered_data.to_csv(filter_output, index=False)'''

