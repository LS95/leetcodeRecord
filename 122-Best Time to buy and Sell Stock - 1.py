#coding=utf-8

class Solution:
    def maxProfit(self, prices):
        result = 0
        first,second ,maxValue = 0 , 0 ,0
        n = len(prices)
        while  first < n:
            second = first + 1
            buyValue = prices[first]
            while second < n:
                sellValue = prices[second]
                if sellValue <= buyValue:
                    break
                else:
                    currentMaxValue = sellValue
                    for jj in range(second+1,n):
                        if prices[jj] <= currentMaxValue:
                            break
                        else:
                            if prices[jj] > currentMaxValue:
                                currentMaxValue = prices[jj]
                    result = result + (currentMaxValue - buyValue)
                    print("first %s second %s  buyValue %s  sellValue %s ,res = %s"  % (first ,second, buyValue, sellValue, result) )
                second += 1
            first += 1

        return result
        # for k,v in enumerate(prices):
        #     print(k, v)

                
# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j] == target:
#                     return [i,j]
#         return None

if __name__ == '__main__':
    nums = [7,1,5,3,6,4]
    a =Solution()
    res = a.maxProfit(nums)
    print(res)


