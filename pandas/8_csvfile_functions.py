"""
functions that we can apply on csv file.


data = pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\hotel_booking.csv",nrows=20, usecols=[0,1,2,3,4,5])

data.index => this will show details about index
data.columns => will show all the columns names
data.describe() => will give you min, max, mean, percentage of the numerical values of all columns.
data.head() => by default it will show only starting 5 datas.
               if we give any value inside head(any value) this will show you that number of datas.
data.tail() => same logic, but it will show you last wala data.
data.isnull() => will show true where there is null values, otherwise false.
data.isnull().sum() => will sum all the null values.
data[0:2] => this will print rows that how much we want. here we mentioned from 0 to 2
             so this will print that number of rows.
             so just like slicing we can give any range of data.
data["colum name"] => we can also give specific column name it will show that column.


we can change data frame from data frame to simple array.
we can also change data frame from data frame from numpy array.

data.index.array => will change dataframe to array.
data.to_numpy() => will change dataframe to numpy array
data.sort_index(axis=0, ascending=False)  => will sort data in descending order
                                             we also have to mention axis which mean that which we want to
                                             like row or column in descending order.
data["is_canceled"][5] = 1  => this will change the data in column "is_canceled"
                               and the index 5, value to 1
what type of data is inside "is_canceled" and index5 that value will be changed to 1 or anything
we want like
data["is_canceled"][5] = "fuckkkkk"

there is another method for this
data.loc[0,"columnName"] = "maaz"  => now this will also change value of 0 index and any specific name
                                      of column to any value we want... like eg below.
data.loc[0,"lead_time"] = 88


data.loc[[1,2],["is_canceled","lead_time"]] => this will only give the 1st and 2nd row and only the specific
                                               two mentioned columns.


data.drop(rowName_or_columnName, axis) => this will delete that row or column which we spcify.
data.drop("is_canceled", axis=1) => this will delete is_canceled column.

"""
import pandas as pd

data = pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\hotel_booking.csv",nrows=20, usecols=[0,1,2,3,4,5])
print(data)

data.loc[0, "lead_time"] = 88

"""
we can change data frame from data frame to simple array.
we can also change data frame from data frame from numpy array.
"""