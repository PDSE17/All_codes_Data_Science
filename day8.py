# day 8 code


# basic class and object 
# example 1
class address:
    city="jaipur"
    state=" rajasthan"
    def __init__(self,city,state): # this---> self # constructor
        self.city=city # attribute
        self.state=state # attribute

a=address("jaipur","rajasthan")
print(a.city)    
print(a.state)



# example 2 constructor
class address:
    def __init__(self,city,state):
        self.city=city
        self.state=state
    def show(self): # method
        print(" the city is ",self.city)   # a--> object 

a=address("jaipur","rajasthan")
a.show()




# inheritence 
class address:
    def __init__(self,city,state):
        self.city=city
        self.state=state

    def location(self):
        return f"my location is {self.city} in {self.state}"             
class user(address):
    def __init__(self,name,age,city,state):
        self.name=name
        self.age=age
        self.city=city
        self.state=state
    def username(self):
        print(f"my name is {self.name}")

    def userDetails(self):
        print(f"my name is {self.name} and my location is {self.city} in {self.state}")    

u=user("prasanjeet",20,"munger","Bihar")
u.userDetails()        
u.location()

a=address("munger","Bihar")



# encapsulation
class address:
    def __init__(self,city,state):
        self.city=city
        self.state=state

    def location(self):
        print(f"my location is {self.city} in {self.state}")

a=address("munger","Bihar")
a.location()
print(a.city)
print(a.state)

        


        
# encapsulation private attribute
class address:
    def __init__(self,city,state):
        self.__city=city  # private attribute
        self.state=state

    def location(self):
        print(f"my location is {self.__city} in {self.state}")

    def getcity(self):
        return self.__city

a=address("munger","Bihar")
a.location()
a.getcity()
# print(a.city)
print(a.state)



# polymorphism
class address:
    def __init__(self,city,state):
        self.city=city
        self.state=state
    def location(self):
        print(f"my address location is {self.city} in {self.state}")

class hometown:
    def __init__(self,city,state):
        self.city=city        
        self.state=state
    def location(self):
        print(f"my hometown location is {self.city} in {self.state}")


a=address("vizag","Andhra Pradesh")        
a.location()

b=hometown("munger","bihar")
b.location()


# class variable
class address:
    total=0 # class variable
    def __init__(self,city,state):
        self.city=city
        self.state=state
        address.total += 1

    def location(self):
        print("location")

a=address("jaipur","rajasthan")            

b=address("munger","Bihar")

a.total



# overloading and overriding

# overloading---> not possible
def address(city,state):
    print(f"my address is{city} in {state}")

def address(city,state,country)    :
    print(f"my address is {city} at {state} in {country}")

# address("munger","bihar")
address("munger","bihar","india")



# overriding 
class address:
    def __init__(self,city,state):
        self.city=city
        self.state=state
    def location(self):
        print("address locations")

class user(address):
    def __init__(self,name,age,city, state):
        super().__init__(city, state)        
        self.name=name
        self.age=age
    def location(self):  # overriding
        print("user locations ")

u=user("prasanjeet",20,"munger","bihar")
u.location()    



# tuple
# tuple is immutuable


t=(10,20,30)
print(t[0])
print(t[-1])

# example
marks=[98,90,80,85]
marks[3]=50
print(type(marks))
print(marks)

t=tuple(marks)
print(type(t))
print(t)


m=list(t)
print(type(m))
print(m)


