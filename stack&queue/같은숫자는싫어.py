"""
배열 arr에서 연속적으로 나타내는 숫자는 하나만 남기고 전부 제거하려고 합니다
단, 제거된 후 남은 수들을 반환할 때는 배열 arr 원소들의 순서를 유지해야 합니다
배열 arr에서 연속적으로 나타내는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 작성

제한사항
- 배열 arr의 크기: 1,000,000 이하의 자연수
- 배열 arr 원소의 크기: 0보다 크거나 같고 9보다 작거나 같은 정수
"""
arr = [1,1,3,3,0,1,1]

def solution(arr):
    # 연속되지 않는 숫자를 담을 리스트
    answer = []

    # arr 리스트에 있는 숫자를 하나씩 꺼내서 answer 리스트와 비교
    for num in arr:
        # 맨 처음에는 아무 숫자도 없기 때문에 answer 리스트의 길이가 0이면 그냥 추가
        if len(answer) == 0:
            answer.append(num)
        # answer 리스트의 맨 뒷자리 숫자가 현재 숫자와 같지 않으면 연속하지 않으므로 answer 리스트에 추가
        else:
            if answer[-1] != num:
                answer.append(num)
    return answer

print(solution(arr))