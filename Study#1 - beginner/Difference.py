# Problem: 두수의 차이 구하기

#숫자를 2번 입력받는다.
print("숫자를 입력하세요 : ")
a = int(input())
print("숫자를 하나 더 입력하세요 : ")
b = int(input())

# 조건문을 이용하여 숫자의 차이를 비교한다.

if a <= b :
	c = b-a
else : 
	c = a-b

print("두 숫자 간의 차이는 ",c, "입니다.")