# In this blog we will cover special args in python
#1. *args (Non keyword arguments)
#2. **kwargs (Key word arguments)

def func1(self,*args):
  print(self)
  for arg in args:
      print (arg)

func1('a','b','c')

def func2(self,**kwargs):
  print(self)
  for key,value in kwargs:
     print(key+'::'+value)
    
func2('s1',a1='val1',a2='val2',a3='val3',a4='val4')

def func3(self,*args,**kwargs):
  print(self)
  for arg in args:
      print (arg)

  for key,value in kwargs:
     print(key+'::'+value)
    
func3('s1',1,2,3,4,a1='val1',a2='val2',a3='val3',a4='val4')
