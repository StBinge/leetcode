#
# @lc app=leetcode.cn id=1507 lang=python3
#
# [1507] 转变日期格式
#

# @lc code=start
class Solution:
    def reformatDate(self, date: str) -> str:
        date=date.split()
        date[0]=date[0][:-2].zfill(2)
        M=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date[1]=f'{(M.index(date[1])+1):0>2}'
        return '-'.join(reversed(date))
# @lc code=end
assert Solution().reformatDate("6th Jun 1933")=="1933-06-06"
