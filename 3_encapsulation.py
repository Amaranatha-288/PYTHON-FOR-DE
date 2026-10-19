class Myclass: 

  #Class variables
  var1="Ansh"
  var2="lamba"

  #instance variable

  def __init__(self,dyn1,dyn2,dyn3):
     self.dyn1=dyn1 #public
     self.__dyn2=dyn2 #Private Variable
     self._dyn3=dyn3 #Protected
  def func1(self):
          print(f"Hello World,{self.dyn1}")

  def func2(self):
         print(f"Hello Globe,{self.dyn2}")

  def func3(self):
         print(f"Hello Globe,{self.dyn3}")


obj = Myclass("Amar","v","a")
print(obj.dyn1,obj._dyn3)