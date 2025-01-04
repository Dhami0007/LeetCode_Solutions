def uniquePathsIII(grid):
    def dfs(node, visited, count, limit):
        
        if grid[node[0]][node[1]] == 2:
            if len(visited) == limit-1:
                count[0] += 1
            return
        visited.add(node)
        for move in moves:
            i, j = node[0] + move[0], node[1] + move[1]
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != -1 and (i, j) not in visited:
                dfs((i, j), visited, count, limit)
        visited.remove(node)

    count = [0]
    limit = 0
    start = (0, 0)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                start = (i, j)
            if grid[i][j] != -1:
                limit += 1
    
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    trail = set()

    dfs(start, trail, count, limit)

    return count[0]



def main():
    grid = [[0,1],[2,0]]
    print(uniquePathsIII(grid))

main()