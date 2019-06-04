class Test():
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            result = "1"
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
t = Test()
print t.countAndSay(6)