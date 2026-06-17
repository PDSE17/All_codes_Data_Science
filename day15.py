# day 15 code

# pandas 

# json file
import pandas as pd
df=pd.read_json(r"C:\Users\PRASANJEET DAS\Downloads\file1.json")
#data=df.to_dict(orient="records")# this will print the data in dictionary format in vs code terminal output 
# print(df)


# pandas methods

# head
# it gives the starting rows data
print(df.head(2)) # ---> gives the data of first two rows starting from zero
print(df.head(-3)) # ---> gives the data of rows removes the last three rows of data 

# tail 
# it gives the last rows data
import pandas as pd
df=pd.read_json(r"C:\Users\PRASANJEET DAS\Downloads\file1.json")
print(df.tail(2))
# gives the data of last two rows 
print(df.tail(-2))
# skips the first two data rows


# info
import pandas as pd
df=pd.read_json(r"C:\Users\PRASANJEET DAS\Downloads\file1.json")
print(df.info())


# describe
import pandas as pd
df=pd.read_json(r"C:\Users\PRASANJEET DAS\Downloads\file1.json")
print(df.describe())


# shape
import pandas as pd
df=pd.read_json(r"C:\Users\PRASANJEET DAS\Downloads\file1.json")
print(df.shape)


# null
import numpy as np
import pandas as pd
df=pd.read_json(r"C:\Users\PRASANJEET DAS\Downloads\file1.json")
df["salary"]=[100,200,300,400,np.nan]
print(df)


# rename
import pandas as pd
df=pd.read_json(r"C:\Users\PRASANJEET DAS\Downloads\file1.json")
df.rename(columns={"name":"student_name","roll no":"id"},inplace=True)
print(df)


# question
import pandas as pd
data = {
    "Emp_Id":[101,102,103,104,105,106],
    "Name":["Amit","Riya","raj","Sara","john","Neha"],
    "Department":["IT","HR","Finance","IT","Sales","HR"],
    "Salary":[50000,45000,60000,55000,48000,52000],
    "Experience":[2,3,5,4,1,3]
}
df=pd.DataFrame(data)
print(df.head()) #--> print all rows
print(df.head(2))
print(df.tail())
print(df.info())
print(df.describe())
df.rename(columns={"Name":"Ep_name"},inplace=True)
print(df)



# operations on column

import pandas as pd
data = {
    "Emp_Id":[101,102,103,104,105,106],
    "Name":["Amit","Riya","raj","Sara","john","Neha"],
    "Department":["IT","HR","Finance","IT","Sales","HR"],
    "Salary":[50000,45000,60000,55000,48000,52000],
    "Experience":[2,3,5,4,1,3]
}
df=pd.DataFrame(data)
# get single column data
print(df["Name"])


# add single column
# df["Marks"]=[100,99,94,100,89,100]
df["Marks"]=df["Salary"] / 2
print(df)
