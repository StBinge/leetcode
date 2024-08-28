#
# @lc app=leetcode.cn id=2062 lang=python3
# @lcpr version=30204
#
# [2062] 统计字符串中的元音子字符串
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vows=set('aeiou')
        N=len(word)
        ret=0
        for i in range(N):
            s=set()
            for j in range(i,N):
                if word[j] not in vows:
                    break
                s.add(word[j])
                if s==vows:
                    ret+=1
        return ret


# @lc code=end
assert Solution().countVowelSubstrings(word="cuaieuouac") == 7
assert Solution().countVowelSubstrings(word="unicornarihan") == 0
assert Solution().countVowelSubstrings(word="aeiouu") == 2


#
# @lcpr case=start
# "aeiouu"\n
# @lcpr case=end

# @lcpr case=start
# "unicornarihan"\n
# @lcpr case=end

# @lcpr case=start
# "cuaieuouac"\n
# @lcpr case=end

# @lcpr case=start
# "bbaeixoubb"\n
# @lcpr case=end

#
