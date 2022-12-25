class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        li = []
        now = [root]
        while now:
            li.append([data.val for data in now])
            nex = []
            for data in now:
                if data.left:
                    nex.append(data.left)
                if data.right:
                    nex.append(data.right)
            now = nex
        return li