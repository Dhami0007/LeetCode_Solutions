import time
def orangesRotting(grid) -> int:
    minutes = 0
    m = len(grid)
    n = len(grid[0])

    queue = list()
    fresh = 0
    rotten = 0
    for i in range(m):
        for j in range(n):
            cell = grid[i][j]
            if cell == 2:
                queue.append((i,j))
                rotten += 1
            elif cell == 1:
                fresh += 1

    adj_finder = [(-1,0),(1,0),(0,-1),(0,1)]

    while len(queue) != 0:
        lim = len(queue)
        found = False
        for k in range(lim):
            a,b = queue.pop(0)
            for direction in adj_finder:
                x,y = direction
                n_x = a+x
                n_y = b+y
                
                if 0 <= n_x < m and 0 <= n_y < n:
                    if grid[n_x][n_y] == 1:
                        grid[n_x][n_y] = 2
                        queue.append((n_x,n_y))
                        rotten  += 1
                        found = True

        if found:
            minutes += 1
    
    
    if fresh - (rotten-1) == 0:
        return minutes
    else:
        return -1


def main():
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(orangesRotting(grid))

main()