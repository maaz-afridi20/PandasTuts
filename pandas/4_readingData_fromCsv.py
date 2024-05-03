"""
Reading Data From Csv.
pd.read_csv("filename")
nrows=5 => for number of rows
usecols=[column name or index] => for apni marzi k columns
skiprows=[row index] => this will skip that specific row which we specify here.
index_col=["columnname"] => iss mein hm jiss column ka name b dengay tu ye uss column mein
                            jo b values hongi uss ko rows ki number bana dega.. matlab k indexes.
header= any_value => ye jo hm header mein jo b value pass karengay tu wo ye karega k
                     iss mein jo b row mein data hogaa uss ko column k nae bana dega...
names=["columns names"] => iss mein hm jo b name dengay tu wo column k name ho jayengay...
header=none => this will remove the header. mean k iss k columns name delete ho jayengay.
dtype{"headingName":type} => for changing data type of some thing.

"""


import pandas as pd

"""
if we want to have some specific row then we can also use nrow attribute
like given below
if we give nrows = 4 now it will give us that much rows
like if we give nrows = 100 it will give us 100 rows. and so on.
"""
d3 = pd.read_csv("D:/assets/kaggledatasets/csv_of_that_zip_files/crudeoil.csv", nrows=4)
print(d3)


"""
if we want to get some specific column then we can use
"usecols" parameter
like given below.
"""

d3 = pd.read_csv("D:/assets/kaggledatasets/csv_of_that_zip_files/crudeoil.csv", usecols=['column name'])
print(d3)


"""
if do not know the name of the column specifically then we can also use 
the indexes number so this will give uss that columns. like given below.
now this will give us the column of 0 index, 5th index, 7th index and 3rd.
"""

d3 = pd.read_csv("D:/assets/kaggledatasets/csv_of_that_zip_files/crudeoil.csv",nrows=8, usecols=[0,5,7,3])
print(d3)


# for skipping rows.
d3 = pd.read_csv("D:/assets/kaggledatasets/csv_of_that_zip_files/crudeoil.csv",nrows=20,skiprows=[2])
print(d3)
"""
in skiprows if we want to skip some rows then we can use skiprows parameter and then pass that
index number of that rows which we want to skip.
this will skip that. rows.
"""

d3 = pd.read_csv("D:/assets/kaggledatasets/csv_of_that_zip_files/crudeoil.csv",nrows=10, index_col=[])
print(d3)


# header example..
d3 = pd.read_csv("D:/assets/kaggledatasets/csv_of_that_zip_files/crudeoil.csv",nrows=10,header=5)
d3

# this will change the names of columns to my give names.
# names example..
d3 = pd.read_csv("D:/assets/kaggledatasets/csv_of_that_zip_files/crudeoil.csv",nrows=10, names=["myyear","mymonth","myoriginname","origintype",'destinationname','destinationtype','grade','quantity'])
d3


# for changing data type.
d3 = pd.read_csv("D:/assets/kaggledatasets/csv_of_that_zip_files/crudeoil.csv",nrows=10, dtype={"month":float})
d3  # this will change the data type of month to float.
#  we have to pass it in dictionary.

