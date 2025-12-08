"""
코니는 매일 다른 옷을 조합하여 입는 것을 좋아함

코니는 각 종류별로 최대 1가지 의상만 착용할 수 있다
착용한 의상 일부가 겹치더라도 다른 의상이 겹치지 않거나 혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법으로 의상을 착용한 것으로 간주
코니는 하루의 최소한 한 개 이상의 의상을 입는다
코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합 수를 return 하도록 하는 solution 함수 작성

제한 사항
1. 코니가 가진 의상의 수는 1개 이상 30개 이하
2. 같은 이름을 가진 의상은 존재하지 않습니다.
3. clothes의 모든 원소는 문자열로 이루어져 있습니다.
4. 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
"""
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

def solution(clothes):
    dic = {}
    # 옷과 종류를 딕셔너리에 저장
    for cloth in clothes:
        # 특정 옷은 리스트 안에 저장
        dic.setdefault(cloth[1], []).append(cloth[0])

    # 기본값 1
    ans = 1
    # 모든 종류에 대하여 해당 종류에서 옷을 고르지 않을 경우까지 고려하여 옷의 개수 + 1을 곱해준다
    for key, value in dic.items():
        ans *= (len(value) + 1)
    # 1개 이상의 의상을 입으므로 해당 경우 제외
    return ans - 1

print(solution(clothes))