"""
File: weather_master.py
Name: Roger(Yu-Ming) Chang
-----------------------------------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment Handout.
"""

# Constant
EXIT = -100						# Controls when to end the program.


def main():
	t_lst = []
	cold_day = 0
	print('stanCode \"Weather Master 4.0\" !')

	t = int(input('Next Temperature: ' + '(or ' + str(EXIT) + ' to quit?) '))
	if t == EXIT:
		print('No temperature were entered.')
	else:
		t_lst.append(t)
		while True:
			t = int(input('Next Temperature: ' + '(or ' + str(EXIT) + ' to quit?) '))
			if t == EXIT:
				break
			t_lst.append(t)

		for t in range(len(t_lst)):
			if t < 16:
				cold_day += 1

		print('Highest Temperature:', max(t_lst))
		print('Lowest Temperature:', min(t_lst))
		print('Average:', sum(t_lst)/len(t_lst))
		print(str(cold_day) + ' cold day(s).')


if __name__ == "__main__":
	main()
