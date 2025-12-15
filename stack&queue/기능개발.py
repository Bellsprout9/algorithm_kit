"""
각 기능은 진도가 100%일 때 서비스에 반영 가능
각 기능의 개발속도는 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 배포됨
각 배포마다 몇개의 기능이 배포되는지 return 하는 solution 함수 작성

제한 사항
- 작업의 개수는 100개 이하
- 작업 진도는 100 미만의 자연수
- 작업 속도는 100 이하의 자연수
- 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정
"""

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

from collections import deque

def solution(progresses, speeds):
    # 배포되는 기능의 수를 담을 리스트
    answer = []

    # 리스트를 뒤집기
    progresses = progresses[::-1]
    speeds = speeds[::-1]

    # 기능이 남아있을 동안 실행
    while progresses:
        # 기능의 진행도 더하기
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        # 리스트의 마지막 기능 진행도가 100%가 넘었다면 배포되는 기능의 수를 1로 놓고 진행
        if progresses[-1] >= 100:
            num = 1
            progresses.pop(-1)
            # 그 다음 기능부터 진행도가 100%가 넘으면 빼면서 배포되는 기능의 수에 더하기
            for progress in progresses[::-1]:
                if progress >= 100:
                    num += 1
                    progresses.pop(-1)
                # 그렇지 않으면 바로 break
                else:
                    break

            # 한 턴에 배포되는 기능의 수를 리스트에 추가
            answer.append(num)

    return answer

def solution(progresses, speeds):
    # 배포되는 기능의 수를 담을 리스트
    answer = []

    # 리스트를 deque에 넣기
    progresses = deque(progresses)
    speeds = deque(speeds)

    # 기능이 남아있을 동안 실행
    while progresses:
        # 기능의 진행도 더하기
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        # 리스트의 마지막 기능 진행도가 100%가 넘었다면 배포되는 기능의 수를 0로 놓고 진행
        if progresses[0] >= 100:
            num = 0
            # 진행도가 100%가 넘으면 빼면서 배포되는 기능의 수에 더하기
            while progresses and progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                num += 1

            # 한 턴에 배포되는 기능의 수를 리스트에 추가
            answer.append(num)

    return answer

print(solution(progresses, speeds))