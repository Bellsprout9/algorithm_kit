"""
모든 음식의 스코빌 지수를 K 이상으로 만들고 싶다
스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같은 방식으로 섞어 새로운 음식을 만든다

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞는다
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하는 solution 함수

제한 사항
- 모든 음식의 스코빌 지수를 담은 배열 scovile
- 원하는 스코빌 지수 K
- scovile의 길이는 2 이상 1,000,000 이하
- K는 0 이상 1,000,000,000 이하
- scoville의 원소는 각각 0 이상 1000,000,000 이하
- 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1 리턴
"""
scoville = [1, 2, 3, 9, 10, 12]
K = 7

from heapq import heapify, heappush, heappop

def solution(scoville, K):
    # 음식 리스트를 힙으로 만들기
    heapify(scoville)
    num = 0

    while scoville:
        # 음식이 하나 남았는데 K에 도달하지 못했다면 도달 할 수 없으므로 -1 return
        if len(scoville) == 1 and scoville[0] < K:
            return -1

        # 최소값이 K 이상이면 요구사항을 달성한 것이므로 요리한 횟수 return
        if scoville[0] >= K:
            return num

        # 힙에서 스코빌 지수가 가장 작은 음식 2개 꺼내기
        first_food = heappop(scoville)
        second_food = heappop(scoville)

        # 새로운 음식 조리
        new_food = first_food + (second_food * 2)

        # 새로운 음식을 힙에 추가
        heappush(scoville, new_food)
        # 요리 횟수 추가
        num += 1

print(solution(scoville, K))