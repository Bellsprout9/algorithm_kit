"""
XX게임에서는 일정 피로도를 사용해서 던전을 탐험할 수 있다
각 던전마다 탐험을 시작하기 위해 필요한 "최소 필요 피로도"와
던전 탐험을 마쳤을 때 소모되는 "소모 피로도"가 있다

최소 필요 피로도: 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도
소모 피로도: 던전을 탐험한 수 소모되는 피로도

이 게임에는 하루에 한 번씩 탐험할 수 있는 던전이 여러 개 있는데,
한 유저가 오늘 이 던전들을 최대한 많이 탐험하려고 한다
유저의 현재 피로도 k와 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 이차원 배열 dungeons가 매개변수로 주어질 때,
유저가 탐험할 수 있는 최대 던전 수를 return 하는 solution 함수

제한사항
- k는 1 이상 5,000 이하인 자연수
- dungeons의 세로(행) 길이(즉, 던전의 개수)는 1 이상 8 이하
- dungeons의 각 행은 각 던전의 ["최소 필요 피로도", "소모 피로도"]
- "최소 필요 피로도"는 항상 "소모 피로도"보다 크거나 같다
- "최소 필요 피로도"와 "소모 피로도"는 1 이상 1,000 이하인 자연수
- 서로 다른 던전의 ["최소 필요 피로도", "소모 피로도"]가 서로 같을 수 있다
"""
k = 80
dungeons = 	[[80,20], [50,40], [30,10]]

# 최대 방문 횟수
max_cnt = 0
def solution(k, dungeons):
    # 방문 처리
    visited = [0] * len(dungeons)

    # dfs 돌리기
    def dfs(k, visited, cnt):
        # 최대 방문 횟수 갱신
        global max_cnt
        max_cnt = max(max_cnt, cnt)

        # 던전을 돌면서 조건을 만족하고 방문하지 않았던 던전 방문
        for i in range(len(dungeons)):
            if dungeons[i][0] <= k and visited[i] == 0:
                visited[i] = 1
                # 피로도와 방문 횟수 갱신하여 재귀
                dfs(k - dungeons[i][1], visited, cnt + 1)
                # 방문 기록 백트래킹
                visited[i] = 0

    # 함수 실행
    dfs(k, visited, 0)

    # 최대 방문 횟수 리턴
    return max_cnt

print(solution(k, dungeons))