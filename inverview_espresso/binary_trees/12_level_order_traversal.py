class TreeNone:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# TIME: O(n)
# SPACE: O(n)
class Solution:
    def levelOrder(self, root):
        '''
        BFS
        '''
        levels = []
        queue = [root]
        while queue:
            size = len(queue)
            level = []
            while size != 0:
                item = queue.pop(0)
                level.append(item.val)
                if item.left: queue.append(item.left)
                if item.right: queue.append(item.right)
                size -= 1
            levels.append(level)

        return levels