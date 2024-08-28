#
# @lc app=leetcode.cn id=1803 lang=python3
#
# [1803] 统计异或值在范围内的数对有多少
#
from sbw import *
# @lc code=start
class Trie:
    def __init__(self) -> None:
        self.children=[None,None]
        self.cnt=0
    
    def insert(self,x):
        cur=self
        for i in range(15,-1,-1):
            v=x>>i & 1
            if not cur.children[v]:
                cur.children[v]=Trie()
            cur=cur.children[v]
            cur.cnt+=1
    
    def search(self,x,limit):
        cur=self
        ret=0
        for i in range(15,-1,-1):
            if not cur:
                return ret
            v=x>>i&1
            if limit>>i & 1:
                if cur.children[v]:
                    ret+=cur.children[v].cnt
                cur=cur.children[v^1]
            else:
                cur=cur.children[v]
        return ret
                
class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        ret=0
        root=Trie()
        for n in nums:
            # ret+=root.search(n,high+1)-root.search(n,low)
            ret+=root.search(n,high+1)-root.search(n,low)
            root.insert(n)
        return ret

# @lc code=end
assert Solution().countPairs(nums = [9,8,4,2,1], low = 5, high = 14)==8
assert Solution().countPairs(nums = [1,4,2,7], low = 2, high = 6)==6
