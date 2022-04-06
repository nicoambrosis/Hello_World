a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print('a=',a)
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print('b=',b)
c=[]


for item in a:              #esta sucesion de if's esta muy bueno, pero hay que 
                            #tener en cuenta que solo se aplican al if anterior (por eso hay que aplicarle sangria antes)
    if item in b:
        if item not in c:
            c.append(item)

print('overlaps=',c)
