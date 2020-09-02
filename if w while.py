values=[10,43,12,48,11,18,97,19,33,66]

#trzy liczby rosnace pod rzad
i=0
max=len(values)-2

while i < max :
    print(i, values[i], values[i+1],values[i+2])
    if values[i]<values[i+1]<values[i+2] :
        print('\tFound: ',values[i],values[i+1],values[i+2])
    i+=1
