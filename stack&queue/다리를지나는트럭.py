"""
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 한다
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내기

다리에는 트럭이 최대 bridge_lenth대 올라갈 수 있다
다리는 weight 이하까지의 무게를 견댈 수 있다
단, 다리에 완전히 오르지 않는 트럭의 무게는 무시

모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return

제한조건
- bridge_length는 1 이상 10,000 이하입니다.
- weight는 1 이상 10,000 이하입니다.
- truck_weights의 길이는 1 이상 10,000 이하입니다.
- 모든 트럭의 무게는 1 이상 weight 이하입니다.
"""
bridge_length = 100
weight = 100
truck_weights = [10]

from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 최대 길이만큼의 다리 리스트
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    time = 0
    current_weight = 0

    while bridge:
        # 시간 저장
        time += 1

        # 다리의 맨 앞에 있는 요소를 빼서 현재 다리 무게 총합 갱신
        current_weight -= bridge.popleft()

        if truck_weights:
            # 현재 다리의 합과 대기열 맨 앞 트럭의 무게의 합이 최대 무게보다 작으면 해당 트럭을 다리 위에 올릴 수 있다
            if current_weight + truck_weights[0] <= weight:
                # 대기열에서 트럭을 빼서 다리에 올리기
                truck = truck_weights.popleft()
                bridge.append(truck)
                # 다리 무게 갱신
                current_weight += truck
            # 대기열 맨 앞의 트럭을 올릴 수 없다면 시간만 흐르므로 0 추가
            else:
                bridge.append(0)

    return time



print(solution(bridge_length, weight, truck_weights))
