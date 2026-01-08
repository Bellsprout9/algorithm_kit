"""
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때 k번째에 있는 숫자를 구하려 한다
배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수

제한 사항
- array의 길이는 1 이상 100 이하
- array의 각 원소는 1 이상 100 이하
- commands의 길이는 1 이상 50 이하
- commands의 각 원소는 길이가 3
"""
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command
        # 배열 깊은 복사
        new_array = array[:]
        # 명령대로 자르기
        sliced_array = new_array[i - 1:j]
        # 정렬하기
        sliced_array.sort()
        # k번째 요소 리스트에 추가하기
        answer.append(sliced_array[k - 1])

    return answer

print(solution(array, commands))