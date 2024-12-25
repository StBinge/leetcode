#
# @lc app=leetcode.cn id=2380 lang=python3
# @lcpr version=30204
#
# [2380] 二进制字符串重新安排顺序需要的时间
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        f=0
        zeros=0
        for ch in s:
            if ch=='0':
                zeros+=1
            elif zeros:
                f=max(f+1,zeros)
        return f
# @lc code=end
assert Solution().secondsToRemoveOccurrences('11100')==0
assert Solution().secondsToRemoveOccurrences('0110101')==4


#
# @lcpr case=start
# "0110101"\n
# @lcpr case=end

# @lcpr case=start
# "11100"\n
# @lcpr case=end

#

