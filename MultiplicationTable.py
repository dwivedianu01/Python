import pyodbc 


number = int(input(" Please Enter any number less than 10 : "))

print(" Multiplication Table ")

for i in range(number, 10):
    for j in range(1, 11):
        print('{0}  *  {1}  =  {2}'.format(i, j, i*j))
    print('==============')