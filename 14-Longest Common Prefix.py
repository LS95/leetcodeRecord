#coding=utf-8



class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        strs.sort(key=lambda i: len(i))
        # print(strs)
        for i in range(len(strs[0])):
            tmp = res +  strs[0][i]
            # print("tmp=",tmp)
            for each in strs:
                if each.startswith(tmp) == False:
                    return res
            res = tmp
        return res





if __name__ == '__main__':
    s = Solution()
    res = s.longestCommonPrefix( ["flower","flow","flight"])
    print(res)
    res = s.longestCommonPrefix( ["dog","racecar","car"])
    print(res)
