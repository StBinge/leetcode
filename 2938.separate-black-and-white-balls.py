#
# @lc app=leetcode.cn id=2938 lang=python3
# @lcpr version=30204
#
# [2938] 区分黑球与白球
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumSteps(self, s: str) -> int:
        ret=0
        one_cnt=0
        for bit in s:
            if bit=='0':
                ret+=one_cnt
            else:
                one_cnt+=1
        return ret


# @lc code=end
assert Solution().minimumSteps('0111')==0
assert Solution().minimumSteps('100')==2
assert Solution().minimumSteps('101')==1


#
# @lcpr case=start
# "101"\n
# @lcpr case=end

# @lcpr case=start
# "100"\n
# @lcpr case=end

# @lcpr case=start
# "0111"\n
# @lcpr case=end

#

