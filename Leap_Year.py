# Check if year Leap
yy = int(input("Please Enter the Year :: "))

if (( yy%400 == 0)or (( yy%4 == 0 ) and ( yy%100 != 0))):
    print("%d is a Leap Year" %yy)
else:
    print("%d is Not the Leap Year" %yy)