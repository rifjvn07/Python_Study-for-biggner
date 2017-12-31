#121522 윤석 BMI측정하기
#함수를 정의하는 방식에 대해 알 수 있었다.

## 함수 정의 부분	
def BMI(w,t):
	result = w/(float(t)**2)
	return result
	
	
## 변수 선언 부분
bmi = 0.0
w = 0.0
t = 0.0

## 메인 코드 부분
t = float(input("키(cm)를 입력하세요: "))
w = float(input("몸무게(kg)를 입력하세요: "))
bmi = BMI(w,t/100.0)

#소수 둘째자리까지 표현
print("당신의 BMI: %.2f" %bmi )
