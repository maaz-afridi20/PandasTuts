"""
to create bar plot we have to use
.bar(xAxisData, yAxisData)


Parateters :

plt.xlabel("anyValue")
plt.ylabel('anyvalue')
plt.bar(x,y,color='g',width=0.4)  width will change width of stick and color will change color of stick
plt.xlabel("anyValue",fontsize=10) fontsize will change fontsize of text.
plt.title("languages famousity",fontsize=15,color='yellow') color will change color of text


we can also give multiple colors to sticks.
we have to give list of that colors. like

colorss = ['green','yellow','blue','orange']
plt.bar(x,y,width=0.4,color=colorss)
plt.bar(x,y,width=0.5,align='edge') this will align the text below the stick
                                    align has 2 values one is edge and one is center
                                    we can use any of them.

plt.bar(x,y,width=0.5,edgecolor='black') it will have a border around that stick with black color.
plt.bar(x,y,width=0.5,edgecolor='black',linewidth=8) linewidth will thick or thin that border
plt.bar(x,y,width=0.5,edgecolor='black',linewidth=8,linestyle=':') linestyle will change the style of that
line arround the stick linestyle has many style we can use any value like : - -- -.
it will change the style of that line around stick
plt.bar(x,y,alpha=0.4) alpha will change the color intensity.
it's intensity is between 0.1 to 1

plt.bar(x,y, label="abccc") ye label aik chota sa label hoga ye graph k jo sticks hain un k ooper.
                            magar ye label ko show krnay k liye aik orr parameter ko b use krna parega
                            plt.legend() ye jab hm type kr lengay phirr ye show ho jaye ga. 


we can show multiple bar graph in single chart like 



for horizontal bar graphs.


"""

import matplotlib.pyplot as plt


x =['python','c','c++','java']
y = [80,70,60,82]

plt.bar(x,y,color='g',width=0.4)
plt.xlabel("abc",fontsize=10,color='yellow')
plt.ylabel("def")
plt.bar(x,y,width=0.5,align='edge')

plt.bar(x,y,width=0.5,edgecolor='black',linewidth=8)
plt.bar(x,y,width=0.5,edgecolor='black',linewidth=8,linestyle=':')

plt.legend()
plt.show()