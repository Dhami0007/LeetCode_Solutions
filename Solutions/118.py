def make_grid(numRows):
    result = [ [1 for _ in range(numRows)] ]
    for i in range(numRows-1):
        a = [1] + [0 for _ in range(numRows-1)]
        result.append(a)
    return result

def generate(numRows):
    grid = make_grid(numRows)
    for i in range(1, numRows):
        for j in range(1, numRows-i):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    
    result = list()
    for i in range(numRows):
        row = list()
        j = 0
        row.append(grid[i][j])
        while i != 0:
            j += 1
            i -= 1
            row.append(grid[i][j])
        result.append(row)
    
    return result

def main():
    numRows = 1
    print(generate(numRows))

main()
