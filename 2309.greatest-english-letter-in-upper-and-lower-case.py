#
# @lc app=leetcode.cn id=2309 lang=python3
# @lcpr version=30204
#
# [2309] 兼具大小写的最好英文字母
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def greatestLetter(self, s: str) -> str:
        ss=set()
        ret=''
        for ch in s:
            if ch.islower() and ch.upper() in ss and ch.upper()>ret:
                ret=ch.upper()
            elif ch.isupper() and ch.lower() in ss and ch>ret:
                ret=ch
            ss.add(ch)
        return ret

# @lc code=end
assert Solution().greatestLetter("AbCdEfGhIjK")==''
assert Solution().greatestLetter("arRAzFif")=='R'
assert Solution().greatestLetter("lEeTcOdE")=='E'


#
# @lcpr case=start
# "lEeTcOdE"\n
# @lcpr case=end

# @lcpr case=start
# "arRAzFif"\n
# @lcpr case=end

# @lcpr case=start
# "AbCdEfGhIjK"\n
# @lcpr case=end

#

