"""
Arithmetic Operations
we can do all arithmetic operations through pandas.

addition:
so if we want to add 2 columns then we have to save it in another column
so for this we do like this.

"""
import pandas as pd
df = pd.DataFrame({'a':[1,2,3,4],'b':[5,6,7,8]})
print(df)

df['c'] = df['a'] + df['b']
# this will add column a and b, and it will create another column c and will save it in.
print(df)

# we can also do subtraction
df['d'] = df['a'] - df['b']
print(df)

# multiplication...
df['d'] = df['a'] * df['b']  # this will multiply column a and b,
# and it will create another column d and will save it in.
print(df)


df['c/b'] = df['c'] / df['b']  # will divide c by b.
print(df)

"""
we can also do some more logical things like 
by giving some more conditions like given below
df2 = pd.DataFrame({'a':[20,41,13,34],'b':[5,6,7,8]})

df2["less"] = df2['a'] <= 20
print(df2)

so now this will create another column with name less and in that column
this will return true in that row in which the value in the 'a' column is less than or
equal t0 20, otherwise it will return false

this is another condition. 
df2['modulus'] = df2['b']%2==0
df2
"""
