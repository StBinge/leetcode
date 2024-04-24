#
# @lc app=leetcode.cn id=1542 lang=python3
#
# [1542] 找出最长的超赞子字符串
#


# @lc code=start
class Solution:
    def longestAwesome(self, s: str) -> int:
        masks = {0: -1}
        mask = 0
        ret = 1
        for i, ch in enumerate(s):
            mask ^= 1 << int(ch)
            for j in range(10):
                _mask = mask ^ (1 << j)
                if _mask in masks:
                    ret = max(ret, i - masks[_mask])
            if mask in masks:
                ret = max(ret, i - masks[mask])
            else:
                masks[mask] = i
        return ret


# @lc code=end
assert Solution().longestAwesome("00") == 2
assert Solution().longestAwesome("76263") == 3
assert Solution().longestAwesome("213123") == 6
assert Solution().longestAwesome("12345678") == 1
assert Solution().longestAwesome("3242415") == 5
