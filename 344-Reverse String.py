#coding=utf-8#coding=utf-8
class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s) - 1
        for i in range(n // 2 + 1):
            s[i] ,s[n-i] = s[n-i] , s[i]
        return s
if __name__ == '__main__':
    # main()
    a = Solution()
    res = a.reverseString( ["H","a","n","n","a","h"])
    print(res)