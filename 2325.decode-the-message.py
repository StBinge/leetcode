#
# @lc app=leetcode.cn id=2325 lang=python3
# @lcpr version=30204
#
# [2325] 解密消息
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        maps={}
        cur=ord('a')
        seen=set()
        for ch in key:
            if ch==' ' or ch in seen:
                continue
            maps[ch]=chr(cur)
            cur+=1
            seen.add(ch)
        maps[' ']=' '
        return ''.join(map(lambda x:maps[x],message))
        
# @lc code=end
assert Solution().decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv")=="this is a secret"


#
# @lcpr case=start
# "the quick brown fox jumps over the lazy dog"\n"vkbs bs t suepuv"\n
# @lcpr case=end

# @lcpr case=start
# "eljuxhpwnyrdgtqkviszcfmabo"\n"zwx hnfx lqantp mnoeius ycgk vcnjrdb"\n
# @lcpr case=end

#

