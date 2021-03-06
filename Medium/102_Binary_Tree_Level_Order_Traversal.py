'''


102. Binary Tree Level Order Traversal


Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level = 0
        result = []
        bfs = [(level, root)]

        curr = []
        
        while len(bfs):
            l, node = bfs.pop(0)
            
            if level != l:
                result.append(curr)
                curr = []
                level = l
            
            if node:
                bfs.append((l + 1, node.left))
                bfs.append((l + 1, node.right))
                curr.append(node.val)

        return result
