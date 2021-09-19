from typing import List

class Solution:
    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        
        self.obstacleGrid = obstacleGrid

        return self.recur_path_find([0,0])

    def recur_path_find(self, loc):

        row = loc[0]
        col = loc[1]

        if len(self.obstacleGrid) <= row or len(self.obstacleGrid[0]) <= col or self.obstacleGrid[row][col] == 1:
            return 0
        elif row == len(self.obstacleGrid)-1 and col == len(self.obstacleGrid[0])-1:
            return 1
        else:
            return self.recur_path_find([row +1, col]) + self.recur_path_find([row, col + 1])


    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        tmp_map = [[0 for i in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        tmp_map[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                
                if obstacleGrid[i][j] != 1:
                    if i == 0 and j == 0:
                        continue
                    elif i == 0:
                        tmp_map[i][j] = tmp_map[i][j - 1]
                    elif j == 0:
                        tmp_map[i][j] = tmp_map[i - 1][j]
                    else:
                        tmp_map[i][j] = tmp_map[i - 1][j] + tmp_map[i][j - 1]
        from pprint import pprint

        pprint(tmp_map)

        return tmp_map[-1][-1]



if __name__ == "__main__":

    a = [[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]]
    b = [[0,0,0],[0,1,0],[0,0,0]]
    s = Solution()

    print(f"{s.uniquePathsWithObstacles(b)}")