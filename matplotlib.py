'''
basic structure of matplotlib
-----------------------------
--> figure
-->axes
-->axis
--> grid
-->title
-->legend
'''

import matplotlib.pyplot as plt
subjects = ['python','java','c']
students = [35,7,15]
plt.pie(students,labels=subjects, autopct ='%1.1f%%')
plt.legend(subjects)
plt.title('students in courses')
plt.show()

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y =[10,15,18,20,13]
plt.scatter(x,y)
plt.xlabel('x value')
plt.ylabel('y value')
plt.show()


import matplotlib.pyplot as plt
y =[10,15,18,20,13]
plt.hist(y)
plt.title('histogram plot')
plt.xlabel('x value')
plt.ylabel('y value')
plt.show()



import matplotlib.pyplot as plt

x=[2010,2011,2012,2013,2014,2015]
y=[522,324,649,670,460,300]
plt.bar(x,y)
plt.title('toyata company sales')
plt.xlabel('years')
plt.ylabel('sales')
plt.show()

companis =['totaya','tata','mg','BMw']
sales =[200,230,304,287]
plt.pie(sales,labels=companis,autopct = '%1.1f%%')
plt.legend(companis)
plt.title("companis sales of 2026")
plt.show()
