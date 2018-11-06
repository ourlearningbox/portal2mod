import csv

# The matrix where will be stored the game events from the log file  
events_matrix = [["Evento","Tick"]]


# If the header already exists return its index, else return -1
def FindColumn (header):
	try:
		return events_matrix[0].index(header)
	except ValueError:
		return -1

# opening the log file
input_file = open('C:\\Users\\geron\\Documents\\python\\logbotao')
 
line = input_file.readline()



current_line = 0


while line:
	

	
	# To each Game Event is created a new line in the matrix    
	if line.startswith('Game event'):
		current_line += 1
		
		# Geting Event and Tick values
		events_matrix +=[ [line.split(',')[0].split()[2].replace('"','') , line.split(',')[1].split()[1].split(':')[0] ] ];

	 
		line = input_file.readline()
		
		# In the log file the values relating to a Game Event starts with '-'
		while line.startswith('-'):

			
			current_header = line.split('=')[0].split()[1].replace('"','')
			
			current_value = line.split('=')[1].replace('"','').replace('\n','')
			
			
			# If the current header already exists  
			if FindColumn(current_header) >= 0:

				# Fill with "N\A" the empty spaces in event_matrix[current_line] from the last position of that matrix line until the index of the header corresponding to that value
				for i in range (len(events_matrix[current_line]), FindColumn(current_header) ):
					events_matrix[current_line] += ["N\\A"]
				# Add the current_value in the events_matrix
				events_matrix [current_line] += [current_value]



			else:
				# If the current header  doesn't exists 
				events_matrix[0] += [current_header]

				# Fill with "N\A" the empty spaces in event_matrix[current_line] from the last position of that matrix line until the index of the header corresponding to that value
				for i in range (len(events_matrix[current_line]), FindColumn(current_header) ):
					events_matrix[current_line] += ["N\\A"]
				# Add the current_value in the events_matrix
				events_matrix [current_line] += [current_value]





			
			line = input_file.readline()


    
	line = input_file.readline()



input_file.close()


current_line = 1
NumberOfColumns = len(events_matrix[0])

#Fill in the remain empty spaces with "N\A"
for line in range(1,len(events_matrix)):
	for i in range (len(events_matrix[line]), NumberOfColumns ):
 		events_matrix[line]+= ["N\\A"]


# Write the event_matrix in a csv file 
with open('Log_Tabela.csv', 'w') as csvFile:
	
	for row in events_matrix:
		writer = csv.writer(csvFile)
		writer.writerow(row)


csvFile.close()

