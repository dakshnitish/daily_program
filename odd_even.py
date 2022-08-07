# num=int(input("enter a number:"))
# if num%2==0:
#     print("number is even ")

# else:
#     print("number is oddddd")   

# with open('candidate_data.csv','r') as f:
#    result = f.read()
#    print(result)

counter_dict = {}
with open('candidate_data.csv','r') as f:
	line = f.readline()
	while line:
		line = line.strip()
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)
