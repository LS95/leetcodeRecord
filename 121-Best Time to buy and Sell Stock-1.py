#coding=utf-8

class Solution:
    def  maxProfit(self,prices):
        length = len(prices)
        result = 0
        startIndex = 0
        while startIndex < length -1:
            if prices[startIndex+1] < prices[startIndex]:
                print("price down!!!!:{} -> {}".format(prices[startIndex],prices[startIndex+1]))
                startIndex += 1
                continue
            else:
                print("price up:{} -> {}".format(prices[startIndex],prices[startIndex+1]))
                sellIndex = startIndex + 1
                while  sellIndex < length -1 and prices[sellIndex+1] > prices[sellIndex] :
                    sellIndex +=1
                # prices[sellIndex+1] > prices[sellIndex]
                buyIndex =  startIndex
                sellIndex = sellIndex
                profit = prices[sellIndex] - prices[buyIndex]
                result = result + profit
                print("Buy on day {} (price = {}) and sell on day {} (price = {}), profit = {} result now = {}".format(buyIndex,prices[buyIndex],sellIndex,prices[sellIndex],profit ,result))
                startIndex = sellIndex + 1
                continue
        return result

if __name__ == '__main__':
    #nums = [7,1,5,3,6,4]
    nums = [7,6,4,3,1]
    #nums = [1,2,3,4,5]
    a =Solution()
    res = a.maxProfit(nums)
    print(res)
    print("Game Over")


