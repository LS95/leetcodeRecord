# leetcodeRecord
my leetcodeRecord leetcode刷题记录

# 1.two number  -- easy

## 问题描述 
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

## 输入

数组  目标和
## 输出

数组元素的索引

## 思路

1. brute-force  

    暴力枚举 
    时间复杂度 O(n**2)
    空间复杂度 O(1)
    
2. hash-table 

    第一个存放 值以及索引
    hashMap( nums[i] ,i)
    第二个查找 complement = target-nums[i]是否存在于表中
    
    map.containsKey(complement) && map.get(complement) !=i

    O(n) / O(n)
    
3.  One-pass Hash Table      
    
    一遍   插入的同时进行查找   

4.   新建一个字典 key=   newArray = target - Array[i]  value = i

    遍历数组  索引
    
    newArray.get(Array[i]) &&  newArray.get(Array[i]) !=i :
        return [i, newArray.get(Array[i])]



    
## 代码

py2  brute-force  
``` 
#coding=utf-8

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return None

if __name__ == '__main__':
    nums = [2,7,11,15]
    tar = 9
    a =Solution()
    res = a.twoSum(nums,tar)
    print(res)
```

py3   新建一个字典 存放  newArray = target - Array[i] 的值

```
class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        bArray = {target - num :i  for i,num in enumerate(nums) }
        for i in range(len(nums)):
            if bArray.get(nums[i]) and bArray.get(nums[i]) !=i:
                return [i, bArray.get(nums[i])]

```


# 2. add num  -- medium


## 问题描述
两数相加

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

## 输入
(2 -> 4 -> 3) + (5 -> 6 -> 4)

## 输出

输出：7 -> 0 -> 8
原因：342 + 465 = 807


## 思路

使用python模拟单链表  https://www.cnblogs.com/dream-for/p/5981056.html


1. 对应位数累加  求和  大于10 则进位

    初等数学
    伪代码如下：

将当前结点初始化为返回列表的哑结点。
将进位 arry 初始化为 00。
将 p 和 qq 分别初始化为列表 l1 和 l2 的头部。
遍历列表 l1 和 l2 直至到达它们的尾端。
将 x 设为结点 p 的值。如果 p 已经到达 l1 的末尾，则将其值设置为 00。
将 y 设为结点 q 的值。如果 qq 已经到达 l2 的末尾，则将其值设置为 0。
设定 sum = x + y + carry
更新进位的值，carry = sum / 10carry=sum/10。
创建一个数值为 (sum \bmod 10)(summod10) 的新结点，并将其设置为当前结点的下一个结点，然后将当前结点前进到下一个结点。
同时，将 pp 和 qq 前进到下一个结点。
检查 carry = 1carry=1 是否成立，如果成立，则向返回列表追加一个含有数字 11 的新结点。
返回哑结点的下一个结点。

    

2. 类似加法公式，每次算两个数字的相加，carry保存进位。
先处理l1、l2都有数字的部分；
再处理l1或l2有数字的部分；
最后考虑最高位可能的进位。

## 代码

ref:https://blog.csdn.net/xinxin100011/article/details/81207071

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        finalRes = ListNode(0)
        current = finalRes
        carry = 0
        while (l1 != None and  l2 !=None):
            res = (l1.val + l2.val  + carry)  % 10
            carry = (l1.val + l2.val + carry) // 10
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

        while  current.next:
            res = (current.next.val + carry)  % 10
            carry = (current.next.val + carry ) // 10
            current.next.val = res
            current = current.next
        
        if carry is 1:
            current.next = ListNode(1)

        return finalRes.next
```



# 4. Median of Two Sorted Arrays     --hard 

## 问题描述
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)  / 2 = 2.5

要求找出两个有序集合的中位数  奇数个则为最中间的那个数 
偶数个则为最中间的两个数的平均数 

odd  偶数  
even 奇数 



## 输入

两个数组

## 输出

浮点数 


## 思路

1. 将两个数组合并 重新排序 找到其中位数 (此方法不能满足时间复杂度的要求)

2. https://leetcode.com/problems/median-of-two-sorted-arrays/solution/ 

递归的方法  进行二叉树搜索 

划分为2部分 

左右两边数组元素的个数相同  

左边最大 右边最小 取平均值

设 imin=0，imax=m, 然后开始在 [imin, imax] 中进行搜索
O(log(min(m,n)))
    
  
## 代码

```
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
            
# 正确的方式
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
                
```


# 7- Reverse Integer -- easy

## 问题描述
Given a 32-bit signed integer, reverse digits of an integer.


## 输入
123    -123    120

## 输出
321    -321    21

## 思路

1.  python转为字符串逆序操作 
32位数的范围  -2**31 ， 2 **31 -1

当溢出时返回0

整数取绝对值  
转字符串 [::-1]逆序 
再转整数  添加符号+-1

2. pop原理 

要在没有辅助堆栈 / 数组的帮助下 “弹出” 和 “推入” 数字，我们可以使用数学方法。

//pop operation:
pop = x % 10;
x /= 10;

//push operation:
temp = rev * 10 + pop;
rev = temp;

注意这里判断数据越界的条件:

32位整数范围 [-2**31,2**31-1]
num = 2147483647       
num = -2147483648



## 代码

```
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            res =  int(str(x)[::-1])
        else:
            res =  -1 * int(str(-1*x)[::-1])
        if res >= -2**31 and res <= 2**31 -1:
            return res
        else:
            return 0
            
            
*****

def getReverNumber(x):
    ...:     res = 0
    ...:     c = 1 if x>=0 else -1
    ...:     x = x if x>=0 else -1*x
    ...:     while (x!=0):
    ...:         tmp = x % 10
    ...:         x = x // 10
    ...:         res = 10*res + tmp
    ...:     return  c*res
    
    
*** C++

