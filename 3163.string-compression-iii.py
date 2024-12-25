#
# @lc app=leetcode.cn id=3163 lang=python3
# @lcpr version=30204
#
# [3163] 压缩字符串 III
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def compressedString(self, word: str) -> str:
        ret=''
        pre=word[0]
        cnt=1
        for ch in word[1:]:
            if ch==pre:
                cnt+=1
                if cnt==10:
                    ret+=str(9)+pre
                    cnt=1
            else:
                ret+=str(cnt)+pre
                pre=ch
                cnt=1
        ret+=str(cnt)+pre
        return ret
# @lc code=end



#
# @lcpr case=start
# "abcde"\n
# @lcpr case=end

# @lcpr case=start
# "aaaaaaaaaaaaaabb"\n
# @lcpr case=end

#

