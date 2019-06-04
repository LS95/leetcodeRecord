#coding=utf-8

class Solution(object):
    def singleNumber(self, nums) -> int:
        # result = 0
        # for each in nums:
        #     result = result ^ each
        # return  result
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except :
                hash_table[i] = 1
        return hash_table.popitem()[0]
if __name__ == '__main__':
    a = Solution()
    res = a.singleNumber([4,1,2,1,2])
    print(res)