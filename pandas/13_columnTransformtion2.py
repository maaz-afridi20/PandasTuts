"""

names["bonus rupees"] = (names["salary"]/100)*20

ye names k data mein aik column create krega. bonus rupees k name say
orr jitni salary hogi
uss k base prr ye 20% discount add kr dega iss column mein.

"""
import pandas as pd
import numpy as np

fullhotel = pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\hotel_booking.csv")
names = pd.read_excel("D:\\assets\\generaldata\\names.xlsx")



# print(names)

data = {"months":['january','february','march','april']}
a = pd.DataFrame(data)


def myextract(value):
    return value[0:3]


a["short_month_names"] = a["months"].map(myextract)
print(a)


"""
ye ab ye karega k aik new column create karega shortmonthnames k name say orr uss mein hm nay ye 
condi lagai hai k "a" ka jo month column hai uss prr hm nay map lagaiii haii orr uss map
mein hm nay aik function ko refer kia hai orr wo function ye kaarm karega
k jo b value uss mein aye gii wo uss ki pahli ki 3 value ko humein dega.

tu map ka tu kaam ye hai k jo b cheez ho wo uss prr ietrate hota haii
tu wo jab hm nayu uss mein wo wala method put kr liyaaa tu wo month k column mein jitin b values hongi
sab prr lag jaye ga orr uss mein jo value hogi like month name uss k pahlay k 3 letters humein dedega..

"""