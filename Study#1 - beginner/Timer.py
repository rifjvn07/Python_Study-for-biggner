#시간초 받아 시간으로 변환하기.

#시간초 받기
print("시간초를 입력하세요. ")
time = int(input())

#시,분,초 변환하기
#Hint 1시간 = 3600초

hour = time // 3600
min = (time%3600)//60
sec = (time%60)
print(hour, "시간", min,"분", sec, "초")

