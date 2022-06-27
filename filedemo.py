f=open("my_file.txt","w")
data=["my name is nitish ", "my dob is 28/03/1999 " ,"the language in which i am comfortable with is python"]
for i in data:
    f.write(i)
    f.write('\n')
f.close()


# f=open("my_file.txt","a")
# f.write("i am adding a new line")
# f.close()



# f=open("my_file.txt","r")
# print(f.read())
# f.close()