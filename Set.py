# Set are very useful and interesting datatype, can not chnage value after creation, mutable, unordered and most important not support duplicate values

val = {'a','b','c'}
print(type(val))

val.add('d')
print(val)

try:
  val[1] = 'e'
except:
  print('Can not update value in set')

val1 = set([1,2,3,4])
val2 = set([4,5,6,7])

print(val1)
print(val2)
val3 = val1.union(val2)
print(val3)

val3 = {1,2,3,4}
val4 = {4,5,6,7}
val5 = val3.union(val4)
print(val5)



