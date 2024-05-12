"""
Scatter plot :

mainly we need only 2 parameters x and y

plt.scatter(xValue,yValue)


plt.scatter(x,y,s=10)  will change sizes of that dots.

msizes = [10,8,9,12,5,9]
plt.scatter(x,y,s=msizes) by this all the dots will have different sizes


plt.scatter(x,y,alphe=0.5) will change the transparencey of dots.

plt.scatter(x,y,marker="*") this will change that dot to star... we can also give any other.. we want
                            we can give any thing we want like ^ and , and so on 


plt.scatter(x,y,marker="*",edgecolor='black') ye jo b marker hm nay add kiyaa hai uss k boundry color hoga.
plt.scatter(x,y,marker="^",linewidth=3) ye jo b edge hogaa uss ki width


plt.colorbar() agar hm ye add kar lein tu side prr aik color ki baar show hogi from 0 to 1




agar hm koii specific value nai dena chahtay like green, red blue etc
tu hm koii hex tyype ki values b dy sktay hain magar uss ki value siraf 1 to 100 
k beech mein hogi..
uss k baad 'cmap' ki property hm use karengay iss ka matlab hai color map
tu iss mein hm mention karengay k konsa use karana haii..
is cmap mein just like flutter theme ki tarah hai is mein agar hm siraf aik 
name de dein tu ye khud saray dots ka color decied karega...
tu example given below................................................................
x = [1,2,3,4,5,10]
y = [4,2,6,8,7,8]
mmcolors = [40,57,88,91,40,29]
msizes = [50,80,90,29,50,90]

plt.scatter(x,y,c=mmcolors, cmap="afmhot")

ye jo hm nay afmhot use kiyaa ye wo color k theme ka name hai... ye bohay say hain hm jo b use karein 
like 
set1,set2,set3,spring,wistia,yign,autumn,bone,brg,binary,BrBG 
and many moreee.... ye bohat zyada hain
iss mein kuch words capital and small b hain search it. 
magar iss k sath humein value zaroor mention karni hogii c(color) k parameter mein jaisa k 
ooper mention hai...


hm nay jo colorbar use kiyaa hai ye optional hai.. 
iss k apnay b kuch parameters hain for eg agar iss mein label likhna ho
like 
plt.colorbar().set_label("my colorlabel")  iss say label ajaye ga colorbar ka
plt.colorbar().set_label("my colorlabel",fontsize=20) iss say fontsize change hogi label ki


"""

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [4,2,6,8,7]
myc = ['yellow','green','red','orange','blue']

# plt.scatter(x,y,c='green')  # color will change the color of that dots.
plt.scatter(x,y,c=myc,s=10, marker="*")  # by this all the dots will have diff colors.
plt.title("my Scatter plot...",fontsize=16,color='r')
plt.xlabel('my x label',fontsize=16,color='orange')
plt.ylabel('my y label',fontsize=16,color='blue')

plt.show()