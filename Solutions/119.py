def make_grid(numRows):
    result = [ [1 for _ in range(numRows)] ]
    for i in range(numRows-1):
        a = [1] + [0 for _ in range(numRows-1)]
        result.append(a)
    return result

def getRow(rowIndex):
    numRows = rowIndex + 1
    grid = make_grid(numRows)
    for i in range(1, numRows):
        for j in range(1, numRows-i):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    
    result = list()
    j = 0
    result.append(grid[rowIndex][j])
    while rowIndex != 0:
        rowIndex -= 1
        j += 1
        result.append(grid[rowIndex][j])
    return result

def main():
    rowIndex = 3
    print(getRow(rowIndex))

main()