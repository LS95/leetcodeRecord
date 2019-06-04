#coding=utf-8
# py3
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i  in range(n):
            for j in range(0,i+1):
                matrix[i][j] , matrix[j][i]  = matrix[j][i] , matrix[i][j]
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j] , matrix[i][n-1-j]  = matrix[i][n-1-j] , matrix[i][j]
        return matrix

if __name__ == '__main__':
    a = [[1,2,3],[4,5,6],[7,8,9]]
    b = [
          [ 5, 1, 9,11],
          [ 2, 4, 8,10],
          [13, 3, 6, 7],
          [15,14,12,16]
        ]
    obj = Solution()
    res= obj.rotate(b)
    print(res)
                


# if __name__ == '__main__':
#     nums = [2,7,11,15]
#     tar = 9
#     a =Solution()
#     res = a.twoSum(nums,tar)
#     print(res)


