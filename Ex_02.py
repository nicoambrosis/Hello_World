number=int(input('Please, enter a number:'))
if number%2==0: #el simbolo % es muy util para diferenciar numeros pares de numeros impares. Todos los numeros pares dan 0 como resto de la division por 2
    print(number, 'es un numero par')
    if number%4==0:
        print(number, 'es multiplo de 4')
else:
    print(number, 'es un numero impar')
