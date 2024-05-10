"""
data.groupby()
with the help of groupby we can create a summary of any data we want.

if we want to group data by something then we can use this group by meth0d.

tu yahan prr hm groupby ki help say hm min,max,mean(avg),count,sum etc 
sari cheezain hm groupby ki help say orr phir agg ki help say kr sktay hain...


gp2 = fullhotel.groupby("country").agg({"is_canceled":"count"})

tu for example ye ye karega k hm nay aik variable gp2 banaya..
uss main hm nay fullhotel dataset liyaa orr uss mein
groupby() ko liyaa uss mein nay iss data ko group kiyaa country k base prrr..
tu country k base prr hm nay group kiyaa uss k baad hm nay 
.agg ka function use kiyaa iss ka matlab hai k humein aggrigate bataoo...
iss agg mein nay jiss column ka aggrigate janna chahtay hain uss ka name diyaa
orr agary "count" likh diya ye ye aik method hai orr ye uss ko count kr lega orr print kr lega.



gp3 = fullhotel.groupby("market_segment").agg({"country":"count"})
aa = fullsmoking.groupby(["chol","age"]).agg({"sex":"count"})
we can also pass 2 parameter in groupby 
and so on...


kk = fulldiamonds.groupby(["cut","price"]).agg({"depth":["min","max"]})
kk

more parameters in agg functions.... 



kk = fulldiamonds.groupby(["cut"]).agg({"carat":"count"})
kk
"""

import pandas as pd


fullhotel = pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\hotel_booking.csv")
lesshotel = pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\hotel_booking.csv",nrows=30)
fullsmoking = pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\smokinghealthcsv.csv")
lesssmoking = pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\smokinghealthcsv.csv",nrows=30)
fulloil=pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\crudeoil.csv")
fulldiamonds=pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\diamonds.csv")



print(fulldiamonds.head(20))
kk = fulldiamonds.groupby(["price","carat"]).agg({"clarity":"count"})
print(kk.head(20))


kk = fulldiamonds.groupby(["cut","color"]).agg({"carat":"count"})
print(kk)


"""
 this will find the mean of quantity goupedby originName
 ye aisa karega k fulloil mein saray countries ko together karega

 """
gg = fulloil.groupby("originName").agg({"quantity":"mean"})
gg