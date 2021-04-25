import random
start = input("請決定隨機數字範圍開始值:")
end = input ("請決定隨機數字範圍結束值:")
start = int(start)
end = int(end)

r = random.randint(start, end)
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