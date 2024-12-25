#
# @lc app=leetcode.cn id=2525 lang=python3
# @lcpr version=30204
#
# [2525] 根据规则将箱子分类
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        is_bulky=(length>=10**4 or width>=10**4 or height>=10**4) or length*width*height>=10**9
        is_heavy=mass>=100
        if is_bulky and is_heavy:
            return 'Both'
        if is_bulky:
            return 'Bulky'
        if is_heavy:
            return 'Heavy'
        return 'Neither'
# @lc code=end



#
# @lcpr case=start
# 1000\n35\n700\n300\n
# @lcpr case=end

# @lcpr case=start
# 200\n50\n800\n50\n
# @lcpr case=end

#

