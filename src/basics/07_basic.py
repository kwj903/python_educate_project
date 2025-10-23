# 7단계: 세트(set) – 중복 없는 무작위 컬렉션 연습문제
# 실전에서의 세트 활용 : 1.중복 제거, 필터링 2.조건에 맞는 유일한 데이터만 저장 3.딕셔너리의 키 체크와 함께 빠른 비교 연산 4.태그/카테고리 시스템 구현

# 연습문제1 중복된 요소가 있는 리스트를 set으로 바꾸고 중복을 제거하세요.
num_list = list([1, 2, 3, 3, 2, 4, 5, 5, 4])
print(num_list)
num_set = set(num_list)
print(num_set)

# 연습문제2 두 개의 집합을 만들고, 합집합, 교집합, 차집합을 출력해보세요.
set_a = {1, 2, 3, 4, 5}
set_b = set([4, 5, 6, 6, 7, 7, 8])
print("합집합: ", set_a.union(set_b))
print("합집합: ", set_a | set_b)
print("교집합: ", set_a.intersection(set_b))
print("교집합: ", set_a & set_b)
print("차집합: ", set_a.difference(set_b))
print("차집합: ", set_a - set_b)

# 연습문제3 세트에 값을 추가하고, 제거하는 방법을 사용해보세요.
set_c = {x for x in range(1, 100) if x % 2 != 0 and x % 3 != 0}
print(set_c)
set_c.add(100)
print(set_c)
set_c.remove(1)
print(set_c)
