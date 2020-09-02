import datetime

print('Min and max', datetime.MINYEAR, datetime.MAXYEAR)

#from datetime import timedelta
    #timedelta to liczenie roznicy w czasie
d1 = datetime.timedelta(days=1, hours=2, minutes=-30)
print(d1)

d2 = datetime.timedelta(days=-1, hours=-2, minutes=-15)
print(d2)

print('timedelta sum:',d1+d2)
print('\n')



#from datetime import date
    #datetime do dat
print('Today is', datetime.date.today())

today = datetime.datetime.today()
daysToPay = datetime.timedelta(days=7)
print('Today is', today)
print('Bills should be paid within:', daysToPay.days, 'days')
print('The bill should be paid till:', today + daysToPay)
print('\n')



endOfTheWorld = datetime.date.max
print('The final end of the world will happen (by Python):', endOfTheWorld)
print(endOfTheWorld.weekday())
print('\n')


bornDate = datetime.date(1991,12,31)
today = datetime.date.today()
print(today-bornDate)
print('\n')


#from datetime import datetime
    #datetime opisuje date polaczona z czasem
print('now()\t', datetime.datetime.now())
print('today()\t', datetime.datetime.today())
print('utcnow()\t', datetime.datetime.utcnow())
print('weekday()\t', datetime.datetime.today().weekday())
print('\n')