class Solution {
public:
    int reverse(int x) {
        int rev = 0;
        while(x!=0)
        {
            int pop = x % 10;
            x /= 10;
            if(rev > INT_MAX/10 || (rev == INT_MAX /10 && pop > 7))
                return 0;
            if(rev < INT_MIN/10 || (rev == INT_MIN / 10 && pop < -8))
                return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
};
```

# 8 - String to Integer (atoi) -- easy

## 问题描述

请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，qing返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。


## 输入  输出
输入: "42"
输出: 42
示例 2:

输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
示例 3:

输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
示例 4:

输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
示例 5:

输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
     因此返回 INT_MIN (−231) 。


## 思路

首先去除首部的空字符 

然后找符号位 +  或者 -

遍历字符串  i< length 而且 字符范围'0' -- '9'之间

base = base * 10 + str[i] - '0';

32位整数范围 [-2**31,2**31-1]
num = 2147483647       
num = -2147483648

溢出的判断  
```


if( base > upMax // 10  or (base == upMax // 10 and (ord(str[i]) - ord('0')) > 7 ) ):
```

## 代码

```
class Solution:
    def myAtoi(self,str):
        str= str.strip()
        if len(str) == 0:
            return 0
        fuhao = 1
        base = 0
        i = 0
        upMax =(pow(2,31) -1)
        lowMin = -pow(2,31)
        if(str[i] in '-+'):
            if str[i] == '-':
                fuhao = -1 
            else:
                fuhao = 1
            i += 1

        while(i<len(str) and (str[i]>='0' and str[i]<='9')):
            if( base > upMax // 10  or (base == upMax // 10 and (ord(str[i]) - ord('0')) > 7 ) ):
                if fuhao == 1:
                    return upMax
                else:
                    return lowMin
            base = 10 * base + int(ord(str[i]) - ord('0'))
            i = i + 1
        return fuhao * base
```



# 13 -  Roman to Integer - Easy 

## 问题描述


Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000


## 输入输出

```
Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

```

## 思路

首先新建整形数组 将每个字母转成整数 

然后考虑特殊的情况  
IV 4
IX 9
XL 40
XC 90
CD 400
CM 900

如果相邻的两个 前面的比后面的值小  则需要考虑 加上较小值取反  

## 代码

```
class Solution{

public:
    int romanToInt(string s)
    {
        int RTI[s.size() + 1] = {0};
        int max, i;
        max = 0;
        for(i = 0 ;i < s.size(); i++)
        {
            switch(s[i])
            {
                  case 'I':RTI[i] = 1;break;
                  case 'V':RTI[i]=5;break;
                  case 'X':RTI[i]=10;break;
                  case 'L':RTI[i]=50;break;
                  case 'C':RTI[i]=100;break;
                  case 'D':RTI[i]=500;break;
                  case 'M':RTI[i]=1000;break;
            }
        }
        for( i=0; i<s.size(); i++)
        {
            max += (RTI[i]>= RTI[i+1])?RTI[i]:(-1*RTI[i]);
        }
        return max;
        
    }

};
```





*** 


# 14 - Longest Common Prefix 最长公共前缀-- easy

## 问题描述

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

## 输入  输出

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z


## 思路

首先将字符串数组 按照长度进行排序 

第一个元素就是长度最大的字符串


然后前缀依次添加字符进行判断  

需要后面所有的字符串满足此前缀  

如果有任意一个不满足 则返回


```
if( base > upMax // 10  or (base == upMax // 10 and (ord(str[i]) - ord('0')) > 7 ) ):
```

## 代码

```
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if len(strs) == 0:
            return res
        strs.sort(key=lambda i: len(i))
        # print(strs)
        for i in range(len(strs[0])):
            tmp = res +  strs[0][i]
            # print("tmp=",tmp)
            for each in strs:
                if each.startswith(tmp) == False:
                    return res
            res = tmp
        return res
```


# 15-  3Sum - Medium

## 问题描述

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

## 输入

 nums = [-1, 0, 1, 2, -1, -4]，

## 输出

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

## 思路

最终将3Sum拆解为2Sum+X，2Sum可以先排序，然后再用收尾慢慢收缩的方式寻找target，并且可以在寻找时剔除相同的left，right，时间复杂度因为O(N)。在3Sum中，则需要每个nums[]中的元素都作为X一次，因此O(N^2)，比上方最起码的O(N^3)要好不少。

具体步骤:  
固定一个值 value  寻找另外两个的组合i , j  使得  i+ j = -target   
i,j 分别从左向右遍历  正好找到 则添加   
小了left ++   大了 right--




--------------------- 
作者：傲慢灬 
来源：CSDN 
原文：https://blog.csdn.net/jerry81333/article/details/76020793 


其他思路:
    Leetcode 15:三数之和（最详细解决方案！！！）
    https://blog.csdn.net/qq_17550379/article/details/80614597
    
    
## 代码

```
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
```



# 19   Remove Nth Node From End of List   删除链表里面倒数第N个结点 -  Medium

## 问题描述
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

## 输入输出
给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.

## 思路

设置两个指针  first 和 second  间隔为n
当second到达指针末尾时  first 指向要删除元素的前一个结点 
这样一次遍历即可完成

(first 首先移动n位  然后second和first同时移动 直到first到达末尾NULL
此时second即为要删除的位置)  本质上second和first差距为n




另外的一种需要先统计出来链表的长度 然后从 N-n+1的位置开始脱链操作。此方法需要遍历2次 效果不好。

## 代码

```C++  
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head==NULL)
            return NULL;
        if(head->next==NULL && n==1)
            return NULL;
        ListNode *dummy = new ListNode(0);
        dummy -> next = head;
        ListNode *first = head , *second=head;
        while(first)
        {
            int tmp = n;
            second = first;
            while(tmp--)
            {
                second = second->next;
            }
            if(second == NULL)
            {
                return head->next; //总共n个元素 删除倒数第n个 则返回head的下一个元素
            }
            if(second->next == NULL)
            {
                break;
            }else{    
                first = first->next;
            }
             
        }
        first->next  = first->next->next;
        return dummy->next;
    }
};


补充C:
新建头结点

Node* result = (Node *)malloc(sizeof(Node));



JAVA

public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode first = dummy;
    ListNode second = dummy;
    // Advances first pointer so that the gap between first and second is n nodes apart
    for (int i = 1; i <= n + 1; i++) {
        first = first.next;
    }
    // Move first to the end, maintaining the gap
    while (first != null) {
        first = first.next;
        second = second.next;
    }
    second.next = second.next.next;
    return dummy.next;
}
```



*** 


# 20 - Valid Parentheses   有效的括号 - Easy 
## 问题描述

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。


## 输入输出
示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

## 思路

利用栈的思想  如果是左括号则入栈 

找到匹配的右括号则弹出  

最后判断栈是否为空 

## 代码

```
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = []
        for c in s:
            if c in ['(', '[', '{']:
                res.append(c)
            elif c == ')':
                if not res or res.pop() != '(' : return False
            elif c == ']':
                if not res or res.pop() != '[' : return False
            elif c == '}':
                if not res or res.pop() != '{' : return False
            else:
                return False
        return False if res else True


```
***



# 21   Merge Two Sorted Lists -合并2个有序的链表 -  Easy

## 问题描述
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

## 输入输出


输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4


## 思路

设置两个指针  比较大小 依次赋值

如果都到了末尾 则退出


## 代码

```python


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = tail = ListNode
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        
        return dummy_head.next
        
        
//C++

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *head= new ListNode(0) ,*p1=l1 ,*p2 = l2;
        ListNode *tmp = head;
        while(p1!=NULL && p2!=NULL)
        {
            if((p1->val < p2->val)) 
            {
                tmp->next = p1;
                p1 = p1->next;
            }else
            {
                tmp->next = p2;
                p2 = p2->next;
            }
            tmp = tmp->next;
        }
        if(p1)
            tmp->next=  p1;
        if(p2)
            tmp->next = p2;    
        
        return head->next;
    }
 
};
```


# 26- Remove Duplicates from Sorted  -- easy

## 问题描述
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.



## 输入
[1,1,2],   [0,0,1,1,1,2,2,3,3,4],


## 输出
2  5

## 思路

1.  方法：双指针法
算法

数组完成排序后，我们可以放置两个指针 i 和 j，其中 i 是慢指针，而 j 是快指针。只要nums[i]=nums[j]，我们就增加 j以跳过重复项。

当我们遇到 nums[j]  ！=nums[i]，跳过重复项的运行已经结束，因此我们必须把它（nums[j]nums[j]）的值复制到 nums[i + 1]nums[i+1]。然后递增 i，接着我们将再次重复相同的过程，直到 j 到达数组的末尾为止。

2. 



## 代码

``` java
public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int i = 0;
    for (int j = 1; j < nums.length; j++) {
        if (nums[j] != nums[i]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}
            
*****
py3
    def removeDuplicates(self, nums):
        if len(nums) <=0:
            return None
        if len(nums) == 1:
            return 1
        resNum = 1
        i = 0
        start = nums[0]
        listLen = len(nums)
        while i < listLen :
            j = i + 1
            while j < listLen:
                tmp = nums[j]
                if tmp == start:
                    nums.remove(nums[j])
                    listLen -= 1
                else:
                    resNum += 1
                    start = tmp
                    break 
            i = i + 1
```
# 26- Valid Sudoku  -- Medium 

## 问题描述
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。    
数字 1-9 在每一列只能出现一次。   
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。   



## 输入
输入:
```
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

```
## 输出
输出: true

## 思路

1.  按照指定的规则 如果每一行里面有两个元素数值相同 而且下标不同 则返回False
2.  依次检查每一行 每一列 每一个小格子内部的数值
3.  cell的范围     row // 3  * 3  将0-8映射到 0--6



## 代码

```
*****
py3

class Solution:
    def isValidSudoku(self, board) -> bool:
        rowLen = len(board)
        colLen = len(board[0])
        for row in range(rowLen):
            for col in range(rowLen):
                if board[row][col] == '.':
                    board[row][col] = 0
        for row in range(rowLen):
            for col in range(rowLen):
                # row check
                    for tmp in range(colLen): 
                        if board[row][tmp] !=0 and tmp != col and board[row][tmp] == board[row][col]:
                            return False
                # column check
                    for tmp2 in range(rowLen): 
                        if board[tmp2][col] !=0 and tmp2 != row and board[tmp2][col] == board[row][col]:
                            return False
                # cell  check
                    cellrowStart = row // 3 * 3
                    cellcolStart = col // 3 * 3
                    for i in range(cellrowStart,cellrowStart+3):
                        for j in range(cellcolStart,cellcolStart+3):
                            if(board[i][j] !=0 and board[i][j] == board[row][col] and row!=i and col!=j):
                                return False
        return True


```


# 28 - Implement strStr() 实现strstr 判断一个字符串在另个字符串中出现的位置  -- Easy

## 问题描述
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。



当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。


## 输入  输出
示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1


## 思路

1. 遍历 判断一定长度字符串相等
2. 从头开始 依次判断是否每一个字符相等 不相等则向后遍历

好的思路是使用KMP匹配算法。



## 代码

```
*****
py3

    def strStr(self, haystack, needle):
        lenA , lenB = len(haystack) , len(needle)
        if lenA < lenB:
            return -1;
        if lenB == 0 or haystack == needle:
            return 0
        for i in range(0 , lenA - lenB  +1):
            if haystack[i :i + lenB] == needle:
                return i
        return -1

C

int strStr(char* haystack, char* needle) {
    if (strlen(needle) == 0)
	{
		return 0;
	}
	int i, j , lenA = strlen(haystack) ,lenB = strlen(needle);
	for (i = 0; i <= lenA - lenB; ) //注意此处为等号
	{
		int tmp = i;
		j = 0;
		while (haystack[i] == needle[j] && haystack[i] && needle[j])
		{
			i++;
			j++;
		}
		if (j == lenB)
		{
			return tmp;
		}
		else {
			i = tmp +  1;
		}
	}
	return -1;
}

简化版
int strStr(char* haystack, char* needle) {
    if (strlen(needle) == 0)
	{
		return 0;
	}
	int i, j , lenA = strlen(haystack) ,lenB = strlen(needle);
	for (i = 0; i <= lenA - lenB; i++ )
	{
		int tmp = i;
		j = 0;
		while (haystack[tmp] == needle[j] && haystack[tmp] && needle[j])
		{
			tmp++;
			j++;
		}
		if (j == lenB)
		{
			return i;
		}
	}
	return -1;
}

```
# 38  - Count and Say 报数  -- Easy

## 问题描述
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

 


## 输入  输出
示例 1:

输入: 1
输出: "1"
示例 2:

输入: 4
输出: "1211"


## 思路

就是对于前一个数，找出相同元素的个数，把个数和该元素存到新的string里。

：根据报数的特点，我们可以根据上一项的结果推导下一项。我们遍历上一项，辅以计数变量统计一下某些数字出现的次数。同时我们要不断保存上一项。


也就是先输出个数，然后输出元素



## 代码

```
*****
py3

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return  "1"
        elif n == 2:
            return "11"
        pre = "11"
        for i in range(3, n+1):
            res  = ''
            count = 1
            length = len(pre)
            for j in range(1, length):
                if pre[j-1] == pre[j]:
                    count += 1
                else:
                    res = res + str(count) +pre[j-1]
                    count = 1
            res = res + str(count) + pre[j]
            pre = res
        return res
}
```

# 48 - Rotate Image  -- easy

## 问题描述
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。


## 输入

示例 1:

给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],



## 输出
原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
## 思路

a.如果可以使用新的空间 可以新开辟一个数组 
根据转换后的关系  num[j][n-1-i] = num[i][j]  进行新元素的置换

b.注意不能使用新的空间的情况下
顺时针旋转90度可以等价为
1.  沿着对角线 交换元素  

2.  对于每一行 沿着y轴中轴进行翻转  



## 代码

```
py3

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i  in range(n):
            for j in range(0,i+1):
                matrix[i][j] , matrix[j][i]  = matrix[j][i] , matrix[i][j]
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j] , matrix[i][n-1-j]  = matrix[i][n-1-j] , matrix[i][j]
        #return matrix
