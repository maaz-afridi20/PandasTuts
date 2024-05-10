"""
merge: to merge 2 or more dataframes
join: join work same as merge with some diff parameters.
concatenate: concatenate works same as merge

             but for contaenation the datatype must be same.

             concatenation ka matlab ye hai k ye aisa karega k
             2 dataframes ko concatinate kr dega matlab join kr lega
             magar aisa karega k for ex 
             aik df mein 10 rows hain orr secodn mein 5
             tu ye aisa karega k jab hm concatenate karein gay tu
             ye pahlay dataframe ki 10 values ko print kr lega orr
             uss k bad udd k neechay jo secnod df hai uss ki values 
             ko add kr lega tu difference siraf ye hai k jo concat mein jo b 
             data hota hai wo jab add ho jaye tu pahlay walay data k neechay
             second data ajata hai.. 


"""

import pandas as pd

data1 = {"empid":["emp1","emp2","emp3","emp4","emp5"],"names":["ali","max","warner","rohit","mohit"],"age":[32,53,24,93,32]}
data2 = {"empid":["emp1","emp2","emp3","emp4","emp5"],"salary":[10000,20000,30000,40000,50000]}


df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

"""
for example humaray pass ye data hai 2 data frames hain humein issay merge krna hai
tu hm .merge() say kr sktay hain.
merge krnay k liye koi aik aisa parameter compulsory hai k kiss base prr hm iss ko merge kr rahay hai
warna empty dataframe create ho jaye ga.
bss jo common hogi parameter wo merge ho jaye gii baki rah jayengi
like k agar hm ooper 2 data frames ko dhekein tu dono ki emp id sme hain tu hm 
.merge mein aik aisa parameter hai  (on) ... iss ka matlab k kiss base prr merge krna hai
tu hm uss ka use kr sktay hain... like...
"""

print(pd.merge(df1,df2),on="empid")

# ye dono dtaframes ko empid k base prr merge kr dega.

"""
iss mein humaray pass SQL ki tarah left and right and inner join ka concept b hai..
jaisa k agar hm chahein k leftjoin ho tu jo pahlay walay df yani k hm nay left(firstone) df1

ya zaroori nai hai k first one hi left ho.. agar hm meintion kar dein left right tu 
jo b value hm uss ko de dein tu wo let ya right hogi... as give below...

agar hm mention na karein left,right tu by default jo left prr likhi hogi wo
left consider ki jaye gi or jo right pr likhi hogi wo right.

likhaa hai tu uss ki sari values jo merged df hai uss mein sari hongi hi hongi 
or jo data dosray df mei nnai hoga wahan prr nan likh kr ajayega.
hm left or right mention kr sktay hain like.

uss k sath sath humein mention karna b parega k ab join krna konsa hai 
left krna hai ya right krnaa hai...
by default  join="inner" hota hai
iss ka matlab hai k jo dono dataframes mein common hain wo print kr lo...

"""

print(pd.merge(left= df1, right=df2,on="empid",how="left"))  # ab ye left join karega

print(pd.merge(left= df1, right=df2,on="empid",how="right"))  # ab ye right join karega



# JOIN
print(pd.join(df1,df2))

# CONCATENATION
print(pd.concat([df1,df2],ignore_index=True))
# 
