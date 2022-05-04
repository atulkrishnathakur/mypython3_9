def fun1():
 print("hello")
fun1()


def fun2(name):
 print("Name: "+name)
fun2("Atul")
fun2("Krishna")
fun2("Thakur")


def fun3(*kids):
  print("My Name is: " + kids[1])
  
fun3("Atul", "Krishna", "Thakur")
