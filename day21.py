# day 21 code


# subplots
import matplotlib.pyplot as plt
# graph one data 
year = [2010,2015,2020,2025]
organics = [100,120,250,750]

# graph two data
year = [2010,2015,2020,2025]
farming = [150,220,280,650]

fig , aux = plt.subplots(1,2)

# 1st graph
aux[0].plot(year,organics)
aux[0].set_xlabel("year")
aux[0].set_ylabel("organics")
aux[0].set_title("organics production graph")

# 2nd graph
aux[1].plot(year,farming)
aux[1].set_xlabel("year")
aux[1].set_ylabel("farming")
aux[1].set_title("farming production graph")
plt.show()



# example 2
import matplotlib.pyplot as plt
# graph 1
year = [2010,2015,2020,2025]
dairy = [100,150,650,725]

# graph 2
farming = [300,350,450,550]

# graph 3
college = [10,20,25,30]

# graph 4
transport = [50,75,125,534]

fig, aux = plt.subplots(2,2)

# first row first col
aux[0][0].plot(year,dairy)
aux[0][0].set_xlabel("year")
aux[0][0].set_ylabel("dairy")
aux[0][0].set_title("dairy production graph")

# first row second col
aux[0][1].bar(year,farming)
aux[0][1].set_xlabel("year")
aux[0][1].set_ylabel("farming")
aux[0][1].set_title("farming production")
 
# second row first col
aux[1][0].pie(year,labels=college)
aux[1][0].set_xlabel("year")
aux[1][0].set_ylabel("college")
aux[1][0].set_title("college production")

# second row second col
aux[1][1].scatter(year,transport)
aux[1][1].set_xlabel("year")
aux[1][1].set_ylabel("transport")
aux[1][1].set_title("transport production")
 
 
plt.tight_layout()
plt.savefig("subplots.pdf")
plt.show()




# project 1
# numpy + pandas + matplotlib

import pandas as pd
import matplotlib.pyplot as plt
url ="https://raw.githubusercontent.com/rajendra0968jangid/Ds-arya/main/temperature_data.json"
df = pd.read_json(url)

# drop row 3 -> day = wednesday
df.dropna(subset=["temperature_c"],inplace=True)

# fill average value
df.fillna(df['humidity_pct'].mean(),inplace=True)
 
# new cols -> farenheit   | cell*1.8 -> + 32
df['temperature_f'] = (df['temperature_c'] * 1.8)+32

# subplots -> 1d -> line chart | pie chart
fig,aux = plt.subplots(1,2)
aux[0].plot(df["humidity_pct"],df["temperature_c"])
aux[0].set_xlabel("humidity")
aux[0].set_ylabel("temperature in celsius")
aux[0].set_title("humidity with celsius")
 
aux[1].pie(df["temperature_f"],labels=df["day"],autopct="%1.1f%%")
aux[1].set_title("humidity with farenheit")
 
# save image data
plt.savefig("project1.pdf")
plt.show()
 
