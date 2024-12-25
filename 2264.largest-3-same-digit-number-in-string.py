#
# @lc app=leetcode.cn id=2264 lang=python3
# @lcpr version=30204
#
# [2264] 字符串中最大的 3 位相同数字
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        pre = ""
        cnt = 0
        ret = ""
        for i, ch in enumerate(num):
            if pre == ch:
                cnt += 1
            else:
                if cnt > 2:
                    ret = max(ret, num[i - 3 : i])
                pre = ch
                cnt = 1
        if cnt > 2:
            ret = max(ret, num[-3:])
        return ret


# @lc code=end
assert Solution().largestGoodInteger("222") == "222"
assert Solution().largestGoodInteger("6777133339") == "777"


#
# @lcpr case=start
# "6777133339"\n
# @lcpr case=end

# @lcpr case=start
# "2300019"\n
# @lcpr case=end

# @lcpr case=start
# "42352338"\n
# @lcpr case=end

#
