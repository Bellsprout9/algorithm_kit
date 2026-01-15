"""
중앙은 노란색으로 칠해져 있고, 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫
Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때
카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하는 solution 함수 작성

제한사항
- 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수
- 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수
- 카펫의 가로 길이 >= 세로 길이
"""
brown = 24
yellow = 24

from math import sqrt

def solution(brown, yellow):
    # yellow의 인수를 담을 리스트
    factors = []

    # yellow 모든 인수 경우의 수를 리스트에 담는다
    for r in range(1, int(sqrt(yellow)) + 1):
        if yellow % r == 0:
            factors.append((r, yellow // r))

    # 바깥 테두리의 길이가 brown과 같아진다면 바로 return
    for h, w in factors:
        if 2 * (h + w) + 4 == brown:
            return [w + 2, h + 2]

print(solution(brown, yellow))