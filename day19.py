# day 19 code


# create line chart
import matplotlib.pyplot as plt # visualization
x = [2010,2015,2020,2025]
y = [100,200,250,300]
plt.plot(x,y) # line graph
plt.xlabel("years")
plt.ylabel("sales")
plt.title("sales report")
plt.show() # to show the graph



# create line chart
import matplotlib.pyplot as plt # visualization
x = [2010,2015,2020,2025]
y = [100,200,250,300]

# size of graph
plt.figure(figsize=(6,4))
# 6 is width and 4 is height
plt.plot(x,y)
plt.show()



# customized line chart
import matplotlib.pyplot as plt # visualization
x = [2010,2015,2020,2025]
y = [100,200,250,300]
plt.plot(x,y,color="red",marker="o",linestyle="dashed",markersize=10)

plt.show()


# multiple line chart
import matplotlib.pyplot as plt # visualization
x = [2010,2015,2020,2025]
y1 = [100,200,260,290]
y2 = [150,185,195,300]

plt.plot(x,y1,label="jeans")
plt.plot(x,y2,label="shirt")
plt.legend()
plt.show()


# question 
import matplotlib.pyplot as plt
Subjects = ["Math","Physics","English","Hindi","Chemistry"]
Marks1 = [81,86,90,83,85]
Marks2 = [90,87,80,80,96]
plt.plot(Subjects,Marks1,color="green",marker="o",linestyle="dashed",markersize=8,label="12th")
plt.plot(Subjects,Marks2,color="blue",marker="o",markersize=8,label="10th")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Result")
plt.legend()
plt.show()


# Bar chart
import matplotlib.pyplot as plt
x = [2015,2020,2025,2030]
y = [100,150,200,290]
 
plt.bar(x,y)
# size
plt.figure(figsize=(4,2))
plt.show()
 


# multi bar graph
import numpy as np
import matplotlib.pyplot as plt # visualization
x =np.array([1,2,3,4])
y1 = [10,20,20,40]
y2 = [20,30,25,30]
# calculation of width
w = 0.40
plt.bar(x - w/2,y1,width=w,label="boys")
plt.bar(x + w/2,y2,width=w,label="girls")
plt.xlabel("Groups")
plt.ylabel("Number of Students")
plt.title("No.of students in each group")
plt.legend()
plt.show()


