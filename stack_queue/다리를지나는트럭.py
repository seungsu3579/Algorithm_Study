# 다리를 지나는 트럭


def solution(bridge_length, weight, truck_weights):
    answer = 1
    num_truck = len(truck_weights)
    ing = [[], []]
    finished = []

    while len(finished) != num_truck:
        # truck start crossing bridge
        if len(truck_weights) != 0:
            if sum(ing[0]) + truck_weights[0] <= weight:
                ing[0].append(truck_weights.pop(0))
                ing[1].append(0)

        # truck move
        for i in range(len(ing[1])):
            ing[1][i] += 1

        # check truck crossed bridge
        if len(ing[0]) != 0:
            if ing[1][0] == bridge_length:
                finished.append(ing[0].pop(0))
                ing[1].pop(0)

        answer += 1

    return answer
