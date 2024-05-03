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