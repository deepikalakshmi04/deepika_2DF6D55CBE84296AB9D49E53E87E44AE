def isLeapYear(year):
 if(year %4==0 and year %100!=0)or year % 40==0:
   return True
 else:
   return False
year=int(input("ENTER THE YEAR : ")) 
if isLeapYear(year):
   print(year,"IS A LEAP YEAR ")
else:
   print(year,"IS NOT A LEAP YEAR ")
