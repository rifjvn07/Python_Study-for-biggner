# 구구단출력하기

print("구구단")
print("-------------")

for i in range(1, 10, 1):
	for j in range(1, 10, 1):
		print("%d x %d = %d"%(i,j,i*j))
		if j == 9:
			print("-------------")


