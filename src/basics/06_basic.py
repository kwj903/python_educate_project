# 6단계: 딕셔너리 – 파이썬의 작은 데이터베이스 연습문제

# 연습문제1 이름, 나이, 직업을 담은 딕셔너리를 만들고 출력하세요.
person = {
  "name" : "곽우재",
  "age" : 35,
  "job" : "프로그래머"
}
print(person)
print(person.keys())
print(person.values())
print(person.items())

# 연습문제2 키 "age"의 값을 수정해보세요.
person["age"] = 33
print(person)

# 연습문제3 딕셔너리에 "hobby": "코딩" 항목을 추가하고, 전체를 출력하세요.
person["hobby"] = "코딩"
print(person)

# 연습문제4 키 "name"을 삭제하고 결과를 출력하세요.
del person["name"]
print(person)

