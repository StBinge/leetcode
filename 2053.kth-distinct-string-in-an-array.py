#
# @lc app=leetcode.cn id=2053 lang=python3
# @lcpr version=30204
#
# [2053] 数组中第 K 个独一无二的字符串
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        s=Counter(arr)
        for letters in arr:
            if s[letters]==1:
                k-=1
                if k==0:
                    return letters
        return ''
# @lc code=end



#
# @lcpr case=start
# ["d","b","c","b","c","a"]\n2\n
# @lcpr case=end

# @lcpr case=start
# ["aaa","aa","a"]\n1\n
# @lcpr case=end

# @lcpr case=start
# ["a","b","a"]\n3\n
# @lcpr case=end

#

