#
# @lc app=leetcode.cn id=1643 lang=python3
#
# [1643] 第 K 条最小指令
#
from sbw import *
# @lc code=start
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        V,H=destination
        ret=[]
        for _ in range(H+V):
            cnt=math.comb(H+V-1,V)
            if cnt>=k:
                ret.append('H')
                H-=1
            else:
                k-=cnt
                ret.append('V')
                V-=1
        return ''.join(ret)
# @lc code=end
assert Solution().kthSmallestPath([2,3], 3)=='HHVVH'
assert Solution().kthSmallestPath([2,3], 2)=='HHVHV'
assert Solution().kthSmallestPath([2,3], 1)=='HHHVV'
