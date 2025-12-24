"""
이중 우선순위 큐는 당므 연산을 할 수 있는 자료 구조를 말한다
- I 명령어 숫자: 큐에 주어진 숫자 삽입
- D 1: 큐에서 최대값 삭제
- D-1: 큐에서 최소값 삭제

이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 모든 연산을 처리한 후 큐가 비어있으면 [0, 0], 비어있지 않으면 [최댓값, 최소값]을 return 하는 solution 함수

제한사항
- operations 는 길이가 1 이상 1,000,000 이하인 문자열 배열
- operations의 원소는 큐가 수행할 연산을 나타낸다
- 최대값, 최소값을 삭제하는 연산에서 최대값 최소값이 둘 이상인 경우, 하나만 삭제
- 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시
"""
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

from heapq import heappop, heappush

def solution(operations):
    # 최대 힙, 최소 힙
    min_heap = []
    max_heap = []
    # 살아있는 숫자를 저장
    count = {}

    for operation in operations:
        # 숫자 추가 명령어일 경우 리스트로 끊어서 최소, 최대 힙에 저장
        if operation[0] == 'I':
            num = int(operation[2:])
            heappush(min_heap, int(num))
            heappush(max_heap, -int(num))
            # 딕셔너리에 추가된 만큼 저장
            count[num] = count.get(num, 0) + 1
        else:
            # 힙에 숫자가 존재하는 경우만 진행
            if min_heap and max_heap:
                # 최대값을 빼는 경우
                if operation == "D 1":
                    while max_heap:
                        # 최대 힙에서 최대값 빼기
                        num = -heappop(max_heap)
                        # 뺀 숫자가 유효한 숫자라면 개수 갱신 후 break
                        if count[num] > 0:
                            count[num] -= 1
                            break
                        # 유효하지 않은 숫자라면 유효한 숫자가 나올 때까지 계속 진행
                        else:
                            continue
                else:
                    # 최소 힙에서 최소값 빼기
                    if operation == "D -1":
                        while min_heap:
                            num = heappop(min_heap)
                            # 뺀 숫자가 유효한 숫자라면 개수 갱신 후 break
                            if count[num] > 0:
                                count[num] -= 1
                                break
                            # 유효하지 않은 숫자라면 유효한 숫자가 나올 때까지 계속 진행
                            else:
                                continue
            # 힙에 숫자가 존재하지 않는다면 다음 순회
            else:
                continue

    # 남아있는 최소, 최대 값
    min_num, max_num = 0, 0

    # 최소값 존재 여부를 판단할 플래그
    min_flag = False
    while min_heap:
        # 최소 힙에서 최소값 꺼내기
        min_num = heappop(min_heap)
        # 유효하지 않은 숫자라면 다음 진행
        if count[min_num] == 0:
            continue
        # 유효한 숫자라면 플래그 전환 후 break
        else:
            min_flag = True
            break

    # 플래그가 False라면 유효한 숫자를 찾지 못한 것이므로 min_num은 기본값 0
    if min_flag == False:
        min_num = 0

    # 최대값 존재 여부를 판단할 플래그
    max_flag = False
    while max_heap:
        # 최대 힙에서 최대값 꺼내기
        max_num = -heappop(max_heap)
        # 유효하지 않은 숫자라면 다음 진행
        if count[max_num] == 0:
            continue
        # 유효한 숫자라면 플래그 전환 후 break
        else:
            max_flag = True
            break

    # 플래그가 False라면 유효한 숫자를 찾지 못한 것이므로 max_num은 기본값 0
    if max_flag == False:
        max_num = 0

    return [max_num, min_num]

print(solution(operations))