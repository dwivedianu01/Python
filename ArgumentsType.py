'''
In Python there is two type of arguments we an use or pass to method.
#1 . keyword-Only Argument
#2. Positional Argument

#1 Keyword-only: Pass argument with name so order no matter

Syntax : – 
FunctionName(paramName = value, ...)

#2 Positional: Pass argument with order, if you change order wrong out put will appear
Syntax :-FunctionName(value1, value2, value3,....)

'''
class A():
    def subtract(self,n1,n2):
        return n1-n2
    


a = A()
print(a.subtract(n2=5,n1=30)) # By Keyword-only
print(a.subtract(10,20)) #By Position 




    
