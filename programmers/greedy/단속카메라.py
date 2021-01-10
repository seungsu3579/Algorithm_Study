# 단속카메라

# 효율성 테스트 통과 X
def solution1(routes):
    answer = 0
    cctv = []

    # record all
    while len(routes) != 0:
        road = [0 for i in range(60001)]
        for route in routes:
            for i in range(route[0], route[1] + 1):
                road[i] += 1

        # find max
        max_loc = road.index(max(road))
        if max_loc >= 30000:
            max_loc = max_loc - 60001

        # add cctv
        cctv.append(max_loc)

        # update routes
        for route in routes[:]:
            if route[0] < 0 and route[1] >= 0:
                if max_loc >= route[0] or max_loc <= route[1]:
                    routes.remove(route)
            else:
                if max_loc >= route[0] and max_loc <= route[1]:
                    routes.remove(route)
    answer = len(cctv)
    return answer


################################################


def check(points, points_dict, dict_route):
    tmp = dict(map(lambda x: (x, 0), points))
    for p in points:
        for key in points_dict[p]:
            tmp[p] += dict_route[key]
    return tmp


def refresh(points_dict, dict_route, idx):
    for route in points_dict[idx]:
        dict_route[route] = 0


# 효율성 테스트 통과 X
def solution2(routes):
    answer = 0
    dict_route = dict(map(lambda x: (tuple(x), 1), routes))

    points = sorted(list(set(sum(routes, []))))
    points_dict = dict(map(lambda x: (x, []), points))

    # 트래픽 v2-1
    # for route in routes:
    #     for i in range(route[0], route[1] + 1):
    #         if points_dict.get(i, None) != None:
    #             points_dict[i].append(tuple(route))

    # 트래픽 v2-2
    for route in routes:
        for p in points:
            if p >= route[0] and p <= route[1]:
                points_dict[p].append(tuple(route))

    cctv = []
    while True:

        tmp = check(points, points_dict, dict_route)

        if sum(list(tmp.values())) == 0:
            break

        max_v = -1
        max_loc = 0
        for key, item in tmp.items():
            if max_v < item:
                max_loc = key
                max_v = item

        if max_loc >= 30000:
            max_loc = max_loc - 60001

        cctv.append(max_loc)
        refresh(points_dict, dict_route, max_loc)

    answer = len(cctv)

    return answer


def solution3(routes):
    answer = 0
    s_routes = sorted(routes, reverse=True, key=lambda x: x[0])

    while True:
        eptr = s_routes[-1][1]

        if len(s_routes) == 1:
            answer += 1
            s_routes.pop()
        else:
            done = False
            for i in range(len(s_routes) - 2, -1, -1):
                if s_routes[i][0] > eptr:
                    answer += 1
                    s_routes = s_routes[: i + 1]
                    done = True
                    break
                else:
                    if s_routes[i][1] < eptr:
                        eptr = s_routes[i][1]

            if not done:
                answer += 1
                break

        if len(s_routes) == 0:
            break

    return answer


if __name__ == "__main__":
    print(f"solution = {solution3([[-20,15], [-14,-5], [-18,-13], [-5,-3]])}")
