# day 18 code


# question 1
import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
# entering nan value in this code
# df.loc[4,"marks"] = np.nan

print(df.isnull())
print(df)

# column count sum
print(df.isnull().sum())

# drop null values by row
print(df.dropna())

# drop null values by cols
print(df.dropna(axis=1))

# fill by zero
print(df.fillna(0))

# fill by 100
print(df.fillna(100))


# question 2
# fill roll no by 200
# fill marks by 100

import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df["marks"] = df["marks"].fillna(100)
df["roll no"] = df["roll no"].fillna(200)
print(df)

# question 3
import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
print(df["marks"].mean())

df["marks"] = df["marks"].fillna(df["marks"].mean())

print(df)
# find mean then filled nan values with average


# aggregation
import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)

print(df["marks"].agg([sum,min,max]))


# concatenate
import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df1 = pd.read_json(url)

print(pd.concat([df,df1]))

# by cols
import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df1 = pd.read_json(url)
# question 
df1.loc[2,"name"] = "prasanjeet"
print(pd.concat([df,df1],axis=1))

import matplotlib.pyplot as plt
score = [10,20,30,40]
over = [1,2,3,4]
plt.plot(score,over)

plt.show()