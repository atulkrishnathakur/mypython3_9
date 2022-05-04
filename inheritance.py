class Father:
  def __init__(self):
    self.x = 100;
    self.y = 200;
  def myfun1(self,a,b):
   m = self.x
   n = self.y
   print("m="+str(m)+", n="+str(n))
   
  def myfun2(self):
   print("This is f2 function") 
   
class Son(Father):
 def __init__(self):
    self.x = 2000
    self.y = 3000 
 def myfun1(self,a,b):
   m = self.x
   n = self.y
   print("m="+str(m)+", n="+str(n))
   
  
obj = Son()   
obj.myfun1(10,20)  
obj.myfun2() 

