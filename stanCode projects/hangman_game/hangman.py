"""
File: hangman.py
Name: Roger(Yu-Ming) Chang
-------------------------------
This file demonstrates a Python Console hangman game.
At the beginning of the game, users are asked to input
one letter at a time to guess out a dashed vocabulary (answer).
If the letter is in the answer, the Console updates the
dashed word to its current status. 7 wrong guesses end the game.
"""

import random

# Constant
N_TURNS = 7


def main():
    """
    Users will guess a word by entering a letter each time,
    each one has N_TURNS chances and if answer wrong, the chances
    will minus one.
    """
    chance = N_TURNS
    word = random_word()

    ch_lst = list(e for e in word)
    ans_lst = list('-' for e in word)

    ans = lst_to_ans(ans_lst)
    print('The word looks like:', ans)
    print(f'You have {chance} to guess.')

    while chance > 0:
        guess = input('Your guess: ')
        guess = guess.upper()

        # The situation the input format was correct.
        if len(guess) == 1 and guess.isalpha():
            # The input letter can be found in the word.
            if guess in word:

                for i in range(len(word)):
                    if guess == ch_lst[i]:
                        ch_lst[i] = '-'
                        ans_lst[i] = guess
                ans = lst_to_ans(ans_lst)
                print('You are correct!')

                if ans == word:
                    break
                print('The word looks like', ans)

            # The input letter can't be found in the word.
            else:
                chance -= 1
                ans = lst_to_ans(ans_lst)
                print(f'There is no {guess}\'s in the word.')

                if chance == 0:
                    break

                print('The word looks like', ans)
                print(f'You have {chance} guesses left.')
        # The illegal input format.
        else:
            print('illegal format.')

    if ans == word:
        print('You win!!')
    if chance == 0:
        print('You are completely hung : (')
    print('The word was:', word)


def lst_to_ans(ans_lst):
    """
    :param ans_lst: list[str], contains correct guesses the user entered and undeciphered character.
    :return: str, turns the list into string.
    """
    ans = ''
    for i in range(len(ans_lst)):
        ans += ans_lst[i]
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


if __name__ == '__main__':
    main()
