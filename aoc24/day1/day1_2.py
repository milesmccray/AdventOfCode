"""This time, you'll need to figure out exactly how often each number from
the left list appears in the right list. Calculate a total similarity score
by adding up each number in the left list after multiplying it by the number
of times that number appears in the right list.
Once again consider your left and right lists. What is their similarity score?
"""

with open('input.txt', 'r') as f:
	data = f.read().splitlines()

# Creates a numbered list with no whitespace
number_list = [numbers.split() for numbers in data]

# Separate the pairs of numbers into their associated lists
list_1 = []
list_2 = []

for pair in number_list:
	list_identifier = 0
	for number in pair:
		if list_identifier == 0:
			list_1.append(int(number))
			list_identifier += 1
		else:
			list_2.append(int(number))
# Sort
list_1.sort()
list_2.sort()
total_similarity = 0

for value1 in list_1:
	total_similarity += value1 * list_2.count(value1)
print(total_similarity)


