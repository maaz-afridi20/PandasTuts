"""
pivoting is use for reshaping the dataframe.

hm mention kr sktay  hain k index kia honi chahiyee orr 
column k names kia honay chahiyee..
or values kiaa honi chahiyee..


MELTING : melting hm tab use krtay hain k jaisay k aik data file 
          mein for example aik column mein sara column mein likha hoti hai
          k gender = Female
          like k agar iss mein 1000 rows hon uss saray rows mein 
          aik column hota hai gender = Female or Male 
          tu agar hm kuch aisa krna chahtay hain tu 
          hm melting ka use kr sktay hain... 


"""

import pandas as pd

dictt = {"keys":['k1','k2','k1','k2'],
         'names':["john",'ali','david','peter'],
         'houses':['red','blue','green','red'],
         'grades':['3rd','4th','5th','6th'],
        }
df = pd.DataFrame(dictt)

# print(df.pivot(index="keys",columns='names',values='houses'))



print(pd.melt(df, id_vars=["names"], value_vars=["houses"],var_name=["fkk"],value_name=["check"]))