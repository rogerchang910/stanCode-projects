"""
File: anagram.py
Name: Roger(Yu-Ming) Chang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'                 # This is the filename of an English dictionary
EXIT = '-1'                             # Controls when to stop the loop
CATEGORY = ['a', 'b', 'c', 'd', 'e',    # The keys of the words_dicts
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y',
            'z']

# Global
words_dict = {}                         # Contains all vocabularies in an dictionary
anagrams = []                           # Contains all anagrams for the entered word.


def main():
    read_dictionary()
    print(f'Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)')

    while True:
        word = input('Find anagrams for: ')
        word = word.lower()
        if word == EXIT:
            break
        else:
            print('Searching...')
            find_anagrams(word)
            print(f'{len(anagrams)} anagrams: {anagrams}')
            anagrams.clear()


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python dict according to the first letter.
    """
    # The keys are alphabets. Each key (alphabet) has an empty list in the beginning.
    for i in range(len(CATEGORY)):
        words_dict[CATEGORY[i]] = []
    # Appends words to the corresponding list in a python dict according to the first letter of a word.
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            words_dict[word[0]].append(word)


def find_anagrams(s):
    """
    :param s: str, the word users input.
    :return: str, anagrams for the word input.
    """
    find_anagrams_helper(s, [], [], '')


def find_anagrams_helper(s, ch_lst, index_lst, current_str):
    """
    :param s: (str), the word users input.
    :param ch_lst: list[str], letters of the word input with different combinations.
    :param index_lst: list[int], combinations of indexes of letters of the word input.
    :param current_str: str, combines all letters in ch_lst.
    :return: str, anagrams for the word input.
    """
    if len(current_str) == len(s):
        if current_str in words_dict[current_str[0]] and current_str not in anagrams:
            print('Found:', current_str)
            print('Searching...')
            anagrams.append(current_str)
    else:
        for i in range(len(s)):
            if i not in index_lst:

                index_lst.append(i)
                ch_lst.append(s[i])
                current_str += s[i]

                if has_prefix(current_str):
                    find_anagrams_helper(s, ch_lst, index_lst, current_str)

                index_lst.pop()
                ch_lst.pop()
                current_str = current_str[:len(current_str)-1]


def has_prefix(sub_s):
    """
    :param sub_s: str, the part of a vocabulary.
    :return: bool, If there is any words with prefix stored in sub_s.
    """
    for word in words_dict[sub_s[0]]:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()