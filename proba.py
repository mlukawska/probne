print ("test gita")
#input('Press enter to continue...')



IsWeekend = True
print('Is Weekend =', IsWeekend)

Temperature = 22
print('Temperature =', Temperature)

ToDoList = ''
print('ToDoList =', ToDoList)

IsHappy = not IsWeekend and Temperature >= 20 and ToDoList == '' or IsWeekend and Temperature < 20
print('IsHappy =', IsHappy)


