#
# @lc app=leetcode.cn id=3258 lang=python3
# @lcpr version=30204
#
# [3258] 统计满足 K 约束的子字符串数量 I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        left=one=zero=0
        ret=0
        for i,ch in enumerate(s):
            if ch=='1':
                one+=1
            else:
                zero+=1
            while one>k and zero>k:
                pre=s[left]
                if pre=='1':
                    one-=1
                else:
                    zero-=1
                left+=1
            ret+=i-left+1
        return ret
# @lc code=end
assert Solution().countKConstraintSubstrings('10101',1)==12


#
# @lcpr case=start
# "10101"\n1\n
# @lcpr case=end

# @lcpr case=start
# "1010101"\n2\n
# @lcpr case=end

# @lcpr case=start
# "11111"\n1\n
# @lcpr case=end

#

