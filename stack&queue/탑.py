"""
일직선 위에 N개의 높이가 서로 다른 탑을 수평 직선의 왼쪽부터 오른쪽 방향으로 차례대로 세우고, 각 탑의 꼭대기에 레이저 송신기를 설치
모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사
하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신 가능

제한 사항
- 탑의 수를 나타내는 정수 N
- N은 1 이상 500,000 이하
- 탑들의 높이는 1 이상 100,000,000 이하의 정수
"""
import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))

# 탑의 높이와 인덱스를 새로운 리스트에 저장
towers_with_index = []
for index, tower in enumerate(towers):
    towers_with_index.append((index + 1, tower))

# 정답을 저장할 리스트(기본값 0)
answer = [0] * len(towers)

# 탑의 높이를 비교할 스택
stack = []

# 타워를 왼쪽부터 꺼내보며 비교
for current_index, current_tower in towers_with_index:
    # 현재 타워의 높이가 스택(왼쪽에 있는 타워) 제일 위에 있는 타워의 높이보다 같거나 높아질 때까지 버리기
    while stack and stack[-1][1] <= current_tower:
        stack.pop()
    # 스택에 남아있는 타워가 있다면 제일 위에 있는 타워가 수신받은 타워
    # 스택이 비어있다면 받은 타워가 없으므로 기본값 0
    if stack:
        answer[current_index - 1] = stack[-1][0]

    # 현재 타워를 스택에 추가
    stack.append((current_index, current_tower))

print(*answer)