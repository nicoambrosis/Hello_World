num=float(input('Please, enter a number:'))
chek=float(input('Plese, enter another numer'))
if num%chek==0:
    print(num,'es multiplo de',chek)
else:
    print(num, 'no es multiplo de', chek)
    result=num/chek
    print(num,'/',chek,'=',result)
