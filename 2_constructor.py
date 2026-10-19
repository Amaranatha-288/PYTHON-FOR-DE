class Myclass: 

  #Class variables

  def __init__(self,dyn1,dyn2,dyn3):
     self.dyn1=dyn1
     self.dyn2=dyn2
     self.dyn3=dyn3
  def func1(self):
          print(f"Hello World,{self.dyn1}")

  def func2(self):
         print(f"Hello Globe,{self.dyn2}")

  def func3(self):
         print(f"Hello Globe,{self.dyn3}")


obj = Myclass("Amar","v","a")

obj.func1()
# Another Way to call the fuction
Myclass.func2(obj)
