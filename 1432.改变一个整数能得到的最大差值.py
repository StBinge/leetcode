#
# @lc app=leetcode.cn id=1432 lang=python3
#
# [1432] 改变一个整数能得到的最大差值
#

# @lc code=start
class Solution:
    def maxDiff(self, num: int) -> int:
        digits=str(num)
        
        big_rep='9'
        for d in digits:
            if d=='9':
                continue
            big_rep=d
            break
        small_rep=['',0]
        if digits[0]!='1':
            small_rep=[digits[0],1]
        else:
            for d in digits[1:]:
                if d in '01':
                    continue
                small_rep=[d,0]
                break
        ret=0
        for d in digits:
            big=int(d) if d!=big_rep else 9
            small=int(d) if d!=small_rep[0] else small_rep[1]
            ret=ret*10+big-small
        return ret
# @lc code=end
assert Solution().maxDiff(111)==888
assert Solution().maxDiff(123456)==820000
assert Solution().maxDiff(555)==888
