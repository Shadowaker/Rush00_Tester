#!usr/bin/python3
import os
import time
import sys


def executor(x, main="ex00/main.c", tmain="rush/main.c", form="\n"):

	if os.system(f"gcc -Wall -Wextra -Werror {main} ex00/ft_putchar.c ex00/rush0{x}.c -o rush{x}") != 0:
		print(f"\033[93mRush0{x}\033[0m: \033[91mFail to compile\033[0m", end=form, flush=True)
		return None

	os.system(f"gcc -Wall -Wextra -Werror {tmain} rush/ft_putchar.c rush/rush0{x}.c -o sol{x}")

	if os.system(f"./rush{x} > tmp.gcook") != 0:
		print(f"\033[93mRush0{x}\033[0m: \033[91mFail to execute\033[0m", end=form, flush=True)
		return None

	os.system(f"./sol{x} > tmp.dan")

	if os.system(f"diff tmp.gcook tmp.dan > /dev/null") != 0:
		print(f"\033[93mRush0{x}\033[0m: \033[91mKO\033[0m", end=form, flush=True)
	else:
		print(f"\033[93mRush0{x}\033[0m: \033[92mKO\033[0m", end=form, flush=True)

	os.system(f"rm sol{x} rush{x} tmp.gcook tmp.dan")
	return None

def write_main(x, y):

	with open("main.sample", "r") as f:
		reading = f.read()

	string = reading.format(x=x, y=y)

	with open("main.c", "w") as f:
		f.write(string)

def core(rush, form="\n"):
	d = {0: (1, 1), 1: (10, 10), 2: (42, 42), 3: (100, 100), 4: (200, 200), 5: (500, 500),
		6: (2147483647, -2147483648), 7: (-2147483648, 2147483647), 8: (-33, 23),
		9: (-2147483648, -2147483648), 10: (0, 0), 11: (-42, -42)}

	for i in range(0, 12):

		x, y = d[i]
		write_main(x, y)
		executor(rush, main='main.c', tmain='main.c', form=form)

	os.system(f"rm main.c")

def main():
	if "ex00" not in os.listdir("./"):
		print("Help I'm stupid, please check the files...")
		return None

	if os.system("norminette ex00 > norm") != 0:
		print("\033[91m\tNORMINETTE FAILED!\n")
		os.system("cat norm ; rm norm")
		print("\033[0m")
		return None
	os.system("rm norm")

	try:
		arg_1 = sys.argv[1].lower()

		if arg_1 == "b":
			for x in range(0, 5):
				core(x, "\t")
				print("\n")
		else:
			if arg_1 not in [str(x) for x in range(0, 5)]:
				raise Exception()
			else:
				core(arg_1)

	except Exception as _:
		print("Error: not enough argument or wrong parameter.\n\n",
			"\033[92mExample\033[0m]: python3 tester.py method\n\n",
			"\033[92mmethods: [0, 1, 2, 3, 4, b]\033[0m")


main()