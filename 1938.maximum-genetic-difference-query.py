#
# @lc app=leetcode.cn id=1938 lang=python3
# @lcpr version=30204
#
# [1938] 查询最大基因差
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
MaxBit=19
class BinaryTree:
    def __init__(self) -> None:
        self.zero:BinaryTree=None
        self.one:BinaryTree=None
        self.cnt=0
    
    def insert(self,n:int):
        cur=self
        for i in range(MaxBit-1,-1,-1):
            bit=n>>i & 1
            if bit:
                if not cur.one:
                    cur.one=BinaryTree()
                cur=cur.one
            else:
                if not cur.zero:
                    cur.zero=BinaryTree()
                cur=cur.zero
            cur.cnt+=1
    
    def remove(self,n:int):
        cur=self
        for i in range(MaxBit-1,-1,-1):
            bit=n>>i & 1
            if bit:
                if cur.one.cnt==1:
                    cur.one=None
                    return
                cur=cur.one
            else:
                if cur.zero.cnt==1:
                    cur.zero=None
                    return
                cur=cur.zero
            cur.cnt-=1
    
    def query(self,n:int):
        ret=0
        cur=self
        for i in range(MaxBit-1,-1,-1):
            bit=n>>i & 1
            if bit:
                if cur.zero:
                    ret|=1<<i
                    cur=cur.zero
                else:
                    cur=cur.one
            else:
                if cur.one:
                    ret|=1<<i
                    cur=cur.one
                else:
                    cur=cur.zero
        return ret

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        query_dict=defaultdict(list)
        for i,[node,val] in enumerate(queries):
            query_dict[node].append([i,val])


        par2child=defaultdict(list)
        for i,p in enumerate(parents):
            par2child[p].append(i)
        
        root=parents.index(-1)
        tree=BinaryTree()
        cnt=len(queries)
        ret=[0]*cnt
        def build(root):
            nonlocal cnt
            if cnt==0:
                return
            tree.insert(root)
            if root in query_dict:
                for idx,val in query_dict[root]:
                    ret[idx]=tree.query(val)
                    cnt-=1

            for child in par2child[root]:
                build(child)
            tree.remove(root)

        build(root)
        return ret
# @lc code=end
assert Solution().maxGeneticDifference([-1,0,0,0,3],[[4,6],[0,0],[0,3],[1,8],[4,0]])==[6,0,3,9,4]
assert Solution().maxGeneticDifference(parents = [3,7,-1,2,0,7,0,2], queries = [[4,6],[1,15],[0,5]])==[6,14,7]
assert Solution().maxGeneticDifference(parents = [-1,0,1,1], queries = [[0,2],[3,2],[2,5]])==[2,3,7]


#
# @lcpr case=start
# [-1,0,1,1]\n[[0,2],[3,2],[2,5]]\n
# @lcpr case=end

# @lcpr case=start
# [3,7,-1,2,0,7,0,2]\n[[4,6],[1,15],[0,5]]\n
# @lcpr case=end

#

