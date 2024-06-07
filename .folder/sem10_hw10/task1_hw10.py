"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
"""
import pandas as pd
import random


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

print(data, end='\n\n')



#get_dummies
one_hot_data = pd.get_dummies(data['whoAmI'], dtype=int)

print(one_hot_data, end='\n\n')


#no get_dummies
one_hot_encoded_data = data.pivot_table(index=data.index, columns='whoAmI', aggfunc='size', fill_value=0)
one_hot_encoded_data.columns = one_hot_encoded_data.columns.set_names([None])

print(one_hot_encoded_data)
