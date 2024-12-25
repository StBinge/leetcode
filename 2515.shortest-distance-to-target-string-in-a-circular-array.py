#
# @lc app=leetcode.cn id=2515 lang=python3
# @lcpr version=30204
#
# [2515] 到目标字符串的最短距离
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        N=len(words)
        for i in range(len(words)):
            left=(startIndex-i)%N
            if words[left]==target:
                return i
            right=(startIndex+i)%N
            if words[right]==target:
                return i
        else:
            return -1
# @lc code=end
assert Solution().closetTarget(["hsdqinnoha","mqhskgeqzr","zemkwvqrww","zemkwvqrww","daljcrktje","fghofclnwp","djwdworyka","cxfpybanhd","fghofclnwp","fghofclnwp"],"zemkwvqrww",8)==4


#
# @lcpr case=start
# ["hello","i","am","leetcode","hello"]\n"hello"\n1\n
# @lcpr case=end

# @lcpr case=start
# ["a","b","leetcode"]\n"leetcode"\n0\n
# @lcpr case=end

# @lcpr case=start
# ["i","eat","leetcode"]\n"ate"\n0\n
# @lcpr case=end

#

