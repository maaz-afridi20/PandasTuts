"""
if we want to compare 2 data frame we can use compare method 
in which we can compare data frame that what's are differences like 
k agar humaray pass 1 dataframe hai pichlay year ka us mein salary hai 
orr abi aik orr dataframe hai iss year ka 
hm iss ko compare kr sktay hain k for example k iss sal ki salary mein and pichlay saal ki 
salary mein kiaa koii differences hain ya nai................................................................ 


print(df1.compare(df2))


this will compare df1, with df2 tu ye humein changes bata dega k kiaa 
kiaa changes aye hain kin column mein 
orr ye b prnit kr dega k pahlay kia value thi orr ab kia value hai..

we also have some parameters... given below.


=>    print(df1.compare(df2,align_axis=1))
=>    print(df1.compare(df2,keep_shape=True))  iss ka mean hai k jo changes aye hain wo b print
                                               krwa do orr jo changes nai hain wo b print krwa do
                                               ye wo jo chanes nai aye hain uss ki jagah ye nan print
                                               krwa dega matlab ye k yahan prrr koii b changes nai ayee..
                                               
                                               agar hm iss ko False rahnay dein tu ye siraf wo values
                                               dhikaye gaa jiss mein koii changes aye hon...
                                               by default False hi hota. hai
=>    print(df1.compare(df2,keep_shape=True))                                            


"""
import pandas as pd


dictt = {"fruits":["banana",'apple','kiwi','mango'],
         "price":[100,32,200,500],
         "quantity":[12,3,5,100]}
df1 = pd.DataFrame(dictt)


df2 = df1.copy()  # ye automatically df1 ka sub kuch copy kr lega orr df2 mein ajaye ga.

print()
print(df1)
print()
print(df2)

print('-----------------------------------------------------')
df2.loc[0, "price"] = 120
df2.loc[1,"price"] = 110
df2.loc[3,"price"]  = 2000

df2.loc[0, "quantity"] = 8
df2.loc[1,"quantity"] = 5
df2.loc[3,"quantity"]  = 105


print('-----------------------------------------------------')
print()
print(df1)
print()
print(df2)

print("now comparing...")

print(df1.compare(df2))



print(df1.compare(df2,align_axis=1))