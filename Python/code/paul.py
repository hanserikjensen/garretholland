def scoresAndGrades():
	for count in range(10):
	#print "Scores and Grades"
		score = raw_input ("Please provide a test score between 60-100: ")
		score = int(score)
		print type(score)
		if score >= 90 and score < 100:
			grade = "A"
			print "your grade is", grade
		elif score >= 80 and score <= 89:
			grade = "B"
			print "Score: {}; Your grade is {}".format(score, grade)
		elif score >= 70 and score <= 79:
			grade = "C"
			print "Score: {}; Your grade is {}".format(score, grade)
		elif score >= 60 and score <= 69:
			grade = "D"
			print "Score: {}; Your grade is {}".format(score, grade)
		elif score <= 59:
			grade = "Invalid Grade"
			continue
	print "End of the program. Bye!"


scoresAndGrades()
