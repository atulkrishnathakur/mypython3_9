## The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

## To understand the meaning of classes we have to understand the built-in __init__() function.

## All classes have a function called __init__(), which is always executed when the class is being initiated.

## Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

## Note: The __init__() function is called automatically every time the class is being used to create a new object.

## Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.




class Person:
 mycity = ""
 def __init__(self,name,age,city):
   
   self.myname = name
   self.myage = age
   self.mycity = city
   
obj = Person("atul krishna thakur",20,"Buxar")
print(obj.myname)
print(obj.myage)
print(obj.mycity)


## The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

## It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

class Person1:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person1("John", 36)
p1.myfunc()

