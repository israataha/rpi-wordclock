import datetime

#Get the time
now = datetime.datetime.now()
hour = now.hour % 12 + (1 if now.minute/5 > 7 else 0)
minute = round(now.minute/5)

#Prefix
prefix = "IT IS"

#Hours
hours = ["TWELVE", "ONE", "TWO", 
         "THREE", "FOUR", "FIVE", \
         "SIX", "SEVEN", "EIGHT" ,\
         "NINE", "TEN", "ELEVEN"]

#Minutes
minutes = ["", "FIVE PAST", "TEN PAST", "QUARTER PAST", \
           "TWENTY PAST", "TWENTY FIVE PAST", "HALF PAST", \
           "TWENTY FIVE TO", "TWENTY TO", "QUARTER TO", \
           "TEN TO", "FIVE TO"]

#Suffix
oclock = "OCLOCK"

print(prefix)
print(minutes[minute])
print(hours[hour])
print(oclock if minute == 0 else "")