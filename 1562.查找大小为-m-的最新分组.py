#
# @lc app=leetcode.cn id=1562 lang=python3
#
# [1562] 查找大小为 M 的最新分组
#
from sbw import *


# @lc code=start



class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m==n:
            return n
        endpoints=[(-1,-1) for _ in range(n)]
        ret=-1
        cnt=0
        for i,p in enumerate(arr):
            p-=1
            left=right=p
            if p>0 and endpoints[p-1][1]!=-1:
                left=endpoints[p-1][0]
                left_len=endpoints[p-1][1]-endpoints[p-1][0]+1
                if left_len==m:
                    cnt-=1
            if p+1<n and endpoints[p+1][0]!=-1:
                right=endpoints[p+1][1]
                right_len=endpoints[p+1][1]-endpoints[p+1][0]+1
                if right_len==m:
                    cnt-=1
            l=right-left+1
            if l==m:
                cnt+=1
            if cnt>0:
                ret=i+1
            endpoints[left]=endpoints[right]=(left,right)
        return ret


# @lc code=end
assert Solution().findLatestStep(arr=[3, 5, 1, 2, 4], m=1) == 4
assert Solution().findLatestStep(arr = [2,1], m = 2) == 2
assert Solution().findLatestStep(arr=[1], m=1) == 1
assert Solution().findLatestStep(arr=[3, 1, 5, 4, 2], m=2) == -1
