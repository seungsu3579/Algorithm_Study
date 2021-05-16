# https://www.acmicpc.net/problem/9251

def solution():
    str1 = input()
    str2 = input()
    matrix = [[0 for i in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            if i == 0 or j == 0:                
                matrix[i][j] = 0
            else:
                tmp = matrix[i - 1][j - 1]
                if str1[i-1] == str2[j-1]:
                    tmp += 1
                matrix[i][j] = max(tmp, matrix[i-1][j], matrix[i][j-1])
    
    return matrix[len(str1)][len(str2)]

if __name__ == "__main__":
    print(solution())