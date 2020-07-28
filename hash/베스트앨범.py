# 베스트 앨범


def solution(genres, plays):
    answer = []
    song_map = dict()
    for i in range(len(plays)):
        tmp = song_map.get(genres[i], [0])
        tmp.append((i, plays[i]))
        tmp[0] += plays[i]
        song_map[genres[i]] = tmp

    # sort
    sorted_list = sorted(list(song_map.values()), key=lambda songs: -songs[0])

    for songs in sorted_list:
        songs.pop(0)
        songs = sorted(songs, key=lambda song: -song[1])

        answer.append(songs[0][0])
        if len(songs) != 1:
            answer.append(songs[1][0])

    return answer
