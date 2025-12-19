"""
초 단위로 기록된 주식 가격이 담긴 배열 prices
가격이 떨어지지 않은 기간은 몇 초인지 return

제한사항
- prices의 각 가격은 1 이상 10,0000 이하 자연수
- prices의 길이는 2 이상 100,000 이하
"""
prices = [1, 2, 3, 2, 3]

from collections import deque

def solution(prices):
    answer = []

    prices = deque(prices)

    while prices:
        # 맨 앞에서 현재 가격 꺼내기
        current_price = prices.popleft()

        period = 0

        if prices:
            # 가격이 떨어지지 않았다면 기간 추가
            for price in prices:
                if current_price <= price:
                    period += 1
                # 떨어졌다면 기간 추가하고 바로 break
                else:
                    period += 1
                    break
            # 가격이 떨어지지 않는 기간 추가
            answer.append(period)
        # 마지막 숫자일 경우 0 추가
        else:
            answer.append(0)

    return answer

print(solution(prices))