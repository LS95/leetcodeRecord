#coding=utf-8#coding=utf-8
class Solution:
    def intersection(self, nums1, nums2):
        result = []
        nums1.sort()
        nums2.sort()
        first ,second = 0, 0
        while first < len(nums1):
            while  second < len(nums2):
                if nums1[first] < nums2[second]:
                    first += 1
                    break
                elif nums1[first] > nums2[second]:
                    if second + 1 == len(nums2):
                        return result
                    else:
                        second += 1
                        continue
                else:
                    result.append(nums1[first])
                    first += 1
                    second += 1
                    break
            if second == len(nums2):
                return result
        return result



if __name__ == '__main__':
    # main()
    a = Solution()
    res = a.intersection( [4,9,5],[9,4,9,8,4])
    res = a.intersection( [3,1,2],[1,1])
    #res = a.intersection( [1,2,1,2],[2,2])
    res = a.intersection( [1,2,2,1],[2,2])
    print(res)