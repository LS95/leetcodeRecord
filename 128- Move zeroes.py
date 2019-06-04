#coding=utf-8

class Solutin():
    def moveZeroes(self, nums):
        n = nums.count(0)
        l = len(nums)
        i = 0
        while 0 in nums:
            if (nums[i] == 0):
                nums.remove(nums[i])
                l = l - 1
            else:
                i = i + 1
        for j in range(n):
            nums.append(0)
        return nums



if __name__ == '__main__':
    s = Solutin()
    nums = [1,3,0,12,0,6]
    print(nums)
    s.moveZeroes(nums)
    print(nums)


