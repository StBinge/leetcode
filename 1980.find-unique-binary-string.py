#
# @lc app=leetcode.cn id=1980 lang=python3
# @lcpr version=30204
#
# [1980] 找出不同的二进制字符串
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ret=[]
        for i,n in enumerate(nums):
            ret.append('0' if n[i]=='1' else '1')
        return ''.join(ret)
# @lc code=end
assert Solution().findDifferentBinaryString(["00","10"])=='01'
assert Solution().findDifferentBinaryString(["00","01"])=='10'
assert Solution().findDifferentBinaryString(["01","10"])=='00'


#
# @lcpr case=start
# ["01","10"]\n
# @lcpr case=end

# @lcpr case=start
# ["00","01"]\n
# @lcpr case=end

# @lcpr case=start
# ["111","011","001"]\n
# @lcpr case=end

#

