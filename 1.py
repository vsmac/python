class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
  
  def myfunc1(self):
    print("Hello my name from function2 is " + self.name)
p1 = Person("John", 36)
p1.myfunc()
p2 = Person("Raj", 34)
p2.myfunc1()
