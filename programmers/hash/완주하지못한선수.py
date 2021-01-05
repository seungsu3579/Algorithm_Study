# 완주하지 못한 선수


def solution(participant, completion):

    participant_map = dict()
    answer = ""

    # count participant
    for man in participant:
        participant_map[man] = participant_map.get(man, 0) + 1

    # remove completion
    for man in completion:
        participant_map[man] -= 1

    # find who couldn't complete
    for man, _ in participant_map.items():
        if _ != 0:
            answer = man
    return answer
