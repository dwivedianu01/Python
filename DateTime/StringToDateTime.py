#Use strptime to format date string to date
import datetime

import datetime
 
data = "1983/11/19"
dformat = '%Y/%m/%d'

formatted_date = datetime.datetime.strptime(data,dformat)
print(f"Formatted date {formatted_date}")

print(f"Date {datetime.datetime.strptime(data, dformat).date()}")

