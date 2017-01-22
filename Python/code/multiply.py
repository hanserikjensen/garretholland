#Create a function called 'multiply' that reads each value in the list 
#~ #(e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
#The function should multiply each value in the list by the second argument. For example, let's say: 
#a = [2,4,10,16] 

def multiply(list):
	new_list = []
	for idx in list:
		new_list.append(idx*5)
	print new_list
	

multiply([2,4,10,16])
