"""
handling null values :

data.dropna() => will remove(drop,delete) that whole row in which there is null value
data.fillna() => will fill the null values.


!Parameters of them 
dropna(axis=1)
dropna(how="all")
dropna(subset=["column_name"])
dropna(thresh=1)



fulldata.fillna(method="bfill")
fulldata.fillna(method="ffill")
fulldata.fillna(method="ffill",axis=1)
fulldata.fillna(anyvalue,inplce=True)
fulldata.fillna("asli",limit=2)
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

"""
agar hm chahtay hain k kisi specific column ki null value mein koii specific add karein tu 
humein dictionary ko pass krna parega... or uss mein column ka name and wo specific value
b deni paregi  like 

data.fillna({"price":4290, "y":"patanai"})

so ye jo hai price k column mein jo b null value hogi uss ko 4290 say fill kr dega or y column mein jo b 
null values hogi uss ko "patanai" say fill kr dega.
"""

fulldata.fillna(method="bfill")
fulldata.fillna(method="ffill")

"""
ye bfill or ffill ka methlab ye hai k jo ooper walay methods hain uss mein jo b
null value hoti hain uss mein wo specific value chali jaye gi 
magar iss say accuracy naii ati qk 
agar koii value int hogi orr hm uss mein fillna karein orr koii string dal dein tu 
ye tu ghalat hai tu 
ye ffill and bfill ye karega k 
ffill => ye jo b row mein NA value hai uss ko kahega k aap say ooper walay row mein jo value 
hai uss ko idhar b daal dein tu kam say kam iss say thori accuracy ajaye gii

bfill => isse tarah logic iss ki b hai magar ye neechay walay row say uss
null ko fill kr dega.


agar hm axis na dein tu ye bydefault neechay, ya ooper walay row day data ko copykr lega.
magar agar hm chahtay hain k ffill and bfill k logic ko use krtay hue 
hm right ya left column ko use kein uss null value ko fill krein tu hm axis dy sktay hain...
like


data.fillna(method="ffill",axis=1) or data.fillna(method="ffill",axis=0) 
"""

fulldata.fillna(32,inplce=True)  

"""
ye inplace ye karega. k jahan prr b null value ho uss ko 32 say fill kardegaa...
magar iss ko iss file mein nai aik new file mein changes ko save kr lega.
"""

fulldata.fillna("asli",limit=2)

"""
ye limit ye karega k aik clumn mein for example 10 na values hain orr hm nay limit laga di 2
tu ye karega k jo starting ki 2 Na values hongay us ko fill kar dega "asli" say baki ko chor dega.
ye value ki hm koi b value de sktay hain jo humein put krni ho.
orr limit b apni custom de sktay hain. 
"""