# Without try/catch , open below 2 commented lines if you want to check this error
#count  = 1/0
#print(count)


# With try catch
try:
  count = 1/0
  print(count)
except:
  print("Some error happened")

# With specific Error (1)
try:
  count = 1/0
  print(count)
except ZeroDivisionError:
  print("ZeroDivisionError error happened")

# With specific Error (2)
x = 10
y = "Hi"
try:
    z = x + y
except TypeError:
    print("Error: cannot add an int and a str")

# try/catch with else and finally

list = [1,2,3]
try:
  print("Print postion = %d" %(list[0]))
except:
   print("Error in Printing")
else:
   print("In else condition")
finally:
   print("This will execute always")

print('--------------------------------------------------------------')

list = [1,2,3]
try:
  print("Print postion = %d" %(list[3]))
except:
   print("Error in Printing")
else:
   print("In else condition")
finally:
   print("This will execute always")

