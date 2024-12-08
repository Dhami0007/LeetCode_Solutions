def pathSum(root, targetSum):
    def findNodes(node, nodeSet):
        if node.left is not None:
            nodeSet.add(node.left)
            findNodes(node.left, nodeSet)
        if node.right is not None:
            nodeSet.add(node.right)
            findNodes(node.right, nodeSet)

    def traverse(node, targetSum, sum, targetHit):
        sum += node.val
        if sum == targetSum:
            targetHit[0] += 1
        if node.left is not None:
            traverse(node.left, targetSum, sum, targetHit)
        if node.right is not None:
            traverse(node.right, targetSum, sum, targetHit)
        sum -= node.val

    if root is None:
        return 0
    
    sum = 0
    targetHit = [0]
    nodeSet = {root}
    findNodes(root, nodeSet)
    for node in nodeSet:
        traverse(node, targetSum, sum, targetHit)
    
    return targetHit[0]
    