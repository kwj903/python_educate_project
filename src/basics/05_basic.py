# 5단계: 튜플 (tuple) – 변하지 않는 리스트 연습문제

# 연습문제1. 숫자 3개가 들어있는 튜플을 만들고, 두 번째 요소를 출력하세요.
num = 1, 2, 3
print(num[1])
num2 = (1, 2, 3)
print(num2[1])
num3 = tuple([1, 2, 3])
print(num3[1])

# 연습문제2. 튜플에서 값을 바꾸려 하면 어떤 오류가 발생하는지 실험해보세요.
# print(num.append(4))
# print(num2.remove(1))
# print(num3.pop())

# 연습문제3. 튜플을 리스트로 바꾸고, 값을 수정한 뒤 다시 튜플로 바꿔보세요.
list_num = list(num)
print(list_num)
list_num.pop()
print(list_num)
changed_tuple = tuple(list_num)
print(changed_tuple)
