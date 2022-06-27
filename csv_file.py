f=open("candidate_data.csv","w")
fields = ['Name', 'Branch', 'Year', 'CGPA']
print(type(fields))
deatils = [['Nikhil', 'COE', '2', '9.0'], 
         ['Sanchit', 'COE', '2', '9.1'], 
         ['Aditya', 'IT', '2', '9.3'], 
         ['Sagar', 'SE', '1', '9.5'], 
         ['Prateek', 'MCE', '3', '7.8'], 
         ['Sahil', 'EP', '2', '9.1']] 
print(type(deatils))         
F=str(fields)
D=str(deatils)
for i in F:
      f.write(i)
f.write('\n') 
for i in D:       
      f.write(i) 
f.write('\n')  
f.close()  