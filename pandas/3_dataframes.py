"""
DaatFrame : is 2D data structure

"""
import pandas as pd

l = [1, 2, 3, 4, 5, 8]

var = pd.DataFrame(l)
print(var)
print(type(var))
"""
if we want to print some specific column then we can also mention the column name

var2 = pd.DataFrame(dic, columns=["column_name"])
this will only show the column that we give the name.

just like Series data structure we can also give our own index names.


dic = {"name":['khan','afridi','kadf','afa'], "age":[4,8,29,12], "sub":[1, 5, 99, 2]}
var2 = pd.DataFrame(dic, columns=['name','age'],index=['aa','bb','cc','dd'])
var2

this will print the columns name and age.
and their indexes number will be aa, bb, cc, dd and so on.
because we have mention it in index

we can also get value from some specific column and then the row.
like 

dic = {"name":['khan','afridi','kadf','afa'], "age":[4,8,29,12], "sub":[1, 5, 99, 2]}
var2 = pd.DataFrame(dic,index=['aa','bb','cc','dd'])
print(var2['name'][2])

so now this will give us only name column and then in name column it will only
give the index value of 2. 


we can have any thing like we have Series data structure in the values
we can put any thing and it will print in columns and rows.
just like this.

sr = {"s":pd.Series([1, 2, 3, 4]), "p":pd.Series([5,6,7,8])}
listy = pd.DataFrame(sr)
print(listy)

"""

