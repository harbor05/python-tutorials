#OPERATOR
print(1 + 1)
print(3 - 2)
print(6/3)
print(2**3)

#나머지 값
print(5%3)
print(10%3)
#몫 구하기
print(5//3) 
print(10//3)
#true
print(10 > 3) 
print( 4>= 7)

print(3 == 3) #true
print(4 == 2) #false

print(1 != 3) #true
print(not (1 !=3 )) #false

print((3 > 0) and (3 < 5)) #true(모두 만족할 때)
print((3> 0) & (3 < 5)) #true(둘중 하나라도 다르면 False)

print((3 > 0) or (3 > 5)) #ture(하나라도 true 이면 true)
print((5 > 4 > 3)) #true
print((5 > 4 > 7)) #false

#FORMULA
print(2 + 3 * 4)
print((2 + 3) * 4)

number = 2 + 3 * 4
print(number)

number = number + 2
print(number)

number += 2
print(number)

number *= 2
print(number)

number /= 2
print(number)

number -= 2
print(number)

number %= 2 #나머지
print(number)

#FUNCTION
print(abs(-5)) #절대값
print(pow(4, 2)) #4^2
print(max(5, 12))
print(min(5, 12))
print(round(3.14)) #반올림

from math import * #math 라이브러리 안에 모든 것을 사용한다.
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #제곱근

#RANDOM FUNCTION
from random import *
print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) #0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) #0~10미만의 임의의 값 생성
print(int(random() * 10) + 1) #1 ~ 10이하의 임의의 값 생성
print(int(random() * 45) + 1) #1 ~ 45이하의 임의의 값 생성
print(randrange(1, 46)) #1 ~ 46미만의 임의의 값 생성
print(randint(1, 45)) #1 ~ 45이하의 임의의 값 생성


date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월"+ str(date) + "일로 선정되었습니다.")