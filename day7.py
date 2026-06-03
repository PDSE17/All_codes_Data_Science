# day 7 code


# oops concept 
# example 1
class prasanjeet:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)

p=prasanjeet("hello python")
p.show()        



 # __init__   this is constructor

  #  def __init__(self,name):
   #     self.name=name


# example 2 
class prasanjeet:
    def __init__(self):
        print("calling constructor ")


    def show(self):
        print("show the name: ")

p=prasanjeet()
p.show()        


# example 3
class prasanjeet:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getage(self):
        print("my age is: ",self.age)

    def getname(self):
        print("my name is: ",self.name)

p=prasanjeet("prasanjeet",20)
p.getage()
p.getname()             
        

# method 2 
p=prasanjeet(age=20,name="prasanjeet")
p.getage()
p.getname()  



# example 4
class prasanjeet:
    def __init__(self,*args):
        print(type(args))
        print(args)
        self.name=args[0]

    def getprasanjeet(self):
        print(" the student is: ",self.name)
        return self.name

p=prasanjeet("prasanjeet",20,"9661956103","prasanjeetdasclass11@gmail.com")
t=p.getprasanjeet()
print(t)        



# example 5
class student:
    def __init__(self,*args):
        self.data=args
    def users(self):   
     print(self.data[0])

    def details(self):
        print(self.data[1])
        
        
s=student(["prasanjeet","rohit","vivek","pramveer"],{"address":"bihar","college":"IIT kukas","loc":"jaipur"})   
s.details()



#example 6
self={"fullname":"prasanjeet das"}
# self.fullname="prasanjeet das"

class prasanjeet:
    def __init__(self,name,age):
        self.fullname=name
        self.age=age

    def getage(self):
        print("my age is: ",self.age)

    def getname(self):
        print("my name is: ",self.fullname)

p=prasanjeet(age=20,name="prasanjeet")
p.getname()
p.getage()            
        

# example 7
self={"name":{"name":"prasanjeet","age":20}}
self["name"]["name"]
class student:
    def __init__(self,args):
        print(type(args))
        print(args)
        self.name=args

    def getstu(self):
        print("the student is: ",self.name)
        return self.name

    s=student({"name":"prasanjeet","age":20})
    t=s.getstu()
    print(t["age"])    
                




