users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
count = 1
print 'Students'
for student in users['Students']:
	length = len(student['first_name']) + len(student['last_name'])
	print str(count) + "-" + " " + student['first_name'] + " " + student['last_name'] + " " + "-" + " " + str(length)
	count += 1
count = 1
print '\nInstructors'
for instructor in users['Instructors']:
	length = len(instructor['first_name']) + len(instructor['last_name'])
	print str(count) + "-" + " " + instructor['first_name'] + " " + instructor['last_name'] + " " + "-" + " " + str(length)
	count += 1
	
 
 
 
 
 
 
 
 
 
 
 

