class Test():
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

t = Test()
print t.strStr("hello","ll")