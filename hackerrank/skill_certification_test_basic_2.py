def possibleChanges(usernames):

    answer = []
    for name in usernames:

        base = name[0]
        flag = "NO"
        for ch in name:
            if ch >= base:
                flag = "NO"
            else:
                flag = "YES"
                break
            base = ch
        answer.append(flag)

    return answer

