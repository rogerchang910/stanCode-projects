"""
File: complement.py
Name: Roger(Yu-Ming) Chang
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
The program asks users for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    The program will output the complement of a DNA sequence users input.
    """
    dna = input_dna()
    complement = build_complement(dna)
    print('The complement of ' + str(dna) + ' is ' + str(complement))


def input_dna():
    """
    The function will ask users input a DNA sequence and check whether the input format is correct.
    :return: str, the correct input format.
    """
    while True:
        dna = input('Please give me a DNA strand and I\'ll find the complement: ')
        dna = dna.upper()
        wrong = 0
        for i in range(len(dna)):
            ch = dna[i]
            if ch == 'A' or ch == 'T' or ch == 'C' or ch == 'G':
                wrong += 0
            else:
                wrong += 1
        if wrong > 0:
            print('The input format is not correct.')
        if wrong == 0:
            return dna


def build_complement(base):
    """
    :param base: str, the DNA sequence users input.
    :return: str, the complement of the entered DNA sequence.
    """
    strand = ''
    for i in range(len(base)):
        ch = base[i]
        if ch == 'A':
            strand += 'T'
        if ch == 'T':
            strand += 'A'
        if ch == 'C':
            strand += 'G'
        if ch == 'G':
            strand += 'C'
    return strand


if __name__ == '__main__':
    main()
