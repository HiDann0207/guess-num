import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	number = input('請輸入數字: ')
	number = int(number)
	if number == r:
		print('猜了', count, "次，終於對了!")
		break
	elif number > r:
		print('太大了喔~')
	else:
		print('再大一點!')
	print('你已經猜', count, "次囉")