import csv

fc = []
sc = []
tc = []
foc = []
none = []
with open('responses.csv', 'r') as names:
	reader = csv.reader(names, delimiter=',')
	for row in reader:
		who = {}
		who[row[1].lower()] = row[3]
		if row[3][:2] == '16':
			fc.append(who)
		if row[3][:2] == '17':
			sc.append(who)
		if row[3][:2] == '18':
			tc.append(who)
		if row[3][:2] == '19':
			foc.append(who)
		if row[4] == 'none':
			none.append(who)

with open('sortnames.csv', 'wb') as names:
	writer = csv.writer(names, delimiter=',')
	writer.writerow(['first'])
	for name in fc:
		for key,val in name.items():
			writer.writerow([key,val])
	
	writer.writerow(['second'])
	for name in sc:
		for key,val in name.items():
			writer.writerow([key,val])

	writer.writerow(['third'])
	for name in tc:
		for key,val in name.items():
			writer.writerow([key,val])

	writer.writerow(['fourth'])
	for name in foc:
		for key,val in name.items():
			writer.writerow([key,val])

	writer.writerow(['none'])
	for name in none:
		for key,val in name.items():
			writer.writerow([key,val])

