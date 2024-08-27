#
# @lc app=leetcode.cn id=1694 lang=python3
#
# [1694] 重新格式化电话号码
#


# @lc code=start
class Solution:
    def reformatNumber(self, number: str) -> str:
        ret = []
        for ch in number:
            if ch.isnumeric():
                ret.append(ch)

        N=len(ret)
        ans=[]
        idx=0
        while N>0:
            if N>4:
                ans.extend(ret[idx:idx+3])
                ans.append('-')
                idx+=3
                N-=3
            elif N==4:
                ans.extend(ret[idx:idx+2])
                ans.append('-')
                idx+=2
                ans.extend(ret[idx:idx+2])
                idx+=2
                N-=4
            else:
                ans.extend(ret[idx:])
                idx+=N
                N-=N
        return ''.join(ans)

# @lc code=end
assert Solution().reformatNumber("9964-") == "99-64"
assert Solution().reformatNumber("12") == "12"
assert Solution().reformatNumber("123 4-567") == "123-45-67"
assert Solution().reformatNumber("1-23-45 6") == "123-456"
