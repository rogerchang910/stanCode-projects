"""
File: boggle.py
Name: Roger(Yu-Ming) Chang
----------------------------------------
This program recursively finds all the possible word(s)
for the letters input by users and terminates when all
the input letters are searched over.
"""

# Constant
FILE = 'dictionary.txt'					# This is the filename of an English dictionary
ROWS = 4								# The number of rows for the boggle game.
CATEGORY = ['a', 'b', 'c', 'd', 'e',    # The keys of the words_dicts
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y',
            'z']

# Global
words_dict = {}							# Contains all words in the dictionary.
boggle = []								# Contains all found words in the boggle game.


def main():
	board = []
	read_dictionary()
	print(f'Welcome to the boggle game! Please input {ROWS} letters in each row.')
	print('NOTE: there must be whitespace between two letters. ex: a b c d')
	print('---------------------------------------------------------------')

	for i in range(ROWS):
		row = input(f'{i+1} row of letters: ')
		row = row.lower()

		for j in range(len(row)):
			# Check whether input formats are correct.
			if j % 2 == 0:
				if not row[j].isalpha():
					print('Illegal input')
					return
			if j % 2 == 1:
				if row[j] != ' ':
					print('Illegal input')
					return

		board.append(row.split())

	find_boggle(board)
	print(f'There are {len(boggle)} words in total.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python dict according to the first letter.
	"""
	# The keys are alphabets. Each key (alphabet) has an empty list in the beginning.
	for i in range(len(CATEGORY)):
		words_dict[CATEGORY[i]] = []

	# Put words to the corresponding list in a python dict according to the first letter of a word.
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			words_dict[word[0]].append(word)


def find_boggle(board):
	"""
	:param board: list[list[str]], letters users input.
	"""
	coordinate_lst = []
	letter_lst = []
	word_str = ''
	# Choose the first letter.
	for y in range(len(board)):
		for x in range(len(board[y])):

			coordinate_lst.append((x, y))
			letter_lst.append(board[y][x])
			word_str += letter_lst[-1]

			find_boggle_helper(board, coordinate_lst, letter_lst, word_str)

			coordinate_lst.clear()
			letter_lst.clear()
			word_str = ''


def find_boggle_helper(board, coordinate_lst, letter_lst, word_str):
	"""
	:param board: list[list[str]], letters users input.
	:param coordinate_lst: list[tuple], coordinates of letters.
	:param letter_lst: list[str], contains chosen letters.
	:param word_str: str, combines all letters in letter_lst.
	"""
	if len(word_str) >= 4:
		if word_str in words_dict[word_str[0]] and word_str not in boggle:
			print(f'Found: \"{word_str}\"')
			boggle.append(word_str)

	# Always choose the last element in coordinate_lst as the start to search.
	x = coordinate_lst[-1][0]
	y = coordinate_lst[-1][1]

	# Searching neighbors of the letter in (x, y).
	for i in range(-1, 2):
		for j in range(-1, 2):
			# Neighbor's coordinate. If meets below conditions, it will become the searching beginning.
			new_x = x + j
			new_y = y + i

			# Check whether over the board.
			if 0 <= new_x < len(board):
				if 0 <= new_y < len(board):

					if (new_x, new_y) not in coordinate_lst:
						coordinate_lst.append((new_x, new_y))
						letter_lst.append(board[new_y][new_x])
						word_str += letter_lst[-1]

						if has_prefix(word_str):
							find_boggle_helper(board, coordinate_lst, letter_lst, word_str)

						coordinate_lst.pop()
						letter_lst.pop()
						word_str = word_str[:len(word_str)-1]


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in words_dict[sub_s[0]]:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
