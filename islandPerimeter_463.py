class Solution:
    def islandPerimeter(self, grid: 'List[List[int]]') -> 'int':
        count = 0
        row_sum = []
        for i in range(len(grid)):
            row_sum.append(sum(grid[i]))
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if j < len(grid[i])-1 and grid[i][j+1] == 1:
                        count += 1
                    if i < len(grid)-1 and grid[i+1][j] == 1:
                        count += 1
        # print(sum(row_sum))
        return 4*sum(row_sum) - 2*count
s = Solution()
g = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(s.islandPerimeter(g))

