import random
count = 0
heads = 0
tails = 0
for i in range(5000):
	random_num = random.random()
	rounded_num = round(random_num)
	if rounded_num == 1:
		heads += 1
		count += 1
		print "Attempt #{} Throwing a coin... It's a head!... Got {} heads so far and {} tails so far".format(count,heads,tails)
	if rounded_num == 0:
		tails += 1
		count += 1
		print "Attepmt #{} Throwing a coin... It's a tail!... Got {} heads so far and {} tails so far".format(count,heads,tails)