```


# 53 Maximum Subarray 最大子数组   - Easy Medium  Hard

## 问题描述

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:



## 输入输出
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
## 思路

动态规划法 

从头到尾遍历数组  对于每一个整数 有如下的选择 
1. 前面整体元素之和大于等于0  =>  加入之前的SubArray
2. 自己另起一个SubArray =>       前面总体元素之和 <0 

设状态为f[j]，表示以S[j]结尾的  最大连续子序列和，则状态转移方程如下：

f[j]=max(f[j−1]+S[j],S[j]),其中1≤j≤n

target=max{f[j]},其中1≤j≤n




## 代码

```
C++ 动态规划法  dynamic programming 

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int result = INT_MIN;
        int  tmpMax =  0;
        for(int i=0 ; i < nums.size(); i++)
        {
            tmpMax  =  max(nums[i], tmpMax + nums[i]);
            result =  max(result, tmpMax);
        }
        return result;
    }
};



使用一个变量记录前面子数组元素的和 

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int result = 0;
        int len = nums.size();
        int tmpMax= nums[0], sum = nums[0];
        for(int i=1;i<len;i++)
        {
            if(sum>0)
            {
                sum +=  nums[i];
            }else{
                sum = nums[i];
            }
            tmpMax = max(tmpMax, sum);
        }
        return tmpMax;
    }
};


```
***



# 66 - Plus One  - Easy

## 问题描述

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:




## 输入
Input: [1,2,3]

## 输出
Output: [1,2,4]
Explanation: The array represents the integer 123.
## 思路

1. 数组逆序 从最后一位开始加一  注意进位 


2. 从最后一位开始 如果小于9则此位+1 直接返回

否则 说明==9 则将此位置0

最后的情况如果有[9,9,9]

需要新建一个数组 最前面置1

res = [1] + digits


## 代码

```
1. 
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

2.     
    def  plusOneMethod2(self,digits):
        length = len(digits)
        for j in (range(length)[::-1]):
            if digits[j] < 9:
                digits[j] = digits[j] + 1
                return digits
            digits[j] = 0
        res = [1] + digits
        return res

```


# 70 -  Climbing Stairs 爬楼梯 - Easy

## 问题描述

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？




## 输入输出
注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

## 思路

爬n阶段楼梯  倒过来想 

如果最后上1阶  前面要上 n-1阶 的方法   
如果最后上2阶  前面要上 n-2阶 的方法 

所以相当于斐波那契数量 
n  f(n)  
1  1  
2  2  
3  3  
4  5  
......

但是用递归的方法会多次计算 到时耗时略长 

可以使用数组的方法代替计算  



只有两种办法爬楼，每次一步或者每次两步。

可以这样想，n个台阶，一开始可以爬 1 步，也可以爬 2 步，那么n个台阶爬楼的爬楼方法就等于 一开始爬1步的方法数 + 一开始爬2步的方法数，这样我们就只需要计算n-1个台阶的方法数和n-2个台阶方法数，同理，计算n-1个台阶的方法数只需要计算一下n-2个台阶和n-3个台阶，计算n-2个台阶需要计算一下n-3个台阶和n-4个台阶……

而我们可以很容易直到，1个台阶只有 1 种方法，2个台阶有 2 种方法。

我们还发现，在计算时会有大量重复计算，比如上面所说的：计算n要计算n-1和n-2，在计算n-1时要计算n-2和n-3，而n-2被重复计算了两遍，所以建立一个数组nums[n+1]来保存n个台阶的爬楼方法数，这样可以避免重复计算。

直到n-1<=2,n-2<=2时，可以直接求得n的个数，返回上一层递归。


## 代码

```

class Solution {
    public int climbStairs(int n) {
        if (n == 1)
            return 1;
        else if (n == 2)
            return 2;
        else {
            int[] ans = new int[n];
            ans[0] = 1;
            ans[1] = 2;
            for(int i=2;i<n;i++) {
                ans[i]=ans[i-1]+ans[i-2];
            }
            return ans[n-1];
        }
    }
}



class Solution {
    public int climbStairs(int n) {
        if(n == 1) return 1;
        if(n == 2) return 2;
        int pre1 = 2,pre2 = 1;
        for(int i = 2;i < n; i++){
            int cur = pre1 + pre2;
            pre2 = pre1;
            pre1 = cur;
        }
        return pre1;
    }
}


```
***



# 88 Merge Sorted Array 合并两个有序数组 - Easy 

## 问题描述

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

## 输入输出

```
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
```



## 思路
1. 开辟额外的空间  从前向后找两个list里面的较小值 然后取出来放到第三个开辟的空间中

2.  从后向前插入

假设array1有足够的空间了，于是我们不需要额外构造一个数组，并且可以从后面不断地比较元素进行合并。

比较array2与array1中最后面的那个元素，把最大的插入第m+n位
改变数组的索引，再次进行上面的比较，把最大的元素插入到array1中的第m+n-1位。
循环一直到结束。循环结束条件：当index1或index2有一个小于0时，此时就可以结束循环了。如果index2小于0，说明目的达到了。如果index1小于0，就把array2中剩下的前面的元素都复制到array1中去就行。

作者：小碧小琳
链接：https://www.jianshu.com/p/88203168eb42
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。

## 代码

```

1. C++

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int index1 = 0, index2 = 0 , k = 0;
        vector<int> tmp;
        while(k< m+n)
        {
            if(index1 < m &&  index2 < n)
            {
                if(nums1[index1] < nums2[index2])
                {
                tmp.push_back(nums1[index1]);
                index1++;
                }else{
                tmp.push_back(nums2[index2]);
                index2++;
                }
            }else{
                if(index1 < m)
                {
                    tmp.push_back(nums1[index1]);
                    index1++;
                }
                else{
                     tmp.push_back(nums2[index2]);
                     index2++;
                }
            }
            
            k++;
        }
        nums1 = tmp;
    }
};




2. Python

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index1 = m - 1
        index2 = n - 1
        while index2 >= 0:
            if index1 < 0:
                nums1[0:index2+1] = nums2[0:index2+1]
                break
            
            if nums1[index1] >= nums2[index2]:
                nums1[index1 + index2 +1] = nums1[index1]
                index1 = index1 - 1
            else:
                nums1[index1 +index2 + 1] = nums2[index2]
                index2 -= 1
            
                                      





```
***


# 98 Validate Binary Search Tree 验证二叉搜素树 -  Medium 

## 问题描述
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

## 输入输出
```
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。


```

## 思路

1. 递归方法  

    如果存在左子树 左子树的节点的值 小于 根节点
    
    如果存在右子树  同样需要满足此要求  
    
    递归判断其左子树 和 右边的子树  
    
    但是需要注意的问题是:  
    
    节点左子树的所有节点都小于当前节点，而不是仅仅左根节点小于root，对于右子树同理。
    
    特殊情况
    
    ![A712Sf.jpg](https://s2.ax1x.com/2019/04/11/A712Sf.jpg)

    
    
    要保证当前的树在对应区间内即可。

2. 

中序遍历   

左子树 <  根节点  <  右子树 

遍历之后的序列 应该是递增的序列 



## 代码




```
1. py 


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root , left=None, right = None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        if left and left.val >= root.val:
            return False
        if right and right.val <= root.val:
            return False
        
        return self.isValidBST(root.left, left, root) and self.isValidBST(root.right, root, right);
        
        
2. py 中序遍历 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        pre = None
        stack = list()
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if pre and root.val <= pre.val:
                    return False
                
                pre = root
                root = root.right
        return True


```
***



# 101 - Symmetric Tree  对称二叉树 -  Easy


## 问题描述

给定一个二叉树，检查它是否是镜像对称的。




## 输入输出  

```
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:



```


## 思路


如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

1. 递归方法

判断此节点下面的左右节点  如果都为None 则到了叶子节点  返回True   

如果两个节点都有值  则返回  值相等的情况下

左左 ==  右右  同时 p.left  == q.right 都需要递归满足  




## 代码

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def func(self, p , q):
        if None == p or None == q:
            if p == q: # both None 
                return True
            else:
                return False
        else:
            return  p.val == q.val and self.func(p.left, q.right) and  self.func(p.right , q.left)
        
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return (self.func(root.left, root.right))

 ```


