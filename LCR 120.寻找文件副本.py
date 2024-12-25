#
# @lc app=leetcode.cn id=LCR 120 lang=python3
# @lcpr version=30204
#
# [LCR 120] 寻找文件副本
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        for i,n in enumerate(documents):
            while i!=n:
                if documents[n]==n:
                    return n
                documents[i],documents[n]=documents[n],documents[i]
                n=documents[i]

# @lc code=end
assert Solution().findRepeatDocument([2, 5, 3, 0, 5, 0]) in [0,5]


#
# @lcpr case=start
# [2, 5, 3, 0, 5, 0]\n
# @lcpr case=end

#

