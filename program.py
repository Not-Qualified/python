# Have Used both method for thread - with threading.Thread and concurrent.futures

# Although, threading is suited for I/O bound task, Factorial Count is Much more CPU
# 	Bound and threading is not good that, I suggest Multi-Processing Approach

# Yet, I cut down factorial Process in threading by using length of Integer,
# 	Not the Best Solution, Only thing can help is Multi-Processing Modules

import re
import time
import math
from datetime import datetime
import concurrent.futures
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

start = time.perf_counter()

def manipulate_str(cs_str):
	cs_str = re.split(" |\n", cs_str)

	now = datetime.now()
	file = open(f"test-{now.strftime('%d-%m-%Y@%H-%M')}.txt", "a+")
	for i in cs_str:
		if bool(re.search(r'\d', i)):
			file.write(f"{i}\n")
	file.close()


def factorial(num_range):
	# print([*num_range])
	fact = 1
	for i in num_range:
		fact *= i

	return fact

num = -1
while num < 1:
	try:
		num = int(input("Enter Positive Integer Number to Find Factorial: "))
	except ValueError:
		pass


th = len(str(num))
thread_slices = [range(1, num+1)[i::th] for i in range(th)]
print(thread_slices)

factoid = 1
with concurrent.futures.ThreadPoolExecutor() as executor:
	results = executor.map(factorial, thread_slices)

	for result in results:
		factoid *= result

print(f"Factorial of {num} is {factoid}")
print(f"{len(thread_slices)} thread(s) created for factorial operation")

m = Thread(target=manipulate_str, args=[cs_str])

m.start()

m.join()

finish = time.perf_counter()

print(f"Time Elapsed - {round(finish-start, 2)} seconds")
