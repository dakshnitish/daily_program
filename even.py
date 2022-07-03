# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b =[]
# for i in a:
#     if i%2==0:
#         b.append(i)
        
#     else:
#         continue 
# print(b)      

# print ('or')
# b = [element for element in a if element % 2 == 0]
# print(b)  


a=[1,2,3,4,23,45,5,6,5,4,8,19]
b=[2,4,23.4,8,5,19]
#lst=set(a) & set(b)
#l=list(lst)
l=[i for i in a and b if i in a and b]
print(l)