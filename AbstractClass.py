'''
Python Support abstract class concept, abstract classes are blue prints for other classes.
A class that contains one or more abstract methods is called an abstract class. 
An abstract method is a method that has a declaration but does not have an implementation.
'''
from abc import ABC,abstractmethod

class A(ABC):
      
      @abstractmethod
      def print():
            pass
      
class B(A):
       
       def print():
             print ('Printing in B by abstrat method')
       def print_b(self):
             print ('Printing in B')
             
class C(A):
       
       def print():
             print ('Printing in C by abstrat method')


b = B()
b.print_b()
b.print


c= C()
c.print

'''
Following commented code will give error  - TypeError: Can't instantiate abstract class A with abstract method print
Reason: We can not create object of abstarct class
'''
#c = A()
#c.print()
      
     
