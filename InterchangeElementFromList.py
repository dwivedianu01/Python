#Interchange fist and last element of Any List in Python.
def swapListValuesMethod1(list):
    size = len(list)
    temp = list[0]
    list[0] = list[size-1]
    list[size-1] = temp
    return list

def swapListValuesMethod2(list):
   list[0],list[-1] = list[-1],list[0]
   return list

def swapListValuesMethod3(list):
   vals = list[-1],list[0]
   list[0],list[-1] = vals
   return list

#really interesting use * opeartor
def swapListValuesMethod4(list):
   start,*middle,end = list
   list = end,*middle,start
   return list
    

list = [1,2,3,4,5]
#print(swapListValuesMethod1(list))
#print(swapListValuesMethod2(list))
#print(swapListValuesMethod3(list))

print(swapListValuesMethod4(list))
