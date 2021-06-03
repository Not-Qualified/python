import string
from time import sleep, time, perf_counter
from random import randint
from threading import Thread

start_time = time()

lst = [i for i in string.ascii_letters]
found_me = ['a', 'e', 'i', 'o', 'u', 'y', 'p', 'x', 'z', 'w', 'c']

class Found(Thread):
	def run(self):
		for i in lst:
			if i.lower() in found_me:
				print("Funny Word Found")
				sleep(randint(0, 2))


class Consonant(Thread):
	def run(self):
		for i in lst:
			if i.lower() not in found_me:
				print("Consonant")
				sleep(randint(0, 1))

print(lst)

v = Found()
c = Consonant()

# v.run()
# c.run()

v.start()
c.start()

v.join()
c.join()

print(f"{time() - start_time}")