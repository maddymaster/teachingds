import time
def numbers(max):
	time1 = time.time()
	for i in range(0,max):
		print(i)
	time2 = time.time()
	print(str(time2 - time1))

numbers(100)