"""
0 또는 양의 정수가 주어졌을 때, 정수를 이어붙여 만들 수 있는 가장 큰 수를 return

제한사항
- numbers의 길이는 1 이상 100,000 이하
- numbers의 원소는 0 이상 1,000 이하
- 정답이 너무 클 수 있으니 문자열로 바꾸어 return
"""

numbers = [3, 30, 34, 5, 9]

def solution(numbers):
    # 리스트의 숫자를 문자열로 바꾸어 비교 후 내림차순 정렬
    arr = sorted(numbers, key=lambda x:str(x) * 3, reverse=True)

    # 가장 큰 숫자가 0이라면 모든 숫자가 0이므로 0 리턴
    if arr[0] == 0:
        return '0'

    # 리스트의 숫자를 문자열로 바꾸어주기
    arr = map(str, arr)

    # 모두 붙여 리턴
    return ''.join(arr)


from functools import cmp_to_key

def compare(x, y):
    # 문자열 그대로 붙이기
    t1 = x + y
    t2 = y + x

    # 정수로 변환하여 비교
    if int(t1) > int(t2):
        return -1
    else:
        return 1



def solution(numbers):
    # 리스트 문자열로 변화
    numbers = map(str, numbers)
    # compare 함수대로 정렬
    numbers = sorted(numbers, key=cmp_to_key(compare))

    # 가장 큰 숫자가 0이라면 모든 숫자가 0이므로 0 리턴
    if numbers[0] == "0":
        return "0"

    # 모두 붙여 리턴
    return ''.join(numbers)


print(solution(numbers))