***


# 102 - Binary Tree Level Order Traversal  二叉树层次遍历  -   Medium

## 问题描述

给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。


## 输入输出
例如:
给定二叉树: [3,9,20,null,null,15,7],

```

   3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]


```


## 思路

这是一个BFS问题，首先可以想到就是通常的解法。我们可以使用queue解决，在python中，我们可以通过from queue import Queue。也可以使用list来解决，不过在使用list的时候要注意，我们如果pop操作的话，要添加一个参数pop(0)，表示我们pop最前面的元素。

这里我们要注意一下，外部循环条件，我们不可以写成while q:，因为当输入是[]，这个时候q=[[]]，python对这个结果的判定是True，参看这篇文章python中的and和or。我们这里可以使用while any(q).


## 代码

```
1. ref:https://blog.csdn.net/qq_17550379/article/details/80824320 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return list()
        q, res = [root] , []
        while any(q):
            cur = list()
            len_q = len(q)
            for _ in range(len_q):
                node = q.pop(0)
                cur.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(cur)
        return res

 ```



# 104 -  Maximum Depth of Binary Tree   - Easy  

## 问题描述

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。


## 输入输出
示例：
给定二叉树 [3,9,20,null,null,15,7]，

```

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 


```


## 思路

1. 递归的方法

如果到了叶子节点  则返回 1  因为子节点为NULL

否则找左右节点里面较大的值  + 1

如果一棵树只有一个结点，那么它的深度为1；

如果根结点只有左子树没有右子树，那么树的深度是左子树的深度加1，加1是加上根节这一层。

如果既有左子树又有右子树，那么树的深度应该是左、右子树中深度较大的值再加1



2. 非递归的方法

类似于广度优先遍历  

首先记录 每一层的元素的个数  然后放入队列  计数++  

然后出队列 如果存在左子树  和  右子树   则放入队列 

循环 直到队列为空  



## 代码

```
1. 

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root == NULL)
            return 0;
        int leftDepth =  maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        int maxLen = (leftDepth > rightDepth) ? (1+leftDepth) : (1+rightDepth);
        return maxLen;
    }
};


2.  

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root == NULL)
            return 0;
        queue<TreeNode* >q;
        q.push(root);
        int level = 0;
        while( !q.empty())
        {
            int len = q.size();
            level++;
            while(len--)
            {
                TreeNode *tem = q.front();
                q.pop();
                if(tem->left) 
                {
                    q.push(tem->left);
                }
                if(tem->right)
                {
                    q.push(tem->right);
                }
                
            }
        }
        
        
        return level;
    }
};

```

# 108 - Convert Sorted Array to Binary Search Tree 将有序数组转换成二叉搜素树   - Easy 

## 问题描述  
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。


## 输入输出

```
示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

```


## 思路

1，平衡二叉树：空树或者它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树也都是平衡树。

2，二叉搜索树：空树或者二叉树的所有节点比他的左子节点大，比他的右子节点小。

知道上述概念后，由于我们输入的是有序数组，只需要从中间对分，中间数作为根节点，左侧数组为左子树，右侧数组为右子树，此时左右子树结点数目最多相差1个，再依次递归左右子树。满足条件的高度平衡二叉搜索树就出现了。


## 代码

```
C++  

class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if(nums.empty()) return NULL;
        
        TreeNode* root=new TreeNode(nums[nums.size()/2]);
        vector<int> vec_l=vector<int>(nums.begin(),nums.begin()+nums.size()/2);
        vector<int> vec_r=vector<int>(nums.begin()+nums.size()/2+1,nums.end());
        root->left=sortedArrayToBST(vec_l);
        root->right=sortedArrayToBST(vec_r);
        
        return root;
    }
};


Python3 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


```
***

# 118  Pascal's Triangle   - Easy 

## 问题描述
帕斯卡三角形  
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。


## 输入输出

[
[1],             1   1 
[1,1],           2   1
[1,2,1],         3   1 2
[1,3,3,1],       4   1 3 
[1,4,6,4,1]      5   1 4 6
[1,5,10,10,5,1]  6   1 5 10 
]
## 思路

1. 
首先图形是三角形  然后每一行都是轴对称的 
根据规则  
a[i][j] = a[i-1][j-1]+a[i-1][j]

找到每一行 轴对称加入


2. 

## 代码

```
1. Python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res  = []
        for i in range(numRows):
            tmpList = [1] * (i+1)
            for j in range(i):
                if j == 0:
                    num  = 1
                else:
                    num = res[i-1][j-1] + res[i-1][j]
                tmpList[j] = tmpList[i-j] =  num
            res.append(tmpList)
        return res

简化版代码：

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1] * (i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1]+pascal[i-1][j]
        return pascal



2. C++版

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res;
        for(auto i=0; i< numRows;i++)
        {
            res.push_back(vector<int>(i+1,1));
            for(auto j= 1; j< i; j++)
            {
                res[i][j] = res[i-1][j] + res[i-1][j-1];
            }
            
        }
        return res;
    }
};

```
***



# 121- Best Time to Buy and Sell Stock - easy

## 问题描述
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

## 输入

: [7,1,5,3,6,4]

## 输出
 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

## 思路

1. 类似于波峰 波谷法  找到连续的波峰和波谷

1.1 从前向后找起  如果遇到价格下降的时候   则记录新的开始    
1.2 遇到价格上升的时候 一直查找 直到最高价格时候   卖出    
1.3 尽可能次数多的买卖股票  


2. 一次性遍历法 

利润 = 所有连续两个上升的数值相减法


## 代码

``` py3
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

C++
class Solution {
public:
	int maxProfit(vector<int>& prices) {
		int result = 0;
		int length = prices.size();
		int i = 0 ,vally,peak;
		while (i < length - 1)
		{
			while (i < length - 1 && prices[i] > prices[i + 1])
			{
				i++;
			}
			vally = prices[i];
			while (i < length - 1 && prices[i] < prices[i + 1])
			{
				i++;
			}
			peak = prices[i];
			result = result + (peak - vally);
		}
		return result;
	}
};


C++ DP

class Solution {

public:
    int maxProfit(vector<int>& prices) {
        auto n = prices.size();
        
        if (n == 0)
            return 0;
        
        int prof[n][2];
        int res = 0;

        // prof[x][0]: lowest prices from day 0 to day x  最低价格
        // prof[x][1]: maximum profit from day 0 to day x 最高利润
        prof[0][0] = prices[0];
        prof[0][1] = 0;
        for (auto i = 1; i < n; i++) {
            prof[i][1] = max(prices[i] - prof[i - 1][0], prof[i - 1][1]);
            prof[i][0] = min(prices[i], prof[i - 1][0]);
        }
        return prof[n - 1][1];
    }
};



另外的要求 
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

数组中找到一组可以获得利润的值，然后不断更新他的最大值和最小值，两者最后之差就是他的结果。

思路:

数组中找到一组可以获得利润的值，然后不断更新他的最大值和最小值，两者最后之差就是他的结果。


Java 


class Solution {
    public int maxProfit(int[] prices) {
      if(prices.length==0)return 0;
        int max=0,min=prices[0];
        for(int i=1;i<prices.length;i++){
            min=Math.min(prices[i],min);
            max=Math.max(max,prices[i]-min);
        }
        return max;
    }
}



C++ 

class Solution {
public:
    int maxProfit(vector<int>& prices) {
       if(prices.size() ==0)
            return 0;
       int tmpMin = prices[0];
       int tmpMax = 0;
       for(int i=0; i<prices.size();i++)
       {
            tmpMin = min(tmpMin ,prices[i]);
            tmpMax = max(tmpMax , prices[i] - tmpMin);
        }
        
        return tmpMax;

    }
};


```
# 125- Valid Palindrome - 验证回文串 - easy

## 问题描述
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

## 输入
示例 1:    

输入: "A man, a plan, a canal: Panama"


示例 2:

输入: "race a car"

## 输出
示例 1:  
输出: true

示例 2:  
输出: false

## 思路

1. 保留合法的字符 使用字符串逆序的方式进行判断[::-1]


2. 从左向右判断  处理大小写判断相等的方法

(s[start]-'a'+32)%32 == (s[end]-'a'+32)%32


## 代码

``` 

1.py3

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = "".join([each for each in s.lower() if( (each>='a'and each<='z')  or ( each>='0' and each <='9'))])
        return newS == newS[::-1]

2. C++
class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0, right = s.size()-1;
        while (left < right) {
            if (!isalnum(s[left])) ++left;
            else if (!isalnum(s[right])) --right;
            // deal with upper&lower case at once
            else 
                if ((s[left]+32-'a')%32 != (s[right]+32-'a')%32) 
                    return false;
                else 
                {
                    ++left; 
                    --right;
                }
        }
        return true;
    }
};



3. 递归和非递归的方法


bool isHWRecursion(char * str, int length)
{
	int i;
	if (length == 0 || length == 1) // 长度等于0则返回真
		return true;
	if (str[0] != str[length - 1])  // 判断第一个和最后一个字符是否相同
		return false;
	return isHWRecursion(++str, length - 2); // 判断长度-2的字符
}


bool isHWUnRecursion(char *str, int length)
{
	int start = 0, end = length - 1;
	while (start < end)
	{
		if (str[start] == str[end])
		{
			start++;
			end--;
		}
		else {
			return false;
		}
	}
	return true;
}

```





