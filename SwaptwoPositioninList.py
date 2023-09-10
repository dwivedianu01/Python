#Swap two position element in List Python.
def swapPositionInListValuesMethod1(list,pos1,pos2):
    temp = list[pos1-1]
    list[pos1-1] =  list[pos2-1]
    list[pos2-1] = temp
    return list

def swapPositionInListValuesMethod2(list,pos1,pos2):
   list[pos1-1],list[pos2-1] = list[pos2-1],list[pos1-1]
   return list

def swapPositionInListValuesMethod3(list,pos1,pos2):
   vals = list[pos2-1],list[pos1-1]
   list[pos1-1],list[pos2-1] = vals
   return list

def swapPositionInListValuesMethod4(list,pos1,pos2):
   pos1Element = list.pop(pos1)
   pos2Element = list.pop(pos2-2)
   list.insert(pos1-1,pos2Element)
   list.insert(pos2-2,pos1Element)
   return list
    

list = [1,2,3,4,5]
#print(swapPositionInListValuesMethod1(list,1,3))
#print(swapPositionInListValuesMethod2(list,1,3))
#print(swapPositionInListValuesMethod3(list,1,4))

print(swapPositionInListValuesMethod4(list,1,3))
