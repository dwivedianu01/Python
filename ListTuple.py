#List is very important and powerful datastructure in python, 
#A single list can contain strings, integers, as well as other objects. Lists can also be used for implementing stacks and queues. Lists are mutable, i.e.,
# they can be altered once declared. The elements of list can be accessed using indexing and slicing operations.

lsta = [1,2,3,4,5]
lstb= ['a','b','c','d','e','f']
lstc = ['a',1,'b','abc']
print (lsta)
print (lstb)
print (lstc)
lsta.extend(lstb)
print (lsta)
lstc.append('xyz')
print (lstc)

# Tuples are similar to list but this is unmutable, we can not alter after declaration

tuplea = tuple((1,2,3,4,5))
tupleb= tuple(('a','b','c','d','e','f'))
tuplec = tuple(('a',1,'b','abc'))
print (tuplea)
print (tupleb)
print (tuplec)

try:
  tupleb.append('g')
  print(tupleb)
except:
  print('Error can not append')
