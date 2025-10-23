# 4단계: 리스트와 자료구조의 시작 연습문제

# 연습문제1 : 문자열 "사과,바나나,딸기"를 split()을 이용해서 리스트로 바꿔보세요.
fruits = "사과, 바나나, 딸기".split(", ")
print(fruits)

# 연습문제2 : 과일 목록 리스트에서 마지막 요소를 삭제하고, 첫 번째 요소를 출력하세요.
result = fruits.pop()
print(fruits)
print(fruits[0])
print(result)
print(len(fruits))
print(len(result))

# 연습문제3 : 숫자 리스트 [1, 2, 3, 4, 5]를 반복문으로 돌며, 짝수만 출력해보세요.
num = [i for i in range(1, 6)]
print(num)
for i in num :
  if i % 2 == 0 :
    print(i)

