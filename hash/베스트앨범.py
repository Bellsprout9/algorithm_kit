"""
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 2개씩 모아 베스트 앨범을 출시

노래를 수록하는 기준
1. 속한 노래가 가장 많이 재생된 장르를 먼저 수록
2. 장르 내에서 가장 많이 재생된 노래를 먼저 수록
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록

베스트 엘범에 들어갈 노래의 고유 번호를 순서대로 return 하는 solution 함수

제한 사항
1. genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
2. 장르 종류는 100개 미만입니다.
3. 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
4. 모든 장르는 재생된 횟수가 다릅니다.
"""
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    # 장르 별 총 재생 횟수를 저장
    sum_play = {}
    for i in range(len(genres)):
        sum_play[genres[i]] = sum_play.setdefault(genres[i], 0) + plays[i]

    # 각 노래의 재생 횟수를 인덱스와 함께 저장
    each_play = {}
    for i in range(len(genres)):
        each_play.setdefault(genres[i], []).append((i, plays[i]))

    # 장르의 총 재생 횟수를 기준으로 장르를 정렬
    genres_sorted = sorted(sum_play.keys(), key=lambda g: sum_play[g], reverse=True)

    answer = []
    # 재생 수가 많은 장르 순서대로 재생 수 상위 두 개 곡을 차례대로 리스트에 append
    for g in genres_sorted:
        songs = sorted(each_play[g], key=lambda x: (-x[1], x[0]))
        for idx, _ in songs[:2]:
            answer.append(idx)

    return answer

print(solution(genres, plays))