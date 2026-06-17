# day 20 code


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



# multi bar graph question
import numpy as np
import matplotlib.pyplot as plt # visualization
x =np.array([1,2,3,4])
y1 = [10,20,20,40]
y2 = [20,30,25,30]
y3 = [15,25,30,35]
# calculation of width
w = 0.25
plt.bar(x - w, y1,width=w,label="boys")
plt.bar(x ,y2, width=w,label="girls")
plt.bar(x +w, y3,width=w,label="others")
plt.xlabel("Groups")
plt.ylabel("Number of Students")
plt.title("No.of students in each group")
plt.legend()
plt.show()


# histrogram
import matplotlib.pyplot as plt
marks = [40,55,60,70,75,90,33,50]
plt.hist(marks,bins=2)
plt.show()



# pie chart
import matplotlib.pyplot as plt
fruits =["Apple","Banana","Orange","Watermelon"]
count = [40,24,32,33]
plt.pie(count,labels=fruits)
plt.show()



# percentage in pie chart
import matplotlib.pyplot as plt
fruits =["Apple","Banana","Orange","Watermelon"]
count = [40,24,32,33]
plt.pie(count,labels=fruits,startangle=90,autopct="%1.1f%%")
plt.show()



# subplots
import matplotlib.pyplot as plt
# first chart
x = [1,2,3,4,5]
y = [10,20,30,40,55]
plt.subplot(1,2,1) # row,cols,position
plt.plot(x,y)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()



# second chart
x1 = ["Apple","Banana","Orange","Watermelon"]
y1 = [40,30,15,70]

plt.subplot(1,2,2)
plt.pie(y1,labels=x1,startangle=90)
plt.xlabel("x1 axis")
plt.ylabel("y1 axis")
plt.tight_layout()


plt.show()



# question
# line chart of 4 different players 
import matplotlib.pyplot as plt

innings = [1,2,3,4]

runs1 = [45,78,120,150]
runs2 = [30,65,100,140]
runs3 = [55,85,110,170]
runs4 = [40,70,130,180]

plt.figure(figsize=(10,8))

# Plot 1
plt.subplot(2,2,1)
plt.plot(innings, runs1, marker='o')
plt.title("Player A")
plt.xlabel("Innings")
plt.ylabel("Runs")

# Plot 2
plt.subplot(2,2,2)
plt.plot(innings, runs2, marker='o')
plt.title("Player B")
plt.xlabel("Innings")
plt.ylabel("Runs")

# Plot 3
plt.subplot(2,2,3)
plt.plot(innings, runs3, marker='o')
plt.title("Player C")
plt.xlabel("Innings")
plt.ylabel("Runs")

# Plot 4
plt.subplot(2,2,4)
plt.plot(innings, runs4, marker='o')
plt.title("Player D")
plt.xlabel("Innings")
plt.ylabel("Runs")

plt.tight_layout()
plt.show()



# question
# 4 different charts of same player
import matplotlib.pyplot as plt
innings = [1,2,3,4,5]
runs = [45,78,32,95,60]

plt.figure(figsize=(10,8))

# 1. Line Graph
plt.subplot(2,2,1)
plt.plot(innings,runs, marker='o')
plt.title("Line Graph")
plt.xlabel("Innings")
plt.ylabel("Runs")

# 2. Bar Graph
plt.subplot(2,2,2)
plt.bar(innings,runs)
plt.title("Bar Graph")
plt.xlabel("Innings")
plt.ylabel("Runs")

# 3. Histogram
plt.subplot(2,2,3)
plt.hist(runs,bins=3)
plt.title("Histogram")
plt.xlabel("Runs")
plt.ylabel("Frequency")

# 4. Pie Chart
plt.subplot(2,2,4)
plt.pie(runs,
        labels=[f"I{i}" for i in innings],
        autopct="%1.1f%%")
plt.title("Runs Distribution")

plt.tight_layout()
plt.show()