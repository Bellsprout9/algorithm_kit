"""
전화번호부에 있는 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false, 그렇지 않으면 true를 return 하는 solution 함수 작성

제한 사항
1. phone_book의 길이는 1 이상 1,000,000 이하
2. 각 전화번호의 길이는 1 이상 20 이하
3. 같은 전화번호가 중복해서 들어있지 않습니다.
"""

phone_book = ["12","123","1235","567","88"]

def solution(phone_book):
    dic = {}

    # 핸드폰 번호를 딕셔너리에 저장
    for phone_number in phone_book:
        dic[phone_number] = 1

    # 모든 핸드폰 번호에 대해서 숫자를 하나씩 더해가며 딕셔너리에 일치하는 key가 있는지 비교
    for phone_number in phone_book:
        compare = ''
        for num in phone_number:
            compare += num
            # 만약에 일치하는 숫자가 있고 그 숫자가 해당 핸드폰 번호가 아니라면 접두어가 있는 것이므로 바로 False Return
            if compare in dic and compare != phone_number:
                return False
    # 만족하는 경우가 없다면 True return
    return True

print(solution(phone_book))