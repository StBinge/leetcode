#
# @lc app=leetcode.cn id=470 lang=python3
#
# [470] 用 Rand7() 实现 Rand10()
#

def rand7():
    pass
# @lc code=start
# The rand7() API is already defined for you.

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        if self.rand6()<4:
            return self.rand5()
        else:
            return self.rand5()+5

    
    def rand5(self):
        while True:
            r=rand7()
            if r<6:
                return r
    
    def rand6(self):
        while True:
            r=rand7()
            if r<7:
                return r
# @lc code=end

