"""
handling null values :

data.dropna() => will remove(drop,delete) that whole row in which there is null value
data.fillna() => will fill the null values.
"""
import pandas as pd
fulldata = pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\diamonds.csv")
print(fulldata)

fulldata.dropna(axis=1)  # now this will only delete all null values in columns.
# because axis=1 is showing column and axis=0 is showing row.
fulldata.dropna(how="all")  # ye how hm tub use karengay jab k aik full row ho orr full k full khali ho
# koi aik value b na ho uss mein full row khali ho ye wo wali row ko delete kr dega.
# magar jo baki k na hon wo baki presnt hongay
# siraf wo full row delete ho jaye gii jofull khali hai..

fulldata.dropna(subset=["column_name"])
"""
so jo ye subset ka parameter haii ye, ye karega k for example jab hm axis=1
tu uss mein agar full column mein koii aik value b null ho tu sara ka sara
full column delete ho jta hai.
magar agar hm ye subset mein column name mention kar dein tu ye wo column say null values
delete karega magar siraf wo values delete kar dega jiss mein null ho
full row b uss k sth deletr kr dega.
"""

fulldata.dropna(thresh=1)
"""
jab ham thresh parameter ko use krtay hain iss ka matlab ye hai k uss column say na value ko
remove karo jiss column mein siraf aik hii null value ho
or baki jo columns mein null value ho uss ko rahnay do..
hm 1 ki jagah koii b value de sktay hain.. depending on our need.
"""

fulldata.fillna()