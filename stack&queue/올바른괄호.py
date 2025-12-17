"""
( 또는 ) 로만 이루어진 문자열 s가 주어졌을 때 문자열 s가 올바른 괄호이면 true를, 그렇지 않으면 false를 return하는 solution 함수를 완성

제한사항
- 문자열 s의 길이 : 100,000 이하의 자연수
- 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
"""
s = "(())()"

def solution(s):
    # 문자열의 시작이 닫는 괄호이거나 문자열의 끝이 여는 괄호거나 문자열의 길이가 홀수라면 바로 false return
    if s[0] == ")" or s[-1] == "(" or len(s) % 2 == 1:
        return False

    # 여는 괄호를 담을 리스트
    lst = []

    # 문자열을 순회하며 여는 괄호라면 리스트에 추가, 닫는 괄호라면 뒤에서부터 여는 괄호를 지우기
    for char in s:
        if char == "(":
            lst.append(char)
        # 닫는 괄호 차례인데 리스트가 비어있다면 짝이 맞지 않는 것이므로 바로 False return
        elif char == ")" and not lst:
            return False
        elif char == ")" and lst:
            lst.pop()

    # 리스트가 비어있으면 짝이 맞고, 아니라면 짝이 맞지 않는 것
    return len(lst) == 0


print(solution(s))

