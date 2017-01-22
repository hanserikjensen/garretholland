#~ Create a program that prompts the user ten times for a test score
#~ between 60 and 100. Each time a score is generated, your program should 
#~ display what the grade is for a particular score. Here is the grade table:

def scores_and_grades():
	scores =[]
	print_statement = "Score: {}; Your grade is {}"
	for count in range(10):
		score = int(raw_input ("Please provide a test score between 60-100: "))
		while score <= 59 or score > 100:
			score = int(raw_input ("""Oops! You provided a score outside of the requested range, please provide a test score between 60-100: """))
			#~ if score <= 59 or score > 100:
				#~ print "Oops, like Britney, you did it again, and I don't know how to re-promt you wihtout going into infinite if statements so I'm breaking out of this code and you can run this program again"
				#~ break
		scores.append(score)
	print "\nScores and Grades:\n"
	for score in scores:
		if score >= 90 and score <= 100:
			grade = "A"
			print print_statement.format(score, grade)
		elif score >= 80 and score <= 89:
			grade = "B"
			print print_statement.format(score, grade)
		elif score >= 70 and score <= 79:
			grade = "C"
			print print_statement.format(score, grade)
		elif score >= 60 and score <= 69:
			grade = "D"
			print print_statement.format(score, grade)
	print "\nEnd of the program. Bye!"


scores_and_grades()
