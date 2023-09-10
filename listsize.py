from operator import length_hint

#Method One len function
data_list = [1, 2, 8, 11, 18, 7, 9, 10]
print(len(data_list))

# Method Two length_hint function
print(length_hint(data_list))

# Method Three for loop
sum  = 0
for i in data_list:
  sum = sum+1

print(sum)

#Method Four By Sum function
#loopSum = sum(1 for i in data_list)
#print(str(loopSum))

#Method Five Enumeration
c = 0
for i, a in enumerate(data_list):
    c += 1
print(c)


