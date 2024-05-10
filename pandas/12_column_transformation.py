"""
names["full name"] = names["first_name"].str.capatilize() + " " + names["last_name"]
.loc[] => ye jo .loc hm use krtay hain tu ye hm kisi b value uss say find kr sktay hain like k
          agar hm likhein aisya lesssmoking.loc[0,"heart_rate"] tu ye humein exact value de dega
          k jo column heart_rate and uss k 0 index prr jo value hai wo humein print kr dega.

          agar hm column name mein koii aise value likh lein jo column na ho data mein
          tu error dega... magar agar hm koii uss k samnay aik value likh lein  jaisa k given below

          lesssmoking.loc[0,"abc"] = 10

          tu iss ka matlab hai k aik new column create kare "abc" say orr uss k samnay 10 put kr lo
          0 index pr.

          tu iss example aik neechay b given hai..


lesssmoking.loc[(lesssmoking["heart_rate"] > 85), "high_heart_rate"] = "yes"
lesssmoking.loc[(lesssmoking["heart_rate"]<85), "high_heart_rate"] = "no"

ye ho hai lesssmokig k data mein check karega k jo column "heart_rate"
ka haii uss mein jo value 85 say kam hain tu ye side pr aik orr new
colum create karega "high_heart_rate" k name say  orr uss mein us k samnay print kr dega yes
k jiss ka heart_rate zyada hai 85 say
orr agar kam hai tu no likh lega.


this is another example...


lesssmoking.loc[(lesssmoking["chol"] > 180), "chol_check"] = "high chol"
lesssmoking.loc[(lesssmoking["chol"]) < 180 , "chol_check"] = "normal chol"
lesssmoking.loc[(lesssmoking["chol"]) == 0 , "chol_check"] = "dead"

this will create a column k jiss ka chol 180 say greater hai tu aik new column create ho jaye ga
orr wahan prr high chol likh diya jaye ga.
orr jahan less than 180 ho wahan pr normal chol ajaye ga. orr agar 0 ho tu dead likh diya jaye ga.




names["full name"] = names["first_name"] + " " + names["last_name"]
print(names)

this will add first name and the last name and will create new column full name
and put them in it.

"""


import pandas as pd

names = pd.read_excel("D:\\assets\\generaldata\\names.xlsx")
fullhotel = pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\hotel_booking.csv")
lesshotel = pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\hotel_booking.csv",nrows=30)
fullsmoking = pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\smokinghealthcsv.csv")
lesssmoking = pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\smokinghealthcsv.csv",nrows=30)
fulloil=pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\crudeoil.csv")
lessoil=pd.read_csv("D:\\assets\\kaggledatasets\\csv_of_that_zip_files\\crudeoil.csv",nrows=30)


lesssmoking.loc[(lesssmoking["heart_rate"] < 80), "low_heart_rate"] = "yes"
