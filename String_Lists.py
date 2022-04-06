string=input('Enter a string:')
lenght=(len(string)-1)
string_list=list(string)
#esta linea del codigo me permite transformar la palabra anterior en un lista en la que
#cada letra de la palabra es un elemento de la lista.
print(string_list)
reverse_list=string_list[::-1]
#esta linea invierte la ista anteiorr y genera una nueva lista de manera tal que ambas listas quedan guardadas en la memoria
print(reverse_list)


count=0
a=string_list[count]
b=reverse_list[count]
if count<=lenght:
    if a==b:
        count=count+1
        if count>lenght:
            print("Pal")
    #else:
    #    print('No es un palindromo')


#hasta aca conseguimos que la palabra que metemos se transforme en una lista y adempas dimos vuelta la lista
#ahora hay que comparar cada elemento de la lista




#    n e u q u e n
#    0 1 2 3 4 5 6


#primero voy a tener que convertir el string en una lista
