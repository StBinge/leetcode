#
# @lc app=leetcode.cn id=2190 lang=python3
# @lcpr version=30204
#
# [2190] 数组中紧跟 key 之后出现最频繁的数字
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        cnt=defaultdict(int)
        ret=-1
        mx=0
        for i in range(len(nums)-1):
            if nums[i]==key:
                cnt[nums[i+1]]+=1
                if cnt[nums[i+1]]>mx:
                    mx=cnt[nums[i+1]]
                    ret=nums[i+1]

        return ret
# @lc code=end
assert Solution().mostFrequent([2,2,2,2,3],2)==2


#
# @lcpr case=start
# [1,100,200,1,100]\n1\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,3]\n2\n
# @lcpr case=end

#

