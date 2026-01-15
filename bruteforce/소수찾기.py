"""
한 자리 숫자가 적힌 종이 조각이 흩어져 있다
흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내자
각 종이조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇개인지 return하는 solution 함수

제한사항
- numbers는 길이 1 이상 7 이하의 문자열
- numbers는 0~9까지의 숫자
"""
numbers = "011"

from itertools import permutations

def solution(numbers):
    answer = 0
    lst = [n for n in numbers]
    dic = {}

    # 모든 순열의 경우 구하기
    for r in range(1, len(lst) + 1):
        for per in permutations(lst, r):
            num = ''.join(per)
            # 1이하이거나 이미 계산했던 수라면 패스
            if num[0] == "0" or num == "1" or num in dic:
                continue

            # 소수인지 계산 후 소수라면 answer += 1, 그렇지 않다면 패스
            num = int(num)
            for n in range(2, (num // 2) + 1):
                if num % n == 0:
                    break
            else:
                answer += 1

            # 딕셔너리에 계산한 수 넣어주기
            dic[str(num)] = 1
    return answer

from math import sqrt

def solution(numbers):
    nums = set()

    def dfs(curr, ans):
        # 현재 붙인 문자열이 있다면 int로 바꾸어 세트에 추가
        if ans:
            nums.add(int(ans))

        # 가능한 모든 경우의 수를 재귀로 탐색
        for i in range(len(curr)):
            dfs(
                # 재귀함수의 매개변수를 현재 문자열을 제외한 문자열과 현재 이어붙인 문자열로 갱신
                curr[:i] + curr[i+1:],
                ans + curr[i]
            )

    # dfs 실행
    dfs(numbers, "")

    # 소수의 개수를 세는 변수
    cnt = 0

    # set에서 숫자를 하나씩 꺼내서 소수 판별
    for num in nums:
        if num <= 1:
            continue
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            cnt += 1

    return cnt

print(solution(numbers))