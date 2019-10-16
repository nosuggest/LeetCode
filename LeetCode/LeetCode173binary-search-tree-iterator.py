# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    def __init__(self, root):
        """
        :type root: TreeNode
        """

        def search(root):
            if not root:
                return
            for i in search(root.left):
                yield i

            yield root.val

            for i in search(root.right):
                yield i

        self.s = search(root)
        self.ans = []

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.hasNext():
            return self.ans.pop()

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.ans:
            return True
        try:
            v = next(self.s)
            self.ans.append(v)
            return True
        except:
            return False



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()