#
# @lc app=leetcode.cn id=1209 lang=python3
#
# [1209] 删除字符串中的所有相邻重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count=[-1]
        ret=['']*(len(s)+1)
        idx=1
        for c in s:
            ret[idx]=c
            idx+=1
            if c==ret[idx-2]:
                count[-1]+=1
            else:
                count.append(1)
            if count[-1]==k:
                count.pop()
                idx-=k

        return ''.join(ret[:idx])
# @lc code=end
assert Solution().removeDuplicates(s = "pbbcggttciiippooaais", k = 2)=='ps'
assert Solution().removeDuplicates(s = "deeedbbcccbdaa", k = 3)=='aa'
assert Solution().removeDuplicates(s = "abcd", k = 2)=='abcd'