# 136- Single Number I - easy

## 问题描述
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

## 输入

Input: [4,1,2,1,2]

## 输出
Output: 4


## 思路
1. 快速方法
根据位运算  a ^ a = 0

0 ^ number = number


2. 创建新的列表 遍历元素 如果没在里面则添加 如果在里面则删除操作
append  remove  

3.创建哈希表 {}   key 为元素的值  value为1   如果存在则弹出 否则插入

4. 利用数学的方法

2∗(a+b+c)−(a+a+b+b+c)=c

return  2* sum(set(num)) - sum(nums) 

## 代码

```
    def singleNumber(self, nums) -> int:
        result = 0
        for each in nums:
            result = result ^ each
        return  result

```

# 137- Single Number II - easy

## 问题描述
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:


## 输入

Input: [0,1,0,1,0,1,99]

## 输出
Output: 99


## 思路
1. 利用数学的方法

3∗(a+b+c)−(a+a+a+b+b+b+c)=2c

return  (3* sum(set(num)) - sum(nums) ) // 2;


2. 利用bit位的运算  

首先计算1~32bit位上1的个数  存在三个数 则bit 1的数量一定能被3整除  
将数组中所有数字 bit1的位数相加  对三求余数
最后单一的数字 就是最终的树

3. 真值表的方法 

https://blog.csdn.net/yutianzuijin/article/details/50597413  
http://www.cnblogs.com/grandyang/p/4741122.html



## 代码

``` 
    1. py3
    def singleNumber(self, nums) -> int:
        return  (3 * sum(set(nums)) - sum(nums) ) // 2
    
    2. c
    int findSingleNumberIn3(int *nums, int n)
    {
    	int result = 0, i = 0 ,j=0;
    	for (i = 0; i < 32; i++)
    	{
    		int tmp = 0;
    		for (j = 0; j < n; j++)
    		{
    			tmp +=  (nums[j] >> i) & 1;
    			//tmp = tmp + ((nums[j] >> i) & 1);
    		}
    		result |= ( tmp % 3) << i;
    		//printf("i=%d\t result=%d\n", i, result);
    	}
    
    	return result;
    }

    3. 真值表 ab分别代表 个位和十位  
    出现 0 、1、2、3（0次）
    00 ->  01  -> 10  -> 00
    
    
    class Solution {
    public:
    int singleNumber(vector<int>& nums) {
        int a = 0, b = 0;
        for (int i = 0; i < nums.size(); ++i) {
            b = (b ^ nums[i]) & ~a;
            a = (a ^ nums[i]) & ~b;
        }
        return b;
    }
};

```
# 141- Linked List Cycle  环形链表 - easy

## 问题描述
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

## 输入输出
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。




## 思路
1. 利用快慢指针 开始时都指向头结点

慢指针每次前进1  快指针每次前进2 

如果某次指向同一个位置 则说明存在环  

注意结束条件  while(fast!=NULL &&  fast->next!=NULL)

，如果有环的话，快指针总会和慢指针相遇


2. 递归的思路 

让每个节点的next指向自己 一遍遍历结束后 会遇到自己指向自己的节点 说明有环。  





## 代码

``` 
1. c++  

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
    bool hasCycle(ListNode *head) {
        bool result = false;
        if(head == NULL || head->next == NULL)
            return false;
        ListNode *slow = head;
        ListNode *fast = head;
        while(fast!=NULL && fast->next !=NULL)
        {
           
            slow = slow->next;
            fast = fast->next->next;
             if(fast == slow)
                return true;
            
        }
        return result;
    }
};
    
   
2.
bool hasCycle(ListNode *head)
{
    if(head == NULL || head->next == NULL)
        return false;
    if(head->next == head)
        return true;
    ListNode *tmp = head->next;
    head->next = head;
    bool isCycle = hasCycle(tmp);
    return isCycle;
    
}
```

# 155 - Min Stack 最小栈

## 问题描述

设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。

## 输入输出
```
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.


```

## 思路  

1. 使用2个栈 

    其中一个栈存放所有的元素   另一个栈存放当前的最小值  
    入栈时放入第一个栈 同时如果小于第二个栈的最小值 也放入第二个栈  
    出栈时 如果当前值是第二个栈的栈顶  则两个栈同时pop操作  
    
2. 使用一个栈 同时加上最小的值  

    可以用一个栈实现，加一个变量存储当前的最小值，每次push时，如果新push进来的元素比当前的最小值还要小，将当前的最小值x与要push的数据一起push（一共push两次   先push当前最小值  再push x），再修改最小值；pop时，如果正好pop出最小的元素，那么下一个最小的元素一定就在栈顶，赋值给min 后再pop出去（pop两次）。




## 代码

```

1.C++

class MinStack {
    
    
private:
    stack<int> s1;
    stack<int> minValue;
public:
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        s1.push(x);
        if(minValue.empty() || x <=getMin())
        {
            minValue.push(x);
        }
    }
    
    void pop() {
        if(s1.top() == getMin())
        {
            minValue.pop();
        }
        s1.pop();
    }
    
    int top() {
        return s1.top();
    }
    
    int getMin() {
        return minValue.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */


2.C++

class MinStack {
    
private:
    int min;
    stack<int> s;
public:
    /** initialize your data structure here. */
    MinStack() {
        min = INT_MAX;
    }
    
    void push(int x) {
        if(x <= min)
        {
            s.push(min);
            min = x;
            s.push(x);
        }else{
            s.push(x);
        }
    }
    
    void pop() {
        if(top() == min)
        {
           s.pop(); 
           min = s.top();
           s.pop();
        }else{
           s.pop();
        }
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */

```
***

# 189- rotate array -- easy

Given an array, rotate the array to the right by k steps, where k is non-negative.

数组循环右移 输出新的数组

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

## 输入

数组  n  右移数K>=0 

## 输出

新的数组

## 思路

1. 循环k次 每次    向右移动1个元素   最后一个元素放到头部   Time complexity : O(n*k)  Space complexity O(1)
2. 3次旋转  整体逆序 +   0-k逆序  +   k-len-1逆序
3. 使用额外的数组  原始i 元素到了 i+k  然后将新数组拷贝到原始的数组中  O(n) /   O(n)

```
        int[] a = new int[nums.length];    
        for (int i = 0; i < nums.length; i++) {  
            a[(i + k) % nums.length] = nums[i];  
        }  
        for (int i = 0; i < nums.length; i++) {  
            nums[i] = a[i];  
        }
```

4. 使用额外的变量temp 用于存放 当前需要被替换出来的数字 直到所有的都找到正确的位置   count变量
## 代码


```
1.
void rotate(int* nums, int numsSize, int k) {
    int j = 0 ,tmp = 0;
	while (k--)
	{
		int j, tmp;
		tmp = nums[numsSize - 1];
		for (j = numsSize - 1; j > 0; j--)
		{
			nums[j] = nums[j - 1];
		}
		nums[0] = tmp;
	}
}

2.  注意自己编程的时候 使用vector时需要添加  using namespace std;
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        
        k = k %  nums.size();
        reverse(nums,0 ,nums.size()-1);
        reverse(nums,0, k-1);
        reverse(nums, k , nums.size() -1);
    }
    
    void reverse(vector<int>&  nums ,int start ,int end)
    {
        while(start <end)
        {
            
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
};

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        self.reverse(nums,0, l)
        self.reverse(nums,0,k)
        self.reverse(nums,k,l)
    def reverse(self,nums,start,end):
        i = start
        j = end-1
        while i < j:
            nums[i] , nums[j] = nums[j] ,nums[i]
            i += 1
            j -= 1



3.
public class Solution {
    public void rotate(int[] nums, int k) {
        int[] a = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            a[(i + k) % nums.length] = nums[i];
        }
        for (int i = 0; i < nums.length; i++) {
            nums[i] = a[i];
        }
    }
}

4. public class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        int count = 0;
        for (int start = 0; count < nums.length; start++) {
            int current = start;
            int prev = nums[start];
            do {
                int next = (current + k) % nums.length;
                int temp = nums[next];
                nums[next] = prev;
                prev = temp;
                current = next;
                count++;
            } while (start != current);
        }
    }
}
```


# 190  - Reverse Bits  -  Easy 

## 问题描述

颠倒给定的 32 位无符号整数的二进制位。 
## 输入输出

输入: 00000010100101000001111010011100
输出: 00111001011110000010100101000000
解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
      因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。 
## 思路

python 整数转为二进制字符串  zfill补全至长度为32  然后逆序 转整数 

## 代码

```
Python  

    def reverseBits(self, n):
        # nB = bin(n)[2:]
        # newB = '0' * (32 - len(nB)) +nB
        # reverseB =newB[::-1]
        # result = int(reverseB, 2)
        # return result
        return int(bin(n)[2:].zfill(32)[::-1],2)
        
```


***

# 198- house-robber 打家劫舍   - Easy

## 问题描述

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

## 输入输出

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
    偷窃到的最高金额 = 2 + 9 + 1 = 12 。
    

## 思路

本质:

列表中不能两两相邻元素 求其累加和的最大值 


1.   状态转移
例如ABCD四个房间 
2种情况
1. 如果窃取A 那么考虑 加上CD房间
2. 如果不窃取A  那么考虑 BCD房间

可以得到状态转移方程 

使用dp[i]表示到第i个房间时得到的最大金额数，得到状态转移方程：

