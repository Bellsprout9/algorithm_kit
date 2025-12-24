"""
하드디스크는 한 번에 하나의 작업만 수행할 수 있다
우선순위 디스크라는 가상의 장치를 사용한다고 가정
- 어떤 작업이 들어왔을 때 작업의 번호, 요청 시각, 소요 시간을 저장해두는 대기큐
- 하드디스크가 작업을 하고 있지 않고 대기 큐가 비어있지 않다면 우선순위가 높은 작업을 대기 큐에서 꺼내서 하드디스크에 작업을 시킨다.
- 작업의 소요시간이 짧은 것, 작업의 요청시각이 빠른 것, 작업의 번호가 작은 것 순으로 우선순위가 높다
- 하드디스크는 작업을 한 번 시작하면 해당 작업을 마칠 때까지 그 작업만 수행한다
- 하드디스크는 작업을 마치자마자 다른 작업을 시작할 수 있다 이 과정에서 걸리는 시간은 없다고 가정

모든 요청 작업을 마쳤을 때 각 작업에 대한 반환 시간은 작업 요청부터 종료까지 걸린 시간으로 정의
모든 요청 작업의 반환 시간의 평균 정수 부분을 return 하는 solution 함수를 작성

제한 사항
- 1 ≤ jobs의 길이 ≤ 500
- jobs[i]는 i번 작업에 대한 정보이고 [s, l] 형태입니다.
- s는 작업이 요청되는 시점이며 0 ≤ s ≤ 1,000입니다.
- l은 작업의 소요시간이며 1 ≤ l ≤ 1,000입니다.
"""
jobs = [[0, 3], [1, 9], [3, 5]]

from heapq import heappop, heappush, heapify

def solution(jobs):
    # 초기 작업 개수 저장
    job_len = len(jobs)
    # 현재 시간
    time = 0
    # 작업 대기 큐
    queue = []
    # 하드디스크
    working = []
    # 작업 요청 시간부터 종료 시간까지 걸린 시간의 총합
    answer = 0

    # 작업 리스트에 인덱스 추가
    for i in range(len(jobs)):
        jobs[i].append(i)

    # 힙으로 변경(작업 요청 시간 기준 정렬)
    heapify(jobs)

    # 모든 작업이 끝날 때까지 실행
    while queue or jobs or working:
        # 각 시간마다 이전에 요청된 작업을 대기 큐에 추가
        while jobs:
            # 요청 시간이 가장 빠른 작업 꺼내기
            curr_job = heappop(jobs)
            # 현재 시간 혹은 이전 시간에 요청된 작업이라면 우선순위에 맞춰 작업 대기 큐에 추가
            if curr_job[0] <= time:
              heappush(queue, (curr_job[1], curr_job[0], curr_job[2]))
            # 이후 요청이라면 다시 힙에 넣고 바로 break
            else:
                heappush(jobs, curr_job)
                break

        # 현재 하드디스크에 작업이 있다면
        if working:
            # 작업 종료 시점이 현재 시간과 같다면 작업 종료
            if working[0][0] == time:
                # 요청부터 종료까지 걸린 시간 추가
                answer += (time - working[0][1])
                # 하드디스크에서 제거
                working.pop()
                # 대기 큐에 작업이 있다면 가장 우선순위가 높은 작업을 꺼내 종료 예상 시간과 요청 시간을 저장
                if queue:
                    working_time, requested_time, _ = heappop(queue)
                    working.append((working_time + time, requested_time))
        # 하드디스크에 작업이 없다면
        else:
            # 대기 큐에 작업이 있다면 가장 우선순위가 높은 작업을 꺼내 종료 예상 시간과 요청 시간을 저장
            if queue:
                working_time, requested_time, _ = heappop(queue)
                working.append((working_time + time, requested_time))
        # 각 순회마다 시간 1씩 증가
        time += 1
    # 요청부터 종료까지 걸린 시간 평균의 몫
    return answer // job_len

print(solution(jobs))