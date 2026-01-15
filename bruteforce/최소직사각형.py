"""
명함 지갑을 만드는 회사에서 지갑의 크기를 정하려고 한다
모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하는 solution 함수 작성

제한사항
- sizes의 길이는 1 이상 10,000 이하
- sizes의 원소는 [w,h] 형식
- w는 명함의 가로 길이,  h는 명함의 세로 길이
- w와 h는 1 이상 1,000 이하인 자연수
"""
sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

def solution(sizes):
    # 높이, 넓이들을 저장할 리스트
    widths, heights = [], []

    for size in sizes:
        # 각 명함의 최대값을 높이에, 최소값을 넓이에 저장
        widths.append(min(size))
        heights.append(max(size))

    # 높이와 넓이의 최대값 곱하기
    return max(widths) * max(heights)

print(solution(sizes))