import csv

file_name = 'money.csv'




def openFile(file_name):
	print 'Currently opening ',file_name
	with open(file_name, 'rb') as data:
		reader = csv.reader(data)
		for row in reader:
			split_string = row[0].split('\t')
			for name in split_string:
				if name == 'Bank':
					print 'found it'


openFile(file_name)

banks = []
bank_names = raw_input('Enter in your bank names seperated by commas ')
split_names = bank_names.split(',')
count = 0
for bank in split_names:
	bank[count] = bank
	count = count + 1

credits_cards = []
credit_names = raw_input('Enter in your Credit Card names seperated by commas ')
split_names = credit_names.split(',')
count = 0
for credit in split_names:
	credit_cards[count] = credit
	count = count + 1		
