#!usr/bin/python3
import os
import time
import sys
from multiprocessing import Process


HEADER = '''

88888888ba   88        88   ad88888ba   88        88        ,a8888a,        ,a8888a,
88      "8b  88        88  d8"     "8b  88        88      ,8P"'  `"Y8,    ,8P"'  `"Y8,
88      ,8P  88        88  Y8,          88        88     ,8P        Y8,  ,8P        Y8,
88aaaaaa8P'  88        88  `Y8aaaaa,    88aaaaaaaa88     88          88  88          88
88""""88'    88        88    `"""""8b,  88""""""""88     88          88  88          88
88    `8b    88        88          `8b  88        88     `8b        d8'  `8b        d8'
88     `8b   Y8a.    .a8P  Y8a     a8P  88        88      `8ba,  ,ad8'    `8ba,  ,ad8'
88      `8b   `"Y8888Y"'    "Y88888P"   88        88        "Y8888P"        "Y8888P"



888888888888  88888888888  ad88888ba  888888888888  88888888888  88888888ba
     88       88          d8"     "8b      88       88           88      "8b
     88       88          Y8,              88       88           88      ,8P
     88       88aaaaa     `Y8aaaaa,        88       88aaaaa      88aaaaaa8P'
     88       88"""""       `"""""8b,      88       88"""""      88""""88'
     88       88                  `8b      88       88           88    `8b
     88       88          Y8a     a8P      88       88           88     `8b
     88       88888888888  "Y88888P"       88       88888888888  88      `8b


'''

def check_ctrl(path):
	tmp = ["wrong", "error"]

	with open(path, "r") as f:
		reading = f.read()
	if len([x for x in tmp if x in reading.lower()]) != 0:
		return True
	return False


def exec_diff(x, form):
	if os.system(f"./rush{x} > tmp.culo") != 0:
		print(f"\033[93mRush0{x}\033[0m: \033[91mFail to execute\033[0m", end=form, flush=True)


def executor(x, main, tmain, form, p):

	if os.system(f"gcc -Wall -Wextra -Werror {main} ex00/ft_putchar.c ex00/rush0{x}.c -o rush{x}") != 0:
		print(f"\033[93mRush0{x}\033[0m: \033[91mFail to compile\033[0m", end=form, flush=True)
		return None

	os.system(f"gcc -Wall -Wextra -Werror {tmain} rush/ft_putchar.c rush/rush0{x}.c -o sol{x}")

	p = Process(target=exec_diff, args=(x, form, ), daemon=True)
	p.start()
	p.join(6)

	if p.is_alive():
		print(f"\033[93mRush0{x}\033[0m: \033[91mTimeout\033[0m", end=form, flush=True)
		p.kill()
		return None

	os.system(f"./sol{x} > tmp.dan")

	if os.system(f"diff tmp.culo tmp.dan > ctrl") != 0:
		print(f"\033[93mRush0{x}\033[0m: \033[91mKO\033[0m", end=form, flush=True)
		if check_ctrl("./ctrl") and not p:
			print("-> Check manually.", end=form, flush=True)
	else:
		print(f"\033[93mRush0{x}\033[0m: \033[92mOK\033[0m", end=form, flush=True)
		if not p:
			print("\033[91m-> CHECK FOR CHEATING!\033[0m", end=form, flush=True)

	os.system(f"rm sol{x} rush{x} tmp.culo tmp.dan ctrl")
	return None


def write_main(x, y):

	with open("main.sample", "r") as f:
		reading = f.read()

	string = reading.format(x=x, y=y)

	with open("main.c", "w") as f:
		f.write(string)

def core(rush, form="\n"):
	d = {0: (1, 1), 1: (10, 10), 2: (42, 42), 3: (100, 100), 4: (200, 200), 5: (500, 500),
		6: (2147483647, -2147483648), 7: (-2147483648, 2147483647), 8: (-3, 233),
		9: (-2147483648, -2147483648), 10: (0, 0), 11: (-42, -42)}

	for i in range(0, 12):

		x, y = d[i]
		write_main(x, y)
		if i in [6, 7, 8, 9]:
			executor(rush, 'main.c', 'main.c', form, False)
			#executor(rush, main='main.c', tmain='main.c', form=form, p=False)
		else:
			executor(rush, 'main.c', 'main.c', form, False)
		# executor(rush, main='main.c', tmain='main.c', form=form)

	os.system(f"rm main.c")


def main():
	print("\033[94m", HEADER, "\033[0m\n\n")

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
			"\033[92mExample\033[0m: python3 tester.py method\n\n",
			"\033[92mmethods: [0, 1, 2, 3, 4, b]\033[0m")


main()
