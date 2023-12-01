#
# @lc app=leetcode.cn id=873 lang=python3
#
# [873] 最长的斐波那契子序列的长度
#
from typing import List
# @lc code=start
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:

        ret=0
        num_pos={n:i for i,n in enumerate(arr)}
        n=len(arr)
        f=[[0]*n for _ in range(n)]
        # p1+p2=p3
        for p3 in range(2,n):
            n3=arr[p3]
            for p2 in range(p3-1,-1,-1):
                n2=arr[p2]
                n1=n3-n2
                if n1>=n2:
                    break
                if n1 in num_pos:
                    f[p3][p2]=max(f[p2][num_pos[n1]]+1,3)
                    ret=max(ret,f[p3][p2])
        return ret              



# @lc code=end
assert Solution().lenLongestFibSubseq([2392,2545,2666,5043,5090,5869,6978,7293,7795])==0
arr = [1,3,7,11,12,14,18]
assert Solution().lenLongestFibSubseq(arr)==3

arr = [1,2,3,4,5,6,7,8]
assert Solution().lenLongestFibSubseq(arr)==5
