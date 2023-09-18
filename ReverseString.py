#Let's write program to revers full string

str = 'Hello My name is python, enjoy your day'

print (str)

# Solution 1
lst = str[::-1]
print (lst)

# Solution 2

lst_1 = list(str)

print (lst_1)

lst_1.reverse()
print (lst_1)
reverse_str = ('').join(lst_1)
print (reverse_str)

