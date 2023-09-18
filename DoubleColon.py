'''
Python Double Colon (::) Syntax
Slicing in Python
Collection(start:stop:step)
Colleaction - Any Collection
start - slicing start from index
stop - slicing ends at index
step - This means the list will jump number of steps repeatedly during the iteration.
'''
lst = [1,2,3,4,5,6,7,8,9,10]

lst_1 = lst[3::] #start from index 3
print (lst_1)

lst_2 = lst[:7:] #stop at index 7
print (lst_2)

lst_3 = lst[::3] #jump 3 steps during slicing
print (lst_3)

lst_4 = lst[3:9:2] #start from index 3, stop at 9, jump 2 steps
print (lst_4)
