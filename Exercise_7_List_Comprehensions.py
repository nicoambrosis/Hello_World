##################################################

b = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#a=[]
##########################forma larga...################################
#for age in b:
#    if age%2==0:
#        a.append(age)



#########################Forma corta#######################################

a=[age for age in b if age%2==0]


print(a)
