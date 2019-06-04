#coding=utf-8 

'''
输入是 14个数 

需要修改 输入13个数  然后依次添加 1--9 组成14个数 放入is_agari 进行判断

如果返回True 则输出最后一个数 

不存在则返回0



     print(is_agari([0,0,0,1,2,3,4,5,6,7,8,8,8,8]))  >>> True
'''

from collections import Counter


def is_agari(tehai):
    def is_agari_impl(tehai_cnt, rest_tiles):
        """
        Args:
            tehai_cnt: 各种牌的枚数信息
            rest_tiles: 剩余手牌张数
        """
        if rest_tiles == 0:
            return True
        min_tile = min(filter(lambda x: tehai_cnt[x], tehai_cnt.keys()))
        # 拆刻子
        if tehai_cnt[min_tile] >= 3:
            tehai_cnt[min_tile] -= 3
            if is_agari_impl(tehai_cnt, rest_tiles - 3):
                return True
            tehai_cnt[min_tile] += 3
        # 拆雀头
        if rest_tiles % 3 and tehai_cnt[min_tile] >= 2:
            tehai_cnt[min_tile] -= 2
            if is_agari_impl(tehai_cnt, rest_tiles - 2):
                return True
            tehai_cnt[min_tile] += 2
        # 拆顺子
        if (min_tile < 27 and min_tile % 9 < 7 
                and tehai_cnt[min_tile + 1] and tehai_cnt[min_tile + 2]):
            tehai_cnt[min_tile] -= 1
            tehai_cnt[min_tile + 1] -= 1
            tehai_cnt[min_tile + 2] -= 1
            if is_agari_impl(tehai_cnt, rest_tiles - 3):
                return True
            tehai_cnt[min_tile + 2] += 1
            tehai_cnt[min_tile + 1] += 1
            tehai_cnt[min_tile] += 1
        return False

    return is_agari_impl(Counter(tehai), len(tehai)) if len(tehai) % 3 == 2 else False

def printResult(inputList, n):
    flag = 0
    testinput =  list(inputList)
    testinput.append(n)
    testinput.sort()
    print(testinput , "\t" , testinput)
    if is_agari(testinput) == True:
        print(n," ")
        flag = 1

    if flag == 0:
        print(0)

if __name__ == "__main__":

    # print()
    # inputList = [1,1,1,1,2,2,3,3,5,6,7,8,9] # input
    # for i in range(1,10):
    #     printResult(inputList, i)
        
    print(is_agari([0,0,0,1,2,3,4,5,6,7,8,8,8,8]))