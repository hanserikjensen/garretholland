def draw_stars(list):
	for item in list:
		if type(item) == str:
			print item[0].lower()*len(item)
		else:
			print item*'*'

		

draw_stars([4,6,10,12,22,3,'Garret','Dr. Nefario'])