dp[i]=max{dp[i-1],dp[i-2]+money[i]};


2. 使用2个变量rob和notrob表示是否抢劫当前的房子 ， prerob 和 preNotRob来记录更新之前的值 

rob表示抢了当前的房子  前一个房子不能抢 
rob = preNotRob + 当前的数字 

notRob表示不抢当前的房子  之前的房子可以抢 也可以不抢 所以将其较大的值赋给notRob。

notrob = max(preRotb , preNotRob)


*** 小结 

利用动态规划的共性:

套路:
    
    最优 最大 最小  最长  计数

离散问题：

    容易设计状态 

最优子结构：
    N-1 可以推导出N 
    
基本步骤:
    1. 设计暴力算法 找到冗余
    2. 设计并存储状态(一维 二维  三维数组 Map)
    3. 递归式子 (状态转移方程)
    4. 自底向上计算最优解 (编程方式)  

## 代码

```
1. C++

class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 0)
            return 0;
        if(nums.size() == 1)
            return nums[0];
        int i = 0;
        int *dp = new int[nums.size() + 1];
        dp[0] = nums[0];
        dp[1] = nums[0] > nums[1] ? nums[0] : nums[1];
        for(i=2; i< nums.size() ;i++)
        {
            dp[i] = max(dp[i-2]+ nums[i] , dp[i-1]);
        }
        return dp[nums.size() - 1];
    }
};


2. C++ 

class Solution {
public:
    int rob(vector<int>& nums) {
        int rob = 0, notRob = 0, n =nums.size();
        for(int i=0; i< n;i++)
        {
            int preRob = rob, preNotRob = notRob;
            rob = preNotRob + nums[i];
            notRob = max(preRob , preNotRob);
        }
        return max(rob, notRob);
    }
};

```
***



# 204 - Count Prime 计数质数 - Easy

## 问题描述

统计所有小于非负整数 n 的质数的数量。

## 输入输出
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

注意此处为小于 而不是 小于等于 


## 思路

使用bool数组进行计数  首先标记从1-n的数组元素为false

然后从i*i开始  只要是i的倍数则标记为true

最后统计所有为false的元素的个数 即为质数的个数 

注意整数的表示范围 防止上溢出

## 代码

```

class Solution {
public:
    int countPrimes(int n) {
        vector<bool> check(n+1,true); 
        check[0] = false;
        check[1] = false;
        int upper = sqrt(n) + 1;
        for(int i=2;i<=n ; i++)
        {
            if(check[i] == false)
                continue;
            if( i  >= upper)
                continue;
            int j = i*i;
            while(j <= n)
            {
                check[j] = false;
                j= j + i;
            }
        }
        int res = 0;
        for(int i = 2;i< n;i++)
        {
            if(check[i])
                res++;
        }        
        return res;
        
    }
};


```


# 206 - Reverse Linked List 反转链表 -- easy

Reverse a singly linked list. 反转单链表

Example:


Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

## 输入输出

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL


## 思路

1. 递归方法 

假定后半部分的指针已经有序  如何反转前半部分呢

 
将所有的指针顺序->  改为<-

也即 n1 n2  n2  nk  ||  nk+1  nk+2  

nk.next.next = nk;


2. 非递归的方法 迭代的方法



改变当前元素的指针指向前一个元素  需要中间变量进行保存 

找出一个元素 进行头部插入  

2. 非递归

// ListNode *nextTmp = tmp->next;用于保存下一个指针

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *finalHead =  NULL;
        ListNode * tmp = head;
        while(tmp)
        {
            
           ListNode *tmpNext = tmp->next;
           tmp->next = finalHead;
           finalHead = tmp;
           tmp = tmpNext;
        }
        
        return finalHead;
    }
};







#  217 - Contains Duplicate   - Easy

## 问题描述

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.


## 输入

Example 1:

Input: [1,2,3,1]

Example 2:

Input: [1,2,3,4]


## 输出
Output: true

Output: false

## 思路

1. list转set  元素数量减少说明存在重复的元素

2. 先排序 判断相邻两个元素相等 则说明存在重复的元素
## 代码

```
class Solution:
    def containsDuplicate(self, nums):
        if len(set(nums)) < len(nums):
            return True
        return False
```



#  234 -  Palindrome Linked List

## 问题描述
判断回文链表 -- easy

请判断一个链表是否为回文链表。

## 输入输出
示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true

## 思路

使用快慢指针 

找到中间节点  然后将后半部分逆置  
一个节点指向头结点  另一个节点执行逆置后的头结点 两两相比较



进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？




## 代码

```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
    if(head == NULL || head->next ==NULL)
        return true;
    ListNode *fast = head->next;
    ListNode *slow = head;
    while(fast!=NULL && fast->next!=NULL)
    {
        slow =  slow->next;
        fast = fast->next->next;
    }
    ListNode *secondHead = NULL;
        
    ListNode *second = slow->next;
    slow->next = NULL;
        
    while(second !=NULL)
    {
        ListNode *tmp = second->next;
        second->next = secondHead;
        secondHead = second;
        second = tmp;
    }
    
    while( secondHead !=NULL  && head->val == secondHead->val)
    {
        head = head->next;
        secondHead = secondHead->next;
    }
    
    if(secondHead == NULL)
    {
        return true;
    }else{
        return false;
    }
    
}
};
    
```




*** 

# 237 - Delete Node in a Linked List 删除链表中的一个节点 - Easy

## 问题描述

请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:




## 输入输出
输入: head = [4,5,1,9], node = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.


输入: head = [4,5,1,9], node = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.

链表至少包含两个节点。
链表中所有节点的值都是唯一的。
给定的节点为非末尾节点并且一定是链表中的一个有效节点。
不要从你的函数中返回任何结果。
## 思路

1. 最简单的链表操作  
删除元素操作  此处没有给出头指针head因此无法进行操作。

2. 替换元素值  并修改指针操作  
node节点的下一个节点的值替换当前的值  
修改下一个指针的值   
比较独特的思路   

 



## 代码

```

1. 无
tmp = head;
while(tmp->next!=node)
{
    tmp = tmp->next;
}

tmp->next = node->next;
node->next = NULL;


2.C

struct node {
    int val;
    sturct node *next
};

void deleteNode(struct node *node)
{
    node->val =node->next->val;
    node->next = node->next->next;
}
```




*** 

# 242 - Valid Anagram 有效的字母异位词   - Easy
## 问题描述

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

你可以假设字符串只包含小写字母。


## 输入

示例 1:

输入: s = "anagram", t = "nagaram"
s = "rat", t = "car"


## 输出
Output: true

Output: false

## 思路
字母异位词  说明所有的字母数量相同 只是位置不同

1. 首先判断长度 和 转为集合是否相同 不同则返回False    
然后对于s中的每个元素 在t中删除 如果删除到最后剩余为0 则说明相同 否则不同
Hash Table 先加加 后减减  判断与0的关系 


2. 统计字符 小写字母数组  两个结果是否相同


3. 排序之后判断是否相等 


```
1. py3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or set(s) != set(t):
            return False
        tList = list(t)
        for each in s:
            if each not in tList:
                return False
            tList.remove(each)
        if len(tList) == 0:
            return True
        return False
        
        
2. C统计字符
bool isAnagram(char* s, char* t) {
    int countS[26]={0}, countT[26]={0};
    int i ,j;
    for(i=0; s[i]!='\0';i++)
    {
        countS[s[i]-'a']++;
    }
    for(j=0; t[j]!='\0';j++)
    {
        countT[t[j]-'a']++;
    }
    if(i!=j)
    {
        return false;
    }
    for(i=0;i<26;i++)
    {
        if(countS[i]!=countT[i])
            return false;
    }
    return true;
}


3. C统计字符 先加后减
bool isAnagram(char* s, char* t) {
    int countS[26]={0};
    int i,j;
    for(i=0; s[i]!='\0';i++)
    {
        countS[s[i]-'a']++;
    }
    for(j=0; t[j]!='\0';j++)
    {
        countS[t[j]-'a']--;
    }
    if(i!=j)
    {
        return false;
    }
    for(i=0;i<26;i++)
    {
        if(countS[i]!=0)
            return false;
    }
    return true;
}
```

# 278 First Bad Version   - Easy Medium  Hard

## 问题描述
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。



## 输入输出
示例:

给定 n = 5，并且 version = 4 是第一个错误的版本。

调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true

所以，4 是第一个错误的版本。 

## 思路

二分查找法 

依次向中间缩减 缩小范围法 

起始值start = 1  end = n

注意特殊情况 1的时候 直接返回

## 代码

```
1. python

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1  and  isBadVersion(n):
            return n
        start = 1
        end = n
        tmp =  n / 2
        while start <=  end:
            if isBadVersion(tmp) == False:
                if isBadVersion(tmp+1) == True:
                    return (tmp+1)
                else:
                    start = tmp + 1
            elif isBadVersion(tmp) == True:
                if tmp == 1:
                    return 1
                if isBadVersion(tmp-1) == False:
                    return (tmp)
                else:
                    end = tmp - 1
            tmp = (start + end)  / 2

        return tmp


2. C++

// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1, right = n;
        while(left < right)
        {
            int mid = left + (right - left) / 2;
            if( isBadVersion(mid))
            {
                right= mid;
            }else{
                left = mid +  1;
            }
        }
        return left;
    }
};




```
***



# 283 Move Zeroes  -- Easy 

