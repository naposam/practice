my_list=["Banana","Mango","Apple","Orange"]

newlist=[]

# looping  list
# for loop with index
# for i in range(len(my_list)):
# 	print(my_list[i]);


# x=0
# while x < len(my_list):
# 	print(my_list[x])
# 	x=x+1;


for x in my_list:
	if "A" in x:
		newlist.append(x)
print(newlist)
