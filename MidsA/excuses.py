import csv


f = open('table.txt', 'r')


table = []
for line in f:
	table.append(line.split())



''' The table should be formatted as such:

			
1st platoon	|	Last name		| First name	|	Alpha	|	Total Absences	|	Total Tardies/Leave Early	|	
						|							|							|				|									|														|
						|
						|
____________
2nd platoon	|
						|
						|
						|
....

'''
platoons = [[],[],[],[],[]]
today = ['UA','Tardy/Left Early']


with open('platoons.csv', 'r') as pnames:
	reader = csv.reader(pnames, delimiter=',')
	i=0
	for row in reader:
		for num,names in enumerate(row):
			platoons[num].append(names)

