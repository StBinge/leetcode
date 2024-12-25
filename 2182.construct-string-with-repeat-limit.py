#
# @lc app=leetcode.cn id=2182 lang=python3
# @lcpr version=30204
#
# [2182] 构造限制重复的字符串
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ret=''
        counter=Counter(s)
        sorted_chars=sorted([[k,counter[k]] for k in counter])
        while sorted_chars:
            ch,v=sorted_chars.pop()
            if v<=repeatLimit:
                ret+=ch*v
                continue
            gap=(v-1)//repeatLimit
            for _ in range(gap):
                ret+=ch*repeatLimit
                if not sorted_chars:
                    return ret
                ret+=sorted_chars[-1][0]
                sorted_chars[-1][1]-=1
                if sorted_chars[-1][1]==0:
                    sorted_chars.pop()
            ret+=ch*(v-gap*repeatLimit)
        return ret
# @lc code=end
assert Solution().repeatLimitedString(s = "aababab", repeatLimit = 2)=='bbabaa'
assert Solution().repeatLimitedString("cczazcc",3)=='zzcccac'


#
# @lcpr case=start
# "cczazcc"\n3\n
# @lcpr case=end

# @lcpr case=start
# "aababab"\n2\n
# @lcpr case=end

#