## 问题描述

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:



Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.


## 输入

Input: [0,1,0,3,12]

## 输出

Output: [1,3,12,0,0]

## 思路

遍历数组  当前元素不为0 则移动到对应的位置
tmpIndex++
当前元素为0 则记录0的个数
遍历完毕后 也完成了所有非零元素的移动 


或者不用统计0的个数  0的个数 = 总数 - 非零的个数。


或者 使用交换的方法

## 代码

```
# C++
void moveZeroes(int* nums, int numsSize) {
    int tmpNum=0,zeroCounts=0;
	for(int i=0;i<numsSize;i++)
	{
		if (nums[i] != 0)
		{
			nums[tmpNum++] = nums[i];
		}
	}
	for (int i =tmpNum; i < numsSize; i++)
	{
		nums[i] = 0;
	}
}



void moveZeroes(vector<int>& nums) {
    int lastNonZeroFoundAt = 0;
    // If the current element is not 0, then we need to
    // append it just in front of last non 0 element we found. 
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != 0) {
            nums[lastNonZeroFoundAt++] = nums[i];
        }
    }
 	// After we have finished processing new elements,
 	// all the non-zero elements are already at beginning of array.
 	// We just need to fill remaining array with 0's.
    for (int i = lastNonZeroFoundAt; i < nums.size(); i++) {
        nums[i] = 0;
    }
}


void moveZeroes(vector<int>& nums) {
    int last = 0, cur = 0;
    
    while(cur < nums.size()) {
        if(nums[cur] != 0) {
            swap(nums[last], nums[cur]);
            last++;
        }
        
        cur++;
    }
}


# py

class Solutin():
    def moveZeroes(self, nums):
        n = nums.count(0)
        l = len(nums)
        i = 0
        while 0 in nums:
            if (nums[i] == 0):
                nums.remove(nums[i])
                l = l - 1
            else:
                i = i + 1
        for j in range(n):
            nums.append(0)
        return nums



```


# 326  Power of Three 判断是否是3的幂  - Easy

## 问题描述

判断一个数 是否是3的幂


## 输入输出


Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false



## 思路

3的幂 3 9 27 81 243 每一个的约数都是 3的幂

3的幂的特点：如果一个整数N是3的幂，那么其所有约数都是3的幂。那么，换一个角度，如果n小于N且是N的约数，那么其一定是3的幂；

②、int型数据最大值为2^31-1 = 2147483647 = 0x7fffffff，则int型数据中3的最大幂如下：

int max = (int) Math.pow(3, (int) (Math.log(0x7fffffff) / Math.log(3))); ③、最后判断整数n是不是max的约数，如下即可。

max % n == 0;

小trick  找到最大值 然后判断是否n是其约数  




## 代码

```
class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n <=0)
            return false;
        if(n == 1)
            return true;
        int upper  = pow(3, int(log(0x7fffffff) / log(3)));
        if(upper % n  ==0)
            return true;
        return false;
    }
};


bool ispow3(int n)
{
	int max3 = pow(3, int(log(0x7fffffff) / log(3)));
	printf("max3 = %d\n", max3);
	printf("my max3 = %d\n", 0x7fffffff - 0x7fffffff % 3);

	if (max3 % n == 0)
	{
		cout << n << " pow 3" << endl;
		return true;
	}
	cout << n << " not pow 3" << endl;
	return false;
}

```





*** 




# 344-.Reverse String -Easy

## 问题描述
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

反转字符数组  
 
空间复杂度O(1)

## 输入



Example 1:

Input: ["h","e","l","l","o"]


## 输出
Output: ["o","l","l","e","h"]

## 思路

1. 使用python [::-1]逆序

2. 
start++  end--   依次交换
    
    
## 代码
```

1.py3 


return s[::-1]

def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s) - 1
        for i in range(n // 2 + 1):
            s[i] ,s[n-i] = s[n-i] , s[i]
        return s
    
    
2. C++

class Solution {
public:
    void reverseString(vector<char>& s) {
        int n = s.size();
        int start = 0, end = n-1;
		for(; start<end;start++ ,end--)
		{
			char tmp = s[start];
			s[start] = s[end];
			s[end] = tmp;
		}
    }
};
```
# 349-. Intersection of Two Arrays -Easy

## 问题描述
Given two arrays, write a function to compute their intersection.

求两个数组的交集




## 输入


Input: nums1 = [1,2,2,1], nums2 = [2,2]
## 输出
Output: [2]


## 思路

1. 使用python set处理  然后从元素数量较少的里面开始遍历 如果存在于第二个里面则添加

2. 
首先排序 然后使用2个索引  
如果找到相同的 则放到结果里面。

3. 直接用python的集合操作

    return list(set1 & set2)  
    
    
## 代码
```

1.py3 

class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) < len(set2):
            return self.set_intersection(set1,set2)
        else:
            return self.set_intersection(set2,set1)
        
    def set_intersection(self, set1 ,set2):
        return [x for x in set1 if x in set2]
    
    
2. 

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
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
        

3. 

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

```


[toc]

# 384 Shuffle an Array  打乱一个没有重复元素的数组。 -  Medium  

## 问题描述
// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();

## 输入输出  
```
我的输入
["Solution","shuffle","reset","shuffle"]
[[[1,2,3]],[],[],[]]
我的答案
Judging
预期答案
[null,[3,1,2],[1,2,3],[1,3,2]]
```
## 思路

洗牌方法 遍历一遍元素 随机产生一个要交换的索引 然后两个元素互换 


```
length = vec.size();
for(int i=0;i<length;i++)
{
    int pos = rand() % (length - i);
    swap(tmp[i+pos] , tmp[i]);
}

```
## 代码

```
class Solution {
    
private:
    vector<int> vec;
public:
    Solution(vector<int>& nums) {
        vec = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return vec;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        if(vec.size() == 0)
            return {};
        vector<int> tmp(vec);
        int len = vec.size();
        for(int i=0;i<len;i++)
        {
            int pos = rand() % (len - i);
            swap(tmp[i+pos] , tmp[i]);
        }
        return tmp;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */
```
***



# 387-. First Unique Character in a String   查找字符串中第一个不重复的字符串 返回索引 -Easy

## 问题描述
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

存在则返回索引 否则返回-1 



## 输入

s = "leetcode"
return 0.
## 输出
Output: [2]


## 思路
假定是字符串只有所有的小写字母  
1. 遍历元素  如果后面存在相同的则跳过当前字母  




2. 首先统计一遍所有字母出现的次数 然后从string开头  如果次数为1则返回 否则返回-1

    
    
## 代码
```

1.C++

int firstUniqChar(char* s) {
    int i=0,j=0;
    int charNums[32] = {0};
    for(i=0; s[i]!='\0';i++)
    {
        if(charNums[s[i] - 'a'] !=0 )
            continue;
        for(j=i+1;s[j] != '\0';j++)
        {
            if(s[j] == s[i])
            {
                charNums[s[i] - 'a'] =  1;
                break;
            }
        }
        if(charNums[s[i] - 'a'] == 0 )
        {
            return i;
        }
    }
    return -1;
}

2. 
class Solution {
public:
    int firstUniqChar(string s) {
        int count[26] = {0};
        
        for (int i = 0; i < s.size(); i++)
            count[s[i] - 'a']++;
        
        for (int i = 0; i < s.size(); i++)
            if (count[s[i] - 'a'] == 1)
                return i;
        
        return -1;
    }
};


3. Py3  
class Solution:
    def firstUniqChar(self, s: str) -> int:
        numsCount = [0] * 26
        for i in range(len(s)):
            numsCount[ord(s[i]) - ord('a')] += 1
        for i in range(len(s)):
            if(numsCount[ord(s[i]) - ord('a')] == 1):
                return i     
        return -1
        
    注意python2 - 3 不能直接进行字符串的相减操作  str - str 会报错


```

*** 

# 412   Fizz Buzz   - Easy 

## 问题描述
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。


## 输入输出

示例：

n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

## 思路

for遍历 if else判定

3 的倍数   

5 的倍数




## 代码

```
1. 

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> res;
        for(int i=1;i<=n;i++)
        {
            if(i%3 == 0)
            {
                if(i%5==0)
                {
                    res.push_back(string("FizzBuzz"));
                }else{
                    res.push_back(string("Fizz"));
                }
            }else{
                if(i%5 ==0)
                {
                    res.push_back(string("Buzz"));
                }else{
                     res.push_back((std::to_string(i)));
                }
            }
                
        }
        return res;
    }
};

2. 

vector<string> ss(n);
for ( int i=1;i<=n;++i ) 
	ss[i-1] = (i%15==0) ? "FizzBuzz" : (i%3==0)?"Fizz": (i%5==0)?"Buzz":to_string(i) ;
return ss;

3. py

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [ i%3/2*'Fizz'+i%5/4*'Buzz' or str(i+1) for i in range(n)]


```

*** 



# 461 - Hamming Distance  汉明距离  - Easy 

## 问题描述

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.


Note:
0 ≤ x, y < 2^31.

两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。


## 输入输出

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。



## 思路
1. 两个数异或操作 然后求其中二进制中1的个数

2. 递归操作  如果两个数完全一致 返回0   否则从最低位开始统计1的个数  右移，递归调用

## 代码

