#
# @lc app=leetcode.cn id=2808 lang=python3
# @lcpr version=30204
#
# [2808] 使循环数组所有元素相等的最少秒数
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        N=len(nums)
        pos_map=defaultdict(list)
        for i,n in enumerate(nums):
            pos_map[n].append(i)
        
        ret=N
        for ar in pos_map.values():
            ar.append(N+ar[0])
            mx=max(y-x-1 for x,y in pairwise(ar))
            ret=min(ret,(mx+1)//2)
        return ret
                

        
        

# @lc code=end
assert Solution().minimumSeconds([5,5,5,5])==0
assert Solution().minimumSeconds([2,1,3,3,2])==2
assert Solution().minimumSeconds([1,2,1,2])==1


#
# @lcpr case=start
# [1,2,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [5,5,5,5]\n
# @lcpr case=end

#

