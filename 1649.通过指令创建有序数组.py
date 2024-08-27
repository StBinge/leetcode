#
# @lc app=leetcode.cn id=1649 lang=python3
#
# [1649] 通过指令创建有序数组
#
from sbw import *
# @lc code=start
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        Max=max(instructions)
        tree=[0]*(Max+1)
        def lowbit(x):
            return x&-x
        def update(x):
            while x<=Max:
                tree[x]+=1
                x+=lowbit(x)
        def query(x):
            ret=0
            while x>0:
                ret+=tree[x]
                x-=lowbit(x)
            return ret
        
        ret=0
        cnt=defaultdict(int)
        for i,x in enumerate(instructions):
            smaller=query(x-1)
            bigger=i-smaller-cnt[x]
            ret+=min(smaller,bigger)
            update(x)
            cnt[x]+=1
            ret%=10**9+7
        return ret

# @lc code=end
assert Solution().createSortedArray([1,3,3,3,2,4,2,1,2])==4
assert Solution().createSortedArray([1,2,3,6,5,4])==3
assert Solution().createSortedArray([1,5,6,2])==1
