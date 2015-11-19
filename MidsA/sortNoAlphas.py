import csv

classes=[[],[],[],[],[]]
with open('sortnames.csv', 'r') as names:
	reader = csv.reader(names, delimiter=',')
	who = ''
	for rowl in reader:
		row = rowl[0]
		if row == 'first' or row == 'second' or row == 'third' or row == 'fourth' or row == 'none':
			who = row
			continue
		if who == 'first':
			classes[0].append(row)
		if who == 'second':
			classes[1].append(row)
		if who == 'thrid':
			classes[2].append(row)
		if who == 'fourth':
			classes[3].append(row)
		if who == 'none':
			classes[4].append(row)


anames = []
with open('platoons.csv', 'r') as names:
	reader = csv.reader(names, delimiter=',')
	for row in reader:
		if row[0] == 'one':
			continue
		for name in row:
			anames.append(name.lower())


