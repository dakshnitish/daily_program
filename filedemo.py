f=open("my_file.txt","wb")
#data=["my name is nitish ", "my dob is 28/03/1999 " ,"the language in which i am comfortable with is python"]
data=[1,2,5,7,45,8]
b=bytes(data)
#for i in b:
f.write(b)
    #f.write('\n')
f.close()


# f=open("my_file.txt","a")
# f.write("i am adding a new line")
# f.close()



# f=open("my_file.txt","r")
# print(f.read())
# f.close()