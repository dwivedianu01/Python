#In this blog we will se how we can define function using lamda
#In Python, an anonymous function means that a function is without a name. As we already know the def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions. It has the following syntax: 
#Syntax
#lambda <arguments> : <statement1> if <condition> else <statement2>


lst = [11,22,44,12,34,67,89]

lamda_function = lambda lst,v: True if v in lst else False

print(lamda_function(lst,11))
print(lamda_function(lst,12))
print(lamda_function(lst,13))
print(lamda_function(lst,89))
print(lamda_function(lst,34))
print(lamda_function(lst,35))
print(lamda_function(lst,68))




