def makeGraph(conns):
    result = dict()
    for curr,next in conns:
        if curr not in result:
            result[curr] = []
        if next not in result:
            result[next] = []
        result[curr].append(next)
        result[next].append(curr)
    return result

def dfs(graph, memory, node, revs, conns):
    memory.add(node)
    for next in graph[node]:
        if next not in memory:
            if (node,next) in conns:
            # this is the forward connection
                revs[0] += 1
            dfs(graph, memory, next, revs, conns)


def minReorder(n, connections):
    graph = makeGraph(connections)
    # O(1) lookup in sets
    connections = set((u,v) for u,v in connections)
    print(graph)
    memory = set()
    revs = [0]
    dfs(graph, memory, 0, revs, connections)
    return revs[0]


def main():
    n = 6
    connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

    print(minReorder(n, connections))

main()