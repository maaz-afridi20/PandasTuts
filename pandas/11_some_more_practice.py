"""

data.info()  => give you info about dataset
data.describe() => 
data.isnull() => show you null data
data.isnull().sum() => will count that null
data.duplicated("columnName") => show you true or false when duplicate dtta is here.
data.drop_duplicated(columnName) => will drop all duplicates values.


data.replace(valueToReplace, desiredValue)


data.fillna() => for filling something inside null value
"""

import pandas as pd
import numpy as np

data = pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\smokinghealthcsv.csv",nrows=25)
fulldata = pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\smokinghealthcsv.csv")


print(data.isnull().sum())
print(data.duplicated().sum())

"""
duplicate wahan pr acha use hota hai k jaisay ab koi id card ka number ho
uss mein humein maloom krna hai k koi duplicate tu nai hai
qk id card number mein dupilcate hona error hai qk id tu unique hoti hai tu 
tu aisay cndition mein zyada useful hota hai. warna use tu har jagah kr sktay hain.
"""

data.replace(np.nan, "afdaf"),  # ye ab jahan prr b nan ki value hogi wahan prr afdaf ko replace kr dega 
# jahan prr b nan hogi.. yahan hm jo value b dena chahain dy sktay hain........
data.replace(np.nan, 7839)   # and so on..

"""
agar hm specifically chahtay hain k koii colum mein data ko replace krein tu wo b kr
sktay hain..

tu ab ye jaye gaa siraf salary walay column mein orr wahan dhekega k jo 
Nan han un ko in say replace kr dega orr baki sb ko chor dega.
"""
data["salary"] = data["salary"].replace(np.nan, 89283)



data.fillna()