num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1)) #recordar que el segudo elemento del rango no se incluye, por ese motivo es necesario incluir el num+1

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)
