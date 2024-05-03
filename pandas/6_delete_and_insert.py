"""
Deleting and Inserting Data. :

"""

import pandas as pd

var = pd.DataFrame({"a":[1,2,3,4,5],"b":[9,6,7,8,10]})

var.insert(1, "c", var['a'])
print(var)

"""
so for inserting data in some thing it has 2 parameters.
pahla parameter hai k humain data insert kahan krna hai matlab column ka index number
tu ham nay diya hai 1. matlab k a and b k beech mein ban jaye ga.
uss k baad hm nay name dena hai column ka tu ham nay diyaa hai "c"
uss k baad humein dena haii k column mein hoga kiaa. matalab k data.
tu ham nay yaha par 'a' column ko hi copy kr diya 
matlab k bss jo 'a' mein ho data wohi ho c mein b.


hmm iss tarah b krr sktay hain k koii orr data b put krr sktay hain
like

mydata = ['a','b','c','d','e']

var.insert(2,"New Data",mydata)
tu ab ye jo new column banaega..
ye 2 index prr banay ga iss ka name hoga 'new data' orr jo third parameter, mean k data aana kahan say
haii hum nay waha prr mydata variable put krr diyaa matlab k iss mein jo data hai 
tu wo jo new data ka column banega uss mein ajaye ga.

data must of b same length. warna error aye. ga
"""


# if we want to load some minimum data like k kuch conditions
# laga kar minimun data ley ayein tu hm ye b kr sktay hain...
# like
"""
tu uss k liye humein same logic banani hogi k aik new variable create krna hoga.
qk agar new daat chahiyee tu kahin prr tu show hoga.

tu agar koii thora data chahiyee matlab k km data chahiyee tu hm wohi
slicing ko use karengay jaisay k list mein use ki thii..
like given belos.

var['min data'] = var['a'][:2]
tu ab ye jo haii ye aik new column banayee ga.. named 'min data'
uss mein jo a column ka data wo sara copy kr lega magar siraf 0 index say lekar 2 tk
"""

var = pd.DataFrame({"a":[1,2,3,4,5],"b":[9,6,7,8,10]})
var['min data'] = var['a'][:3]
print(var)

# deleting data...


"""
there is 2 methods of deleting data...
pop keyword : var.pop("b") this will delete column b 
del keyword : del var['a'] this will delete column a
with the help of pop we can delete any data.
so in pop we have to give the name of the column which we want to delete.
like in this we had given the name of column 'b' so this will delete 'b'
"""

var.pop("b")
print(var)

del var['a']
print(var)

