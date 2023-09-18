"""
Directive or format code 	Returned Valued	Example
%Y	Full year with century	2021,2022
%y	Year without century with zero padded value	00,01,….21,22…,99
%-y	Year without century	0,1…,99
%m	Month with zero padded value	01-12
%-m	Month without zero padded value	1-12
%B	Full month name	January, February,…, December
%b	Short form of month 	Jan, Feb,…,Dec
%A	Full weekday name	Sunday, Monday,..
%a	Short form of weekday name	Sun, Mon,..
%w	Weekday as decimal value	0-6
%d	Days with zero padded value	01-31
%-d	Days with decimal value	1-31
%H	Hour (24-hour clock) as a zero-padded value.	00-23
%-H	Hour (24-hour clock) without zero-padded value.	0,1,…,23
%I	Hour (12-hour clock) as a zero-padded value.	01-12
%-I	Hour (12-hour clock) without zero-padded value.	1-12
%M	Mins with zero-padded 	00-59
%-M	Mins without zero padded value	0-59
%S	Secs with zero padded value	00-59
%-S	Secs without zero padded value	0-59
%f	Micro Secs with zero-padded value	000000 – 999999
%p	Locale’s AM or PM.	AM/PM
%j	Day of the year with zero padded value	001-366
%-j	Day of the year without zero padded value	1-366
%z	UTC offset in the form +HHMM or -HHMM.	 
%Z	Time zone name.	 
%C	Locale’s appropriate date and time	Fri Apr 02 02:09:07 2020
%x	Locale’s appropriate date	02/04/22
%X	Locale’s appropriate time	02:04:22
%W	Week number of the year. Monday as first day of week	00-53
%U	Week number of the year. Sunday as first day of week	00-53

https://www.geeksforgeeks.org/how-to-format-date-using-strftime-in-python/
"""
#Format date by strftime function

import datetime

current_date = datetime.datetime.now()
print(f"Today's date {current_date}")

current_year = current_date.strftime("%Y")
print(f"Year {current_year}")

current_year = current_date.strftime("%y")
print(f"Year {current_year}")

current_minute = current_date.strftime("%M")
print(f"Minutes {current_minute}")

current_month = current_date.strftime("%m")
print(f"Month {current_month}")

current_week = current_date.strftime("%W")
print(f"Week {current_week}")

current_week_n = current_date.strftime("%U")
print(f"Week {current_week_n}")

current_full_month = current_date.strftime("%B")
print(f"Month {current_full_month}")

current_short_month = current_date.strftime("%b")
print(f"Month {current_short_month}")



