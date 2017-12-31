#랜덤구구단 출력하기

import random

dan = random.randrange(1,10)

print("구구단")
print("-------------")

for j in range(1, 10, 1):
	print("%d x %d = %d"%(dan,j,dan*j))
	if j == 9:
		print("-------------")