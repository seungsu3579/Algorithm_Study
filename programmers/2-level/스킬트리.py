def solution(skill, skill_trees):
    answer = 0
    stack = []
    for i in range(len(skill) - 1, -1, -1):
        stack.append(skill[i])

    for skill_tree in skill_trees:
        check = stack[:]

        for i in range(len(skill_tree)):
            if skill_tree[i] in check:
                if check[-1] != skill_tree[i]:
                    answer -= 1
                    break
                else:
                    check.pop()

        answer += 1

    return answer


a = solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])
print(a)
