"""
H-index는 과학자의 생산성과 영향력을 나타내는 지표
어느 과학자의 H-index를 나타내는 값인 h를 구하려고 한다

H-index를 구하는 법
- 어떤 과학자가 발표한 논문 n편
- h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용
- h의 최대값이 이 과학자의 H-index

어떤 과학자가 발표한 논문의 인용 횟수를 담은 베열 citations가 매개변수로 주어질 때, 이 과학자의 H-index를 return 하는 solution 함수

제한 사항
- 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하
- 논문별 인용 횟수는 0회 이상 10,000회 이하
"""
citations = [6, 4, 3, 1]

def solution(citations):
    # 내림차순 정렬
    citations.sort(reverse=True)

    # h-index 초기값
    h_index = 0

    # index를 기준으로 각 논문에 대해 계산
    for i in range(len(citations)):
        # 해당 논문이 i + 1(해당 논문보다 인용수가 많거나 같은 논문의 수) 보다 크거나 같다면 h-index 갱신
        if citations[i] >= i + 1:
            h_index = i + 1

    return h_index

print(solution(citations))