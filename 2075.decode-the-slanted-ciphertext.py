#
# @lc app=leetcode.cn id=2075 lang=python3
# @lcpr version=30204
#
# [2075] 解码斜向换位密码
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText:
            return ''
        N=len(encodedText)
        C=N//rows
        # matrix=[encodedText for r in range(rows)]
        ret=[]
        for c in range(C):
            for r in range(rows):
                idx=r*C+c
                if idx>=N:
                    break
                ret.append(encodedText[idx])
                c+=1
        for i in range(len(ret)-1,-1,-1):
            if ret[i]!=' ':
                return ''.join(ret[:i+1])
        
# @lc code=end

assert Solution().decodeCiphertext(encodedText = "ch   ie   pr", rows = 3)=='cipher'

#
# @lcpr case=start
# "ch   ie   pr"\n3\n
# @lcpr case=end

# @lcpr case=start
# "iveo    eed   l te   olc"\n4\n
# @lcpr case=end

# @lcpr case=start
# "coding"\n1\n
# @lcpr case=end

# @lcpr case=start
# " b  ac"\n2\n
# @lcpr case=end

#

