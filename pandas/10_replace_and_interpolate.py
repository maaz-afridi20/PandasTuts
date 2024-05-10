"""
! Replacing Some Value

data.replace(valueToReplaced,desiredValue)
data.replace([1,2,3,4,5], 100)
"""

import pandas as pd

data = pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\smokinghealthcsv.csv",nrows=25)
fulldata = pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\smokinghealthcsv.csv")



data.replace(to_replace=234,value=100) 
"""
this will replace 234 with 100
if we want to replace any string we can also do that.
then we have to give the value in string like

data.replace(to_replace="diamond",value="python")
this will replace diamond with python
"""

data.replace([1,2,3,4,5], 100)
"""
this will replace all the indexes from 1 to 5 with 100
in indexes mein jo b value hain wo 100 say replace ho jaye gii. 
"""