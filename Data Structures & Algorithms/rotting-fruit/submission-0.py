class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0
        fresh = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col))

                elif grid[row][col] == 1:
                    fresh +=1

        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if (new_row < 0 or new_row >= rows or
                        new_col < 0 or new_col >= cols or
                        grid[new_row][new_col] != 1
                        ):
                        continue

                    grid[new_row][new_col] = 2

                    fresh -=1

                    queue.append((new_row,new_col))

            minutes += 1

        if fresh > 0:
            return -1

        return minutes

                
                    
                