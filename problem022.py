"""

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""

from io import open

names_file = open('p022_names.txt', 'r')
names = names_file.read().split(',')
names.sort()

position = 1
total_score = 0

for name in names:
	name_value = 0

	for letter in name:
		# obtiene el valor del nombre con el valor ASCII de las letras
		name_value += ord(letter)-64

	score = name_value * position
	position += 1
	total_score += score

print(total_score)


names_file.close()

# [Finished in 348ms]
