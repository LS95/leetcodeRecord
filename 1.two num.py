#coding=utf-8

class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        nums_min = {target - n: i for i,n in enumerate(nums)}
        for i in range(len(nums)):
            if nums_min.get(nums[i]) and nums_min.get(nums[i]) != i:
                return [i, nums_min.get(nums[i])]


                
# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j] == target:
#                     return [i,j]
#         return None

# if __name__ == '__main__':
#     nums = [2,7,11,15]
#     tar = 9
#     a =Solution()
#     res = a.twoSum(nums,tar)
#     print(res)


