"""
in pandas we have
1D data which is called => series
2D => DataFrame
3D => PanelData


Series :
if we want to work with 1D data. in pandas we use Series.
"""

import pandas as pd

x = [1429, 2231, 3892, 4720]
a = pd.Series(x, index=['a', 'bb', 'ca', 'kk'], dtype='float', name='first')
print(a)

# we can also get the data through indexes.
print(a[3])

"""
we can also change the index number according to us.
like if we want the index to be  'a', 'b', or 'bb', 'afa', etc we can also do this.
now its index will be not number.
but that values which we have mentioned.
we can also change the data type. by  dtype function.
dtype='float' this will change data to float.
we can also give name to the dataset or data.
so that we can also what data we are talking about.
a = pd.Series(x, index=['a', 'bb', 'ca', 'kk'], dtype='float', name='seriessssdata')
so now if we run this we will also see the name  (seriessssdata).

intead of list we can pass dictionary, tuple etc any thing in this. 
"""

dic = {"name":['python','c++','java','c'], "por":[12, 43, 15, 18], "rank":[1, 4, 3, 2]}
varr = pd.Series(dic)
print(varr)

