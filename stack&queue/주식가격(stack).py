"""
초 단위로 기록된 주식 가격이 담긴 배열 prices
가격이 떨어지지 않은 기간은 몇 초인지 return

제한사항
- prices의 각 가격은 1 이상 10,0000 이하 자연수
- prices의 길이는 2 이상 100,000 이하
"""
prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = [0] * len(prices)

    stack = []
    # 순서대로 가격들을 순회하면서 스택의 마지막 수와 비교
    for current_index, current_price in enumerate(prices):
        # 스택에 맨 위에 있는 가격이 현재 가격보다 크다면 스택 맨 위에 있는 가격은 떨어진 것
        while stack and stack[-1][1] > current_price:
            # 떨어진 가격은 필요 없으므로 pop
            index, _ = stack.pop()
            # 떨어진 기간을 기록
            answer[index] = current_index - index

        # 현재 가격을 스택에 추가
        stack.append((current_index, current_price))

    # 스택에 남아있는 가격은 끝까지 떨어지지 않은 가격이므로 계산해서 기록
    for index, price in stack:
        answer[index] = len(prices) - index - 1

    return answer

print(solution(prices))