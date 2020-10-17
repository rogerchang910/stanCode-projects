"""
File: similarity.py
Name: Roger(Yu-Ming) Chang
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    Users will be asked to entered a long DNA sequence and a short DNA sequence.
    After comparison, the program will show the most similar fragment of the long DNA
    sequence with the short DNA sequence.
    """
    long_q = input_long_q()
    short_q = input_short_q()
    score = match_score(long_q, short_q)
    frag = match_frag(long_q, short_q, score)
    print('The best match is ' + str(frag))


def input_long_q():
    """
    The function will ask users input a long DNA sequence and check whether the input format is correct.
    :return: str, the correct input format.
    """
    while True:
        long_q = input('Please give me a DNA sequence to search: ')
        long_q = long_q.upper()
        wrong = 0

        for i in range(len(long_q)):
            ch = long_q[i]
            if ch == 'A' or ch == 'T' or ch == 'C' or ch == 'G':
                wrong += 0
            else:
                wrong += 1

        if wrong == 0:
            return long_q
        print('The input format is not correct.')


def input_short_q():
    """
    The function will ask users input a short DNA sequence and check whether the input format is correct.
    :return: str, the correct input format.
    """
    while True:
        short_q = input('What DNA sequence would you like to match? ')
        short_q = short_q.upper()
        wrong = 0

        for i in range(len(short_q)):
            ch = short_q[i]
            if ch == 'A' or ch == 'T' or ch == 'C' or ch == 'G':
                wrong += 0
            else:
                wrong += 1

        if wrong == 0:
            return short_q
        print('The input format is not correct.')


def match_score(strand1, strand2):
    """
    :param strand1: str, the long DNA sequence.
    :param strand2: str, the short DNA sequence.
    :return: int, the score that the fragment of strand1 is the most similar with strand2.
    """
    for i in range(len(strand1)-len(strand2)+1):
        # pick a fragment from strand1 which length is as same as strand2.
        frag = strand1[i:len(strand2)+i]
        score = 0
        for j in range(len(strand2)):
            # compare each base of a fragment of strand1 with strand2.
            if frag[j] == strand2[j]:
                score += 1
            else:
                score -= 1
        # assign the score the first fragment of strand1 got is the maximum.
        if i == 0:
            maximum = score
        else:
            if maximum < score:
                maximum = score
    return maximum


def match_frag(strand1, strand2, score):
    """
    :param strand1: str, the long DNA sequence.
    :param strand2: str, the short DNA sequence.
    :param score: int, the score that the fragment of strand1 is the most similar with strand2.
    :return: str, the fragment of strand1 which is the most similar with strand2.
    """
    for i in range(len(strand1)-len(strand2)+1):
        frag = strand1[i:len(strand2)+i]
        point = 0
        for j in range(len(strand2)):
            if frag[j] == strand2[j]:
                point += 1
            else:
                point -= 1

            if point == score:
                return frag


if __name__ == '__main__':
    main()
