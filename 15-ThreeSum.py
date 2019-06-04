#coding=utf-8
# py3
class Solution:
    def threeSum(self, nums):
        nums.sort()
        first=[]
        i=0
        while(i<len(nums)-2):
            if(nums[i]!=nums[i-1] or i==0):
                target=0-nums[i]
                left=i+1
                right=len(nums)-1
                while(left!=right):
                    if(nums[left]+nums[right]==target):
                        first.append([nums[i],nums[left],nums[right]])
                        while(left<right):
                            left+=1
                            if(nums[left]!=nums[left-1]):
                                break
                        while(right>left):
                            right-=1
                            if(nums[right]!=nums[right+1]):
                                break
                    elif(nums[left]+nums[right]>target):
                        right-=1
                    elif(nums[left]+nums[right]<target):
                        left+=1
            i+=1
        return first

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        first=[]
        i=0
        while(i<len(nums)-2):
            if(nums[i]!=nums[i-1] or i==0):
                target=0-nums[i]
                left=i+1
                right=len(nums)-1
                while(left!=right):
                    if(nums[left]+nums[right]==target):
                        first.append([nums[i],nums[left],nums[right]])
                        while(left<right):
                            left+=1
                            if(nums[left]!=nums[left-1]):
                                break
                        while(right>left):
                            right-=1
                            if(nums[right]!=nums[right+1]):
                                break
                    elif(nums[left]+nums[right]>target):
                        right-=1
                    elif(nums[left]+nums[right]<target):
                        left+=1
            i+=1
        return first

    def myThreeSum(self,nums):
        nums = sorted(nums)
        i = 0
        length = len(nums)
        res = []
        if length <= 2:
            return []
        while (i < length - 2):
            if(nums[i] != nums[i-1]  or i==0):
                target = 0 - nums[i]
                left = i + 1
                right = length -1
                while(left !=right):
                    if (nums[left] + nums[right] == target):
                        res.append([nums[i] , nums[left] ,nums[right]])
                        while left < right:
                            left += 1
                            if (nums[left] != nums[left-1]):
                                break
                        while right > left:
                            right -= 1
                            if (nums[right] != nums[right +1]):
                                break
                    elif (nums[left] + nums[right] > target):
                        right -= 1
                    else:
                        left += 1
            i += 1
        return res

if __name__ == '__main__':
    a = [-4, -1, -1, 0, 1, 2]
    obj = Solution()
    res= obj.myThreeSum(a)
    print(res)
                


# if __name__ == '__main__':
#     nums = [2,7,11,15]
#     tar = 9
#     a =Solution()
#     res = a.twoSum(nums,tar)
#     print(res)


