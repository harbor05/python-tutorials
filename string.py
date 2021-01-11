#string
sentence = '나는 나입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print (sentence2)

sentence3 = """
나는 30살이고
파이썬은 흠..
"""
print(sentence3)

#slicing

jumin = "990000-1234567"

print("성별:" + jumin[7])
print("연:" + jumin[0:2]) #0부터 2직전까지
print("월:" + jumin[2:4])
print("일:" + jumin[4:6])
print("생년월일" + jumin[0:6])
print("생년월일" + jumin[:6])
print("뒤 7자리" + jumin[7:])
print("뒤 7자리 뒤에서부터" + jumin[-7:])

#functions
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)

index = python.index("n", index + 1) #2번째 n
print(index)

print(python.find("Python"))

# print(python.index("Java"))  > error

print(python.count("n"))

#string format

#1
print("나는 %d살 입니다" %30) #d는 정수
print("나느 %s을 좋아해요" %"python") #문자열
print("Apple은 %c로 시작해요" %"A") #character

print("나는 %s색과 %s색을 좋아해요" %("검정","빨강"))

#2
print("나는 {}살 입니다" .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))

#3
print("나는 {age}살이며, {color}색을 좋아해요" .format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요" .format(color = "빨강", age=16))

#4
age = 31
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요")


#Escape
print("백문이 불여일견 동해물\n과백두산")
print("백문이 불여일견 '동해물과' 백두산")
print("백문이 불여일견 \"동해물과\" 백두산") #\ 두개(\\)는 하나로 처리
# \r은 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b 는 한글자를 지움
print("Redd\bApple")

# \t는 탭
print("Red\tApple")

#quiz
url = "http://google.com"

domain = url.replace("http://","")
domain = domain[:domain.index(".")]
password = domain[0:3] + str(len(domain)) + str(domain.count("e")) + "!"

print("{0}의 비밀번호는 {1} 입니다." .format(url, password))