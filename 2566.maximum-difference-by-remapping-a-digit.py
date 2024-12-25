#
# @lc app=leetcode.cn id=2566 lang=python3
# @lcpr version=30204
#
# [2566] 替换一个数字后的最大差值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minMaxDifference(self, num: int) -> int:
        s=str(num)
        mx=num
        for ch in s:
            if ch=='9':
                continue
            mx=int(s.replace(ch,'9'))
            break
        mi=int(s.replace(s[0],'0'))
        return mx-mi
# @lc code=end
assert Solution().minMaxDifference(90)==99


#
# @lcpr case=start
# 11891\n
# @lcpr case=end

# @lcpr case=start
# 90\n
# @lcpr case=end

#

