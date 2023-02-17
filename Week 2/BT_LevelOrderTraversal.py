#Pattern: Breadth First Search

def levelOrder (self, root: Optional[TreeNode]) -> List[List[int]]:
    
    #Check's to see if the BT has nodes
    if not root:
        return None 
    queue = [root]
    res = []


    while queue:
        level = []
        l = len(queue)
        for i in range(l):
            currNode = queue.pop(0)
            level.append(currNode.val)
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

        res.append(level)
    return res


#Time Complexity is O(n) Space Complexity is O(n)