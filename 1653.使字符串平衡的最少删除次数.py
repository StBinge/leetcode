#
# @lc app=leetcode.cn id=1653 lang=python3
#
# [1653] 使字符串平衡的最少删除次数
#


# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        pre_b_cnt=0
        ret=0
        for c in s:
            if c=='a':
                if pre_b_cnt:
                    pre_b_cnt-=1
                    ret+=1
            else:
                pre_b_cnt+=1
        return ret


# @lc code=end
assert Solution().minimumDeletions("bbaaaaabb") == 2
assert Solution().minimumDeletions("aababbab") == 2
