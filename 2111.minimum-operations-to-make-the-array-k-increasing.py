#
# @lc app=leetcode.cn id=2111 lang=python3
# @lcpr version=30204
#
# [2111] 使数组 K 递增的最少操作次数
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        def count(idx:int):
            f=[]
            for n in arr[idx::k]:
                idx=bisect_right(f,n)
                if idx==len(f):
                    f.append(n)
                else:
                    f[idx]=n
            return len(f)

        ret=len(arr)
        for i in range(k):
            ret-=count(i)
        return ret

# @lc code=end



#
# @lcpr case=start
# [5,4,3,2,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [4,1,5,2,6,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [4,1,5,2,6,2]\n3\n
# @lcpr case=end

#

