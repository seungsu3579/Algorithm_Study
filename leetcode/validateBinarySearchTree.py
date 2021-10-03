# https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.v = (-1) * pow(2, 31) - 1

        return self.inorder(root)

    # 중위 순회 - 카카오 블라인드 2차 CS테스트 문제 중 일부.
    def inorder(self, node):

        if node != None:
            a = True
            b = True

            if node.left:
                a = self.inorder(node.left)

            if node.val > self.v:
                self.v = node.val
                print(node.val)
            else:
                return False

            if node.right:
                b = self.inorder(node.right)

            return a and b

        else:
            return True

