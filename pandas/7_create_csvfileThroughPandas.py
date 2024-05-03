import pandas as pd

dis = {"a":[1,2,3,4,5],"b":[6,7,8,9,10],"c":[11,22,33,44,55]}
d = pd.DataFrame(dis)
print(d)
d.to_csv("filename.csv")

"""
tu in order to create a csv file from your data 
like k hm chahtay hain k jo data hmaray pass hai uss ki csv file 
bana lein tu humein 
jo data frame hogaaa jo yahan psrr d hai 
uss ka name lengay orr uss k baad .to_csv("fileNamve.csv")
tu yahan comman k andar hm jo b name likhengay wo humaray pass jo new csv file create
hogii uss ka name hogaaa... orr ye 
jahan prr jupiter notebook hogii waha prr hi ye jo new file create huee hai
waha prrr hogii ye file..


aaar hm koii specific jagah dena chahtay hain tu poori path deni hogiii...
just like below...
"""

d.to_csv("D:/assets/generaldata/created.csv")

"""
dis = {"a":[1,2,3,4,5],"b":[6,7,8,9,10],"c":[11,22,33,44,55],"d":['ali','khan','afridi','check','ufff']}
d = pd.DataFrame(dis)
d.to_csv("D:/assets/generaldata/mycreated.csv")

this will create mycreated csv file in the given folder...
"""

d.to_csv("D:/assets/generaldata/mycreated2.csv", index=False)

"""
jab hm direct koi file create krtay hain tu in ki values ki jo index values hoti hain
wo b aik row mein show krwata haiii tu
agar hmm nay yaha prr index=False kr diya tu matlab ye k
humein index number show krnay ki need nai hai
jo row numbers. hain wohi bss teek hain..
if we give another parameter [header]
throgh this it will change the name of the columns... according to our names...
d.to_csv("D:/assets/generaldata/mycreated2.csv", index=False, header=[names of columns])
but the number of columns must be same...
"""
