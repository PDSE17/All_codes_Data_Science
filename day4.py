# day 4 code

# functions
# block of statement it executes whenever it is called
# declared by using def 
# argument---> def hello(a)
# parameter---> hello (10)


# function example 1
def hello():
    print("hello function is working ")
hello()    


# example 2
def hello1(a):
    print(a)
hello1(100)


# example 3
def add(a,b):
    print(a + b)
add(10,5)    


# example 4 
def add(a=2,b=3): #default value
    print(a + b)
add()


#example 5
def power(a,b):
    print(a**b)

power(5,2)
power(2,5)
power(b=5,a=2)
power(a=2,b=5)


#example 6
def student(*a):
    print(a)
    print(type(a))
    print(a[0])

student(1,2,3,4,5,6)

def student(a,b):
    print(a,b)

# student(1,2,3,4,5,6)
student(10,20)        



# question
def marks(a):
    for i in a:
     print(i)

marks([10,20,30,40,50])    



# question
def address(a):
    for i in a:
     for j in i:
      print(j)


address(["hello","prasanjeet"])



# example 7
def add():
  print() 


# lambda function
add =lambda x:x
print(add(100))   

sum=lambda x,y: x+y
print(sum(10,20))


a=lambda  x:x
print((a[10,20,30,40]))




# list comprehensions
print([i for i in range(5)])

# example
l=[10,20,30,40,50,60]
print([l[i] for i in range(len(l))])


# question
l=[10,20,[30,40,50,60]]
print([l[2][i] for i in range(len(l[2]))])



# list
l=[10,20,30]
print(l)

print(len(l))

l.append(40) # used to add at last
print(l)

l.insert(1,11) # used to add at specific position
print(l)



#example of append
l=["hello","prasanjeet","python"]
l.append("IIT kukas")
print(l)
print(l[0])
print(l[1])
print(l[2])
print(l[-1])


#example of insert
l=[True,False,10,20]
l.insert(1,10)
print(l)



#question
l=[10,20,30,{"name":"prasanjeet","address":["jaipur","kukas","bihar","vizag"]}]
print(l)
print(l[0])
print(l[1])
print(l[2])
print(l[3]["address"][2])
for i in l[-1]["address"]:
   print(i)


#question
l=[10,20,30,[40,50,[60,70,80]]]
print(l[3][0])  
print(l[3][1]) 




# dictionary
d={"name":"prasanjeet"}
print(d["name"])
print(d.keys())
print(d.values())





address={"Message":"Number of Post office(s) found: 12","Status":"Success","PostOffice":[{"Name":"Belan Bazar",
                                                                                          "Description":"","BranchType":"Sub Post Office",
                                                                                          "DeliveryStatus":"Non-Delivery","Taluk":"Munger","Circle":"Munger",
                                                                                          "District":"Munger","Division":"Monghyr","Region":"Patna HQ",
                                                                                          "State":"Bihar","Country":"India"}]}

for i in address["PostOffice"]:
    print(i["Name"])
    print(i["Taluk"])
    print(i["Circle"])
    print(i["District"])
    print(i["Division"])
    print(i["Region"])
    print(i["State"])
    print(i["Country"])
    print("\n")
