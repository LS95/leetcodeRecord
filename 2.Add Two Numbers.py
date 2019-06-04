#coding=utf-8
# py3
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        finalRes = ListNode(0)
        current = finalRes
        carry = 0
        while (l1 != None and  l2 !=None):
            res = (l1.val + l2.val  + carry)  % 10
            carry = (l2.val + l2.val + carry) // 10
            newNode = ListNode(res)
            current.next = newNode
            current = newNode
            l1 = l1.next
            l2 = l2.next  

        if l1:
            current.next = l1
        elif l2:
            current.next = l2
        else:
            current.next = None

        while  current:
            res = (current.val + carry)  % 10
            carry = (current.val + carry ) // 10
            current.val = res
            current = current.next
        
        if carry is 1:
            current.next = ListNode(1)

        return finalRes.next
'''
自定义实现python单链表

class Node(object):
    def __init__(self,x):
        self.val = x
        self.next = None

    def getValue(self):
        return self.val
    def setValue(self,data):
        self.val = data

    def getNext(self):
        return self.next

    def setNext(self,nextNode):
        self.next = nextNode

class LinkedList(object):
    def __init__(self):
        self.head = None

    def  isEmpty(self):
        return self.head == None
    # 头部插入法
    def  add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while  (current!= None):
            current = current.getNext()
            count += 1
        return count


    def  show(self):
        current = self.head
        while current != None:
            print(current.getValue() )
            current = current.getNext()
        # print(" ")

    def search(self,searchValue):
        current = self.head
        found = False
        while  not found and (current != None):
            if  current.getValue() == searchValue:
                found = True
            else:
                current = current.getNext()
        print(found)

    def remove(self,removeValue):
        previous = None
        current = self.head
        found = False
        while not found and current != None:
            if current.getValue() == removeValue:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found == False:
            print("not found {0}".format(item))
        elif current == self.head:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def getValue(self, index):
        current = self.head
        while index:
            index -= 1
            current =current.getNext()
        return current.getValue()

    def insert(self,index,item):
        previous = None
        current = self.head
        count = 0
        temp = Node(item)
        if index  > self.size():
            print("out index")
        elif index == 0:
            temp.setNext(current)
            self.head = temp
        else:
            while index:
                index -= 1
                previous =  current
                current =current.getNext()
            previous.setNext(temp)
            temp.setNext(current)

class Solution(object):
    def addTwoNumbers(self, l1 ,l2):
        newRes = LinkedList()
        len1 = l1.size()
        len2 = l2.size()
        print(l1.size() , l2.size())
        maxLen= max(len1,len2)  
        c = [0 ] * (maxLen + 1)
        num = [0] * maxLen 
        for i in range(maxLen):
            num[i] = l1.getValue(i) + l2.getValue(i) + c[i]
            if num[i] >= 10:
                num[i] -= 10
                c[i+1] = 1
            newRes.add(num[i])
        if c[maxLen] == 1:
            newRes.add(1)
        return newRes


if __name__ == '__main__':
    alist=LinkedList()
    alist.add(3)
    alist.add(4)
    alist.add(2)

    blist =LinkedList()
    blist.add(8)
    blist.add(6)
    blist.add(5)

    alist.show()
    blist.show()

    print(alist.size() , " " , blist.size())
    print(alist.getValue(0))
    print(alist.getValue(1))



    res = Solution()
    finalRes = res.addTwoNumbers(alist,blist)
    finalRes.show()



'''
    # for i in range(10):
    #     alist.add(i)
    # # print(alist)
    # alist.show()
    # print(alist.size())
    # alist.remove(5)
    # alist.show()
    # alist.insert(7,110)
    # alist.show()
    # alist.search(110)

# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         lenA = len(nums1)
#         lenB = len(nums2)
#         newLen = lenA +lenB
#         newArray = sorted(nums1 +nums2)
#         if newLen %2 == 0:
#             return (newArray[newLen // 2 -1] + newArray[newLen // 2] ) * 1.0 /2
#         else:
#             return newArray[newLen // 2]

# class Solution_RecursiveApproch(object):
#     def findMedianSortedArrays(self, A, B):
#         m , n = len(A), len(B)
#         if m > n:
#             m, n , A ,B  =  n, m , B , A
#         if n == 0:
#             raise ValueError

#         imin ,imax ,half_len = 0 , m , int((m + n + 1) / 2)
#         while  imin <= imax:
#             i = int((imin + imax) / 2)
#             j = half_len - i
#             if i < m and B[j-1] > A[i]:
#                 imin  = i + 1
#             elif i> 0  and A[i-1] > B[j]:
#                 imax = i - 1
#             else:
#                 if i==0:
#                     max_of_left = B[j-1]
#                 elif j==0:
#                     max_of_left =  A[i-1]
#                 else:
#                     max_of_left = max(A[i-1],B[j-1])
#                 if (m + n ) % 2 == 1:
#                     return max_of_left
#                 if i==m:
#                     min_of_right = B[j]
#                 elif j == n :
#                     min_of_right = A[i]
#                 else:
#                     min_of_right = min(A[i],B[j])

#                 return  (max_of_left + min_of_right) / 2.0


# if __name__ == '__main__':
#     a = [1,2,3]
#     b = [2,4,6]
#     obj = Solution_RecursiveApproch()
#     res= obj.findMedianSortedArrays(a,b)
#     print(res)
                


# if __name__ == '__main__':
#     nums = [2,7,11,15]
#     tar = 9
#     a =Solution()
#     res = a.twoSum(nums,tar)
#     print(res)


