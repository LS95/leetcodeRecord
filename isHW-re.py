class Test():
    def myAtoi(self,str):
        str= str.strip()
        if len(str) == 0:
            return 0
        fuhao = 1
        base = 0
        i = 0
        upMax =(pow(2,31) -1)
        lowMin = -pow(2,31)
        print "upMax = %d  lowMin=%d" % (upMax , lowMin)
        if(str[i] in '-+'):
            if str[i] == '-':
                fuhao = -1 
            else:
                fuhao = 1
            i += 1

        while(i<len(str) and (str[i]>='0' and str[i]<='9')):
            if( base > upMax // 10  or (base == upMax // 10 and (ord(str[i]) - ord('0')) > 7 ) ):
                print 'i=%d base = %d ' % (i ,base) 
                if fuhao == 1:
                    return upMax
                else:
                    return lowMin
            base = 10 * base + int(ord(str[i]) - ord('0'))
            i = i + 1

        return fuhao * base

t = Test()
print t.myAtoi("2147483648")