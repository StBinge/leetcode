#
# @lc app=leetcode.cn id=2780 lang=python3
# @lcpr version=30204
#
# [2780] 合法分割的最小下标
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        N=len(nums)
        n=m=0
        for k,v in cnt.items():
            if v*2>N:
                n=k
                m=v
                break
        if N&1==1 and N//2+1==m:
            return -1
        
        pre=0
        for i in range(N):
            if nums[i]==n:
                pre+=1
            if pre*2 > i+1 and (m-pre)*2>N-i-1:
                return i
        return -1


# @lc code=end
assert Solution().minimumIndex([3,3,3,3,7,2,2])==-1
assert Solution().minimumIndex( [2,1,3,1,1,1,7,1,2,1])==4
assert Solution().minimumIndex([1,2,2,2])==2


#
# @lcpr case=start
# [1,2,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3,1,1,1,7,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3,7,2,2]\n
# @lcpr case=end

#

