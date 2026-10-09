class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row,col))

        while queue:
            row, col = queue.popleft()
            
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (new_row < 0 or new_row >= rows or
                    new_col < 0 or new_col >= cols or
                    grid[new_row][new_col] != 2147483647
                ):
                    continue
                grid[new_row][new_col] = grid[row][col] + 1
                queue.append((new_row, new_col))

        