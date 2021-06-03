import re
import time
import math
from datetime import datetime
from threading import Thread


cs_str = """Thermo Scientific (c) 2011
         Versa Star Pro   
Meter S/N               V14888
SW Rev                  11.30
Channel                 1
Probe S/n               XT3-11311
Module S/n              VA21265
Method                  100
Calibration Time        28-04-21,14:06
User ID                 LABUSER
-- pH Calibration Report --
Point                   1
pH                      1.68
mV                      292.3
Temperature             24.7 C (ATC)
Calibration Type        Manual
Point                   2
pH                      4.01
mV                      141.8
Temperature             24.7 C (ATC)
Calibration Type        Auto
Point                   3
pH                      7.00
mV                      -14.5
Temperature             24.7 C (ATC)
Calibration Type        Auto
"""

now = datetime.now()
start = time.perf_counter()


def manipulate_str(cs_str):
	str = re.split(" |\n", cs_str)

	now = datetime.now()
	file = open(f"test-{now.strftime('%d-%m-%Y@%H-%M')}.txt", "a+")
	for i in cs_str:
		if bool(re.search(r'\d', i)):
			file.write(f"{i}\n")
	file.close()


def factorial(num_range):
	print([*num_range])
	fact = 1
	for i in num_range:
		fact *= i

	# fact = 1
	# for i in range(1, num+1):
	# 	fact *= i
	return fact

	# print(f"Factorial of {num} is {fact}")
	# math.factorial(num)


num = -1
while num < 1:
	try:
		num = int(input("Enter Positive Integer Number to Find Factorial: "))
	except ValueError:
		pass


th = len(str(num))
thread_slices = [range(1, num+1)[i::th] for i in range(th)]
print(thread_slices)

threads = []
factoid = 1

for each in thread_slices:
	t = Thread(target=factorial, args=[each], )
	t.start()
	# factoid *= t
	# print(dir(t))
	threads.append(t)



for thread in threads:
	thread.join()
	print(thread.daemon)


print(factoid)

# f = Thread(target=factorial, args=[num]) # args=[i]
m = Thread(target=manipulate_str, args=[cs_str])

# f.start()
# m.start()

# f.join()
# m.join()

# factorial(i)

# manipulate_str(str)

finish = time.perf_counter()

print(f"Time Elapsed - {round(finish-start, 2)} seconds")