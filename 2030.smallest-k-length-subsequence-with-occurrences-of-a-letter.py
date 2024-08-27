#
# @lc app=leetcode.cn id=2030 lang=python3
# @lcpr version=30204
#
# [2030] 含特定字母的最小子序列
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        N=len(s)
        remain=s.count(letter)
        include=0
        ret=['']*N
        insert_start=0
        length=0
        idx=0
        for i,ch in enumerate(s):
            if length+N-i==k:
                return ''.join(ret[:length])+s[i:]       
            
            if ch==letter:
                if remain+include==repetition and length+remain>=k:
                    for i in range(k-1,-1,-1):
                        if ret[i]!=letter:
                            ret[i]=letter
                            remain-=1
                            if remain==0:
                                return ''.join(ret)
                remain-=1

            insert=bisect_right(ret,ch,hi=length)
            if insert==k:
                continue
            if insert<k-N+i:
                if ch>letter:
                    return 

            if ch>=letter:
                ret[insert]=ch
                include+=ch==letter
                length=insert+1
                continue
            if remain>=repetition:
                ret[insert]=ch
                length=insert+1
                include=0
            else:
                letter_start_pos=bisect_left(ret,letter,hi=length)
                insert=letter_start_pos+(repetition-remain)

                ret[insert]=ch
                length=insert+1
                idx=i+1
                insert_start=length
                break
        
        last_pos=-1
        for i in range(idx,N):
            if length+N-i==k:
                return ''.join(ret[:length])+s[i:]
            ch=s[i]
            insert=bisect_right(ret,ch,insert_start,length)
            if insert==k:
                continue
            if ch>=letter:
                ret[insert]=ch
                length=insert+1
                if ch==letter:
                    last_pos=insert
                    if last_pos==k-1:
                        return ''.join(ret)
                continue
            if last_pos==-1:
                ret[insert]=ch
                length=insert+1
            else:
                insert=last_pos+1
                ret[insert]=ch
                length+=1
                insert_start=insert

        return ''.join(ret)            
        

# @lc code=end
assert_answer('mmmmxmmm',Solution().smallestSubsequence("mmmxmxymmm",8,"m",4))
assert_answer('afffff',Solution().smallestSubsequence("adffhjfmmmmorsfff",6,"f",5))
assert_answer('abb',Solution().smallestSubsequence("aaabbbcccddd",3,"b",2))
assert Solution().smallestSubsequence(s = "bb", k = 2, letter = "b", repetition = 2)=='bb'

ret= Solution().smallestSubsequence(s = "leetcode", k = 4, letter = "e", repetition = 2)
assert_answer('ecde',ret)
assert Solution().smallestSubsequence(s = "leet", k = 3, letter = "e", repetition = 1)=='eet'


#
# @lcpr case=start
# "leet"\n3\n"e"\n1\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n4\n"e"\n2\n
# @lcpr case=end

# @lcpr case=start
# "bb"\n2\n"b"\n2\n
# @lcpr case=end

#

