"""
다음 규칙에 따라 프로세스를 관리할 경우 특정 프로세스가 몇 번째로 실행되는지 알아내기

1. 실행 대기 큐에서 대기 중인 프로세스를 하나 꺼내기
2. 큐에 대기 중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣기
3. 큐에 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행
    3-1. 한 번 꺼낸 프로세스는 다시 큐에 넣지 않고 그대로 종료

큐에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities
실행 순서를 알고 싶은 프로세스의 위치 location

제한사항
- priorities의 길이는 1 이상 100 이하입니다.
    - priorities의 원소는 1 이상 9 이하의 정수입니다.
    - priorities의 원소는 우선순위를 나타내며 숫자가 클 수록 우선순위가 높습니다.
- location은 0 이상 (대기 큐에 있는 프로세스 수 - 1) 이하의 값을 가집니다.
    - priorities의 가장 앞에 있으면 0, 두 번째에 있으면 1 … 과 같이 표현합니다.
"""

priorities = [2, 1, 3, 2]
location = 2

from collections import deque

def solution(priorities, location):
    queue = deque([])

    # 인덱스와 우선순위를 함께 새로운 큐에 저장
    for index, priority in enumerate(priorities):
        queue.append((index, priority))

    # 실행 횟수 저장
    cnt = 0

    while queue:
        # 큐에서 작업을 꺼내기
        current_process = queue.popleft()

        # 현재 프로세스의 인덱스와 우선순위
        current_location = current_process[0]
        current_priority = current_process[1]

        # 큐에 우선순위가 더 높은 프로세스가 있는지 탐색
        for index, priority in queue:
            # 우선순위가 더 높은 프로세스가 있다면 큐에 현재 프로세스를 추가 후 바로 break
            if priority > current_priority:
                queue.append(current_process)
                break
        # 없다면 실행 횟수 증가
        else:
            cnt += 1
            # 만약 해당 프로세스가 목표 프로세스라면 실행 횟수를 바로 return
            if current_location == location:
                return cnt
    return cnt

print(solution(priorities, location))