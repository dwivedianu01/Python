from datetime import date,datetime

today = date.today()

print(f"Today's date {today}")
print(f"Today's Year {today.year}")
print(f"Today's Month {today.month}")
print(f"Today's Day {today.day}")

current_time = datetime.now() 
 
print("Year :", current_time.year)
 
print("Month : ", current_time.month)
 
print("Day : ", current_time.day)
 
print("Hour : ", current_time.hour)
 
print("Minute : ", current_time.minute)
 
print("Second :", current_time.second)
 
print("Microsecond :", current_time.microsecond)
