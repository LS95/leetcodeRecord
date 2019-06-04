#coding=utf-8

class Solution:
    def plusOne(self, digits):
        res =[0] + digits
        res.reverse()
        print(res)
        ci = 0
        tmp = 0
        for i in range(len(res)):
            if i== 0:
                tmp = res[i] + ci + 1
            else:
                tmp = res[i] + ci
            if (tmp >= 10):
                tmp = tmp % 10
                ci = 1
            else:
                ci = 0
            res[i] = tmp
            print(i ,res[i])
        if(res[-1] == 0):
            res = res[:-1]
        res.reverse()
        return res

    def  plusOneMethod2(self,digits):
        length = len(digits)
        for j in (range(length)[::-1]):
            if digits[j] < 9:
                digits[j] = digits[j] + 1
                return digits
            digits[j] = 0
        res = [1] + digits
        return res

if __name__ == '__main__':
    # main()
    a = Solution()
    res = a.plusOneMethod2([9,9,9])
    print(res)