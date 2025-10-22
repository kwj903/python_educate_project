from random import randint
# 조건문과 논리 연습문제

# 연습문제1
x = 15
if x > 10 and x < 20 :
  print("10보다 크고 20보다 작다")
  
# 연습문제2
score = randint(0, 100)
if score >= 90 :
  print("A")
elif score >= 80 :
  print("B")
elif score >= 70 :
  print("C")
else :
  print("F")

# 연습문제3
user_input = int(input("숫자를 입력하세요: "))

if user_input%2 == 0 :
  print("짝수입니다.")
else :
  print("홀수입니다.")
