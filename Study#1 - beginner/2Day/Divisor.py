#약수 구하기

print("숫자를 입력하세요.")
a = int(input())

for i in range(1, a+1, 1):
	if a%i == 0:
		print(i)