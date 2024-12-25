#
# @lc app=leetcode.cn id=面试题 01.06 lang=python3
# @lcpr version=30204
#
# [面试题 01.06] 字符串压缩
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return S
        pre=S[0]
        cnt=1
        ret=[]
        tot=0
        for ch in S[1:]:
            if ch==pre:
                cnt+=1
            else:
                ret.append(pre+str(cnt))
                pre=ch
                cnt=1
                tot+=len(ret[-1])
        ret.append(pre+str(cnt))
        tot+=len(ret[-1])
        return ''.join(ret) if tot<len(S) else S



# @lc code=end



#
# @lcpr case=start
# "aabcccccaaa"\n
# @lcpr case=end

# @lcpr case=start
# "abbccd"\n
# @lcpr case=end

#

