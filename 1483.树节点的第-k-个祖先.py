#
# @lc app=leetcode.cn id=1483 lang=python3
#
# [1483] 树节点的第 K 个祖先
#
from sbw import *
# @lc code=start
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        m=n.bit_length()-1
        pa=[[p]+[-1]*m for p in parent]
        for i in range(1,m+1):
            for x in range(n):
                p=pa[x][i-1]
                if p==-1:
                    continue
                pa[x][i]=pa[p][i-1]
        
        self.pa=pa


    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if (k>>i) &1:
                node=self.pa[node][i]
                if node==-1:
                    break
        return node
        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
# @lc code=end
obj=TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
assert_test(obj,["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"],[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]],eval_list_str('[null,1,0,-1]'))