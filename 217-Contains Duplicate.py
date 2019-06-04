#coding=utf-8#coding=utf-8

class Solution:
    def containsDuplicate(self, nums):
        if len(set(nums)) < len(nums):
            return True
        return False

if __name__ == '__main__':
    # main()
    a = Solution()
    res = a.containsDuplicate([9,9,9])
    print(res)