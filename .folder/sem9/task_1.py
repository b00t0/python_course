"""
1. Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы
"""

from pandas import read_csv

#1. Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
data = read_csv("california_housing_test.csv")

#2. Посмотреть сколько в нем строк и столбцов
print(data.shape)

print(data)

#3. Определить какой тип данных имеют столбцы
print(data.dtypes)

print(data.info())

print(data.describe())