"""
수포자 삼인방은 모의고사에서 수학문제를 전부 찍으려 한다
1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers
가장 많은 문제를 맞춘 사람이 누구인지 배열에 담아 return 하는 solution 함수

수포자는 1번 문제부터 다음과 같이 찍는다
- 1번 수포자: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5 ...
- 2번 수포자: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5 ...
- 3번 수포자: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 ...


제한 사항
- 시험은 최대 10,000 문제
- 문제의 정답은 1, 2, 3, 4, 5 중 하나
- 가장 높은 점수를 받은 사람이 여럿일 경우, return 하는 값을 오름차순 정렬
"""
answers= [1,2,3,4,5]

def solution(answers):
    answer = []

    # 문제 수 최대치까지 찍기 패턴 반복
    first = [1, 2, 3, 4, 5] * 2000
    second = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    first_cnt, second_cnt, third_cnt = 0, 0, 0

    # 각 수포자의 정답 개수 세기
    for i in range(len(answers)):
        if answers[i] == first[i]:
            first_cnt += 1
        if answers[i] == second[i]:
            second_cnt += 1
        if answers[i] == third[i]:
            third_cnt += 1

    # 최대 정답 수
    max_cnt = max(first_cnt, second_cnt, third_cnt)

    # 수포자의 정답 수가 최대 정답수와 같다면 답 리스트에 추가
    if first_cnt == max_cnt:
        answer.append(1)
    if second_cnt == max_cnt:
        answer.append(2)
    if third_cnt == max_cnt:
        answer.append(3)

    # 오름차순 정렬하여 리턴
    return sorted(answer)

print(solution(answers))