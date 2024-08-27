#
# @lc app=leetcode.cn id=1616 lang=python3
#
# [1616] 分割两个字符串得到回文串
#


# @lc code=start
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:

        def check_self_palindrome(s: str,left,right) -> bool:
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        def check(s1: str, s2: str) -> bool:
            left, right = 0, len(s1) - 1
            while left < right:
                if s1[left] != s2[right]:
                    break 
                left += 1
                right -= 1
            if left>=right:
                return True
            return check_self_palindrome(s1,left,right) or check_self_palindrome(s2,left,right)

        return check(a,b) or check(b,a)

# @lc code=end
assert Solution().checkPalindromeFormation("xbdef", "xecab") == False
assert Solution().checkPalindromeFormation(a="ulacfd", b="jizalu")

assert Solution().checkPalindromeFormation("x", "y")


assert Solution().checkPalindromeFormation(
    "aejbaalflrmkswrydwdkdwdyrwskmrlfqizjezd", 
    "uvebspqckawkhbrtlqwblfwzfptanhiglaabjea"
)
assert Solution().checkPalindromeFormation(
    "pvhmupgqeltozftlmfjjde", "yjgpzbezspnnpszebzmhvp"
)
assert Solution().checkPalindromeFormation(a="ulacfd", b="jizalu")
assert Solution().checkPalindromeFormation(a="abdef", b="fecab")
