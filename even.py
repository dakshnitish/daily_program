a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b =[]
for i in a:
    if i%2==0:
        b.append(i)
        
    else:
        continue 
print(b)      

print ('or')
b = [element for element in a if element % 2 == 0]
print(b)