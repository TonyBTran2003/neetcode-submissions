class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0
        def dfs(row, col):
            if ( row < 0 or row >= rows or
                col < 0 or col >= cols or
                grid[row][col] == "0" or
                (row, col) in visited
                ):
                return
            
            visited.add((row, col))
            
            dfs(row + 1, col)  # down
            dfs(row - 1, col)  # up
            dfs(row, col + 1)  # right
            dfs(row, col - 1)  # left



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    num_islands += 1
                    dfs(row, col)

        return num_islands

