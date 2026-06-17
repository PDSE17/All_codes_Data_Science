# day 14 code

# 1d
# example 1
import pandas as pd
l=[10,20,30]
df=pd.Series(data=l)
print(df)


# example 2
import pandas as pd
d={"name":"prasanjeet","age":"21","roll-no":639}
df=pd.Series(data=d,index=["name","age","roll-no"])
print(df)


# example 3
import pandas as pd
d={
    "name":["prasanjeet","vikram","nisha","pooja","mahesh"],"roll-no":[639,1,143,69,23]
}
df=pd.DataFrame(data=d)
print(df)


# csv 
import pandas as pd
df=pd.read_csv(r"C:\Users\PRASANJEET DAS\Downloads\file1.csv")
print(df)