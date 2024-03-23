#
# @lc app=leetcode.cn id=1340 lang=python3
#
# [1340] 跳跃游戏 V
#
from sbw import *
# @lc code=start

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        L=len(arr)
        sorted_heights=sorted(range(L),key=arr.__getitem__)

        
        f=[1]*L
        
        for i in range(1,L):
            cur=sorted_heights[i]
            h=arr[cur]
            for j in range(cur-1,max(0,cur-d)-1,-1):
                if arr[j]>=h:
                    break
                f[cur]=max(f[j]+1,f[cur])
            for j in range(cur+1,min(cur+d+1,L)):
                if arr[j]>=h:
                    break
                f[cur]=max(f[cur],f[j]+1)
            
        return max(f)
# @lc code=end
assert Solution().maxJumps([7,6,5,4,3,2,1],1)==7
assert Solution().maxJumps([22,29,52,97,29,75,78,2,92,70,90,12,43,17,97,18,58,100,41,32],17)==6
assert Solution().maxJumps(arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2)==4
