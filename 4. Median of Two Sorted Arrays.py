#coding=utf-8
# py3
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lenA = len(nums1)
        lenB = len(nums2)
        newLen = lenA +lenB
        newArray = sorted(nums1 +nums2)
        if newLen %2 == 0:
            return (newArray[newLen // 2 -1] + newArray[newLen // 2] ) * 1.0 /2
        else:
            return newArray[newLen // 2]

class Solution_RecursiveApproch(object):
    def findMedianSortedArrays(self, A, B):
        m , n = len(A), len(B)
        if m > n:
            m, n , A ,B  =  n, m , B , A
        if n == 0:
            raise ValueError

        imin ,imax ,half_len = 0 , m , int((m + n + 1) / 2)
        while  imin <= imax:
            i = int((imin + imax) / 2)
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                imin  = i + 1
            elif i> 0  and A[i-1] > B[j]:
                imax = i - 1
            else:
                if i==0:
                    max_of_left = B[j-1]
                elif j==0:
                    max_of_left =  A[i-1]
                else:
                    max_of_left = max(A[i-1],B[j-1])
                if (m + n ) % 2 == 1:
                    return max_of_left
                if i==m:
                    min_of_right = B[j]
                elif j == n :
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i],B[j])

                return  (max_of_left + min_of_right) / 2.0


if __name__ == '__main__':
    a = [1,2,3]
    b = [2,4,6]
    obj = Solution_RecursiveApproch()
    res= obj.findMedianSortedArrays(a,b)
    print(res)
                


# if __name__ == '__main__':
#     nums = [2,7,11,15]
#     tar = 9
#     a =Solution()
#     res = a.twoSum(nums,tar)
#     print(res)


