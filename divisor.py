list=[3,6,7,8,9,10,18,4]
l=[]
print(list)
n=int(input("enter a number from the above list: "))
for i in list:
    if i%n==0:
        l.append(i)

    else:
        pass

print(l)      