```
C++
1. 
class Solution {
public:
    int hammingDistance(int x, int y) {
        int tmp = x ^ y;
        int res = 0;
        while(tmp)
        {
            res = res + tmp % 2; 
            tmp  = tmp >> 1;
        }
        return res;
        
    }
};


2. 

class Solution {
public:
    int hammingDistance(int x, int y) {
       if( (x^y) == 0)
           return 0;
       return ((x ^ y) %2 + hammingDistance(x/2,y/2));
        
    }
};


```

补充:
求一个数二进制中1的个数 
[如何效率求二进制数中1的个数](https://blog.csdn.net/qq_37934101/article/details/80531513)

```
1. 遍历异或结果的每一位，统计为1的个数

int res = 0;
for (int i = 0; i < 32; ++i) 
{
    res += (exc >> i) & 1;

}
return res;




2. 递归方法求解 

int hammingWeight(uint32_t n) {
    if(n == 0)
        return 0;
    return n%2 + hammingWeight(n / 2) ;
}


3. 使用数组存储  

定义一个长度为255的数组，将0~255中1的个数存在数组中，需要时直接查表就行了，但存储数据需要大量内存。



4. 假如数为num, num & (num - 1)可以快速地移除最右边的bit 1， 一直循环到num为0, 总的循环数就是num中bit 1的个数


int hammingDistance(int x, int y) {
        int res = 0, exc = x ^ y;
        while (exc) {
            ++res;
            exc &= (exc - 1);
        }
        return res;
    }





```

***




# 其他

## 通过位运算实现加法

c = a ^ b;        //亦或  
b =  (a & b) << 1; //进位左移  
直至b==0 没有进位 返回c  

```
int addNumberByXorAndShift(int a, int b)
{
	if (b == 0)
		return a;
	int c = a ^ b;
	b = (a & b) << 1;
	while (b)
	{
		a = c;
		c = a ^ b;
		b = (a & b) << 1;
	}
	return c;
}

```


## 判断数字是否是2 3 4 的幂

2的幂 10000000  -1   0111111111  按位与操作 结果为0

```
if(n & (n-1) == 0)
    return true;
else 
    return false;
```


3的幂    3 9  27 81 243  每一个的约数都是 3的幂

 3的幂的特点：如果一个整数N是3的幂，那么其所有约数都是3的幂。那么，换一个角度，如果n小于N且是N的约数，那么其一定是3的幂；

②、int型数据最大值为2^31-1 = 2147483647 = 0x7fffffff，则int型数据中3的最大幂如下：

int max = (int) Math.pow(3, (int) (Math.log(0x7fffffff) / Math.log(3)));
③、最后判断整数n是不是max的约数，如下即可。

max % n == 0;

num&(num-1) 判断一个数是否为2的幂数，这个不多说。 

```
bool ispow3(int n)
{
	int max3 = pow(3, int(log(0x7fffffff) / log(3)));
	printf("max3 = %d\n", max3);
	printf("my max3 = %d\n", 0x7fffffff - 0x7fffffff % 3);

	if (max3 % n == 0)
	{
		cout << n << " pow 3" << endl;
		return true;
	}
	cout << n << " not pow 3" << endl;
	return false;
}
```


4的幂级数为1,4,16，即0001，0100,10000，也就是1出现在1,3,5,7。。。。位置上。0x55555555在32位系统里表示0b01010101010101010101010101010101。 

```

bool ispow4(int n)
{
	if( (n & (n - 1)) == 0 && (n & 0x55555555) != 0)
	{
		cout << n << " pow 4" << endl;
		return true;
	}
	cout << n << " not pow 4" << endl;
	return false;
}
```







## 交换两个整数的思路

```
1. 借助临时变量

int tmp = a;
a = b;
b = tmp;

2. 不使用临时变量
加法
a = a + b;
b = a - b;
a = a - b;

亦或操作
a = a ^ b;
b = a ^ b;
a = a ^ b;

```

## 0-1背包问题 

问题：有n个物品，第i个物品价值为vi，重量为wi，其中vi和wi均为非负数，背包的容量为W，W为非负数。现需要考虑如何选择装入背包的物品，使装入背包的物品总价值最大。该问题以形式化描述如下：

目标函数  max∑ vixi 


约束条件   max∑ wixi

求最优解

最优解的结构:

如果包含物品n  其余构成子问题 在容量为 w-wn时的最优解 

如果不包含物品n  其余构成子问题 1,2,...,xn-1在容量为W时的最优解 


  根据上述分析的最优解的结构递归地定义问题最优解。设c[i,w]表示背包容量为w时，i个物品导致的最优解的总价值，得到下式。显然要求c[n,w]。

动态规划的时间效率为O(nc)其中n表示物品的个数，c表示背包的容量。空间的效率就是用于存储二维数组的占用空间大小，即为O(nc).

```
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

/*
0-1 背包问题（迭代版）
输入：
products_count：商品的数量
capacity：背包的容量
weight_array：商品重量数组
value_array：商品价格数组
result：结果数组
*/

void knapsack(int products_count,
	int capacity,
	vector<int>& weight_array,
	vector<int>& value_array,
	vector<vector<int>>& result)
{
	int i = 1, j = 1;
	for (i = 1; i <= products_count; ++i)
	{
		for (j = 1; j <= capacity; ++j)// j代表当前背包的容量
		{
			if (weight_array[i] > j)
			{
				result[i][j] = result[i - 1][j];// 放弃第 i 件商品，拿第 i - 1 件商品
			}
			else {
				int withI = result[i - 1][j - weight_array[i]] + value_array[i];
				int withoutI = result[i - 1][j];
				result[i][j] = (withI <= withoutI ? withoutI : withI);
			}
		}
	}

}



int main()
{
	while (1)
	{
		int products_count, capacity;
		vector<int> weight_array(1, 0);
		vector<int> value_array(1, 0);
		cout << endl << "-----------------------------" << endl;
		cout << "please input products count and knapsack's capacity: " << endl; // 输入商品数量和背包容量
		cin >> products_count >> capacity;
		cout << "please input weight array for " << products_count << " products" << endl;
		for (int i = 1; i <= products_count; ++i) // 循环输入每件商品的重量
		{
			int tmp;
			cin >> tmp;
			weight_array.push_back(tmp);
		}
		cout << "please input value array for " << products_count << " products" << endl;
		for (int i = 1; i <= products_count; ++i) // 循环输入每件商品的价格
		{
			int tmp;
			cin >> tmp;
			value_array.push_back(tmp);
		}
		vector<vector<int>> result(products_count + 1, vector<int>(capacity + 1, 0)); // 结果数组
		knapsack(products_count, capacity, weight_array, value_array, result); // 调用动态规划算法

		cout << "\n Result Matrix" << endl;
		/*for (int i = 1; i <= products_count; i++)
		{
			for (int  j = 1; j <= capacity; j++)
			{
				cout << result[i][j] << " ";
			}
			cout << endl;
		}*/
		cout << "knapsack result is " << result[products_count][capacity] << endl;
	}


	return 0;
}


ref: https://blog.csdn.net/chengonghao/article/details/51915753

https://www.cnblogs.com/variance/p/6909560.html

https://www.cnblogs.com/William-xh/p/7305877.html

最清楚的01背包问题讲解: https://www.cnblogs.com/arsenalfaninecnu/p/8945548.html

#include <stdio.h>
#include <stdlib.h>

#define MAX_ROW  1000
#define MAX_COL  1000

int V[MAX_ROW][MAX_COL] = { 0 };

int getMax(int a, int b)
{
	return a <= b ? b : a;
}

int beibao(int n, int w[], int v[], int x[], int C)
{
	int i, j;
	for (i = 0; i <= n; i++)
		V[i][0] = 0;
	for (j = 0; j <= C; j++)
		V[0][j] = 0;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < C + 1; j++)
		{
			if (j < w[i])
			{
				V[i][j] = V[i - 1][j];
			}
			else {
				V[i][j] = getMax(V[i - 1][j], v[i] + V[i - 1][j - w[i]]);
			}
		}
	}
	j = C;
	for (i = n - 1; i >= 0; i--)
	{
		if (V[i][j] > V[i - 1][j])
		{
			x[i] = 1;
			j = j - w[i];
		}
		else {
			x[i] = 0;
		}
	}
	printf("选中的物品是:\n");
	for (i = 0; i<n; i++)
		printf("%d ", x[i]);

	printf("\n");
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < C + 1; j++) {
			printf("%d\t ", V[i][j]);
			if (j == C) {
				printf("\n");
			}
		}
	}
	return V[n - 1][C];

}

int main()
{
	int s;//获得的最大价值
	int w[5] = { 2,2,6,5,4 };//物品的重量
	int v[5] = { 6,3,5,4,6 };//物品的价值
	int x[5];//物品的选取状态
	int n = 5;
	int C = 10;//背包最大容量

	s = beibao(n, w, v, x, C);

	printf("最大物品价值为:\n");
	printf("%d\n", s);
	system("pause");
	system("pause");
	return 0;
}


```


# 思路总结

1. brute-force  

2. hash-table 


3. 数组运算时之前考虑排序能否加快问题解决
4. 旋转运算 分解成几个基本的步骤 





# 常用编程思想 

## 1. 动态规划

* 步骤  
1. 找出最优解的性质 并刻画其结构特征
2. 递归地定义最优解的值
3. 以自底向上的方式计算最优值
4. 根据计算最优值得到的信息，构造一个最优解。


* 适用的问题

1. 问题的最优解中包含了子问题的最优解 
2. 重叠子问题  


