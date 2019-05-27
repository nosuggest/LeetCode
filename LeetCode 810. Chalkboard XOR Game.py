class Solution(object):
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import functools
        if not functools.reduce(lambda x,y:x^y,nums):
            return True
        length = len(nums)
        if length%2:
            '''
            奇数的情况下，只有num^num|0^num=0，偶数对后+单次操作!=0,则无论小红怎么选，小明都可以找到最优解，必然会有一个落单的操作由小红完成
            
            小红，只有在偶数个相同，^下为0，一个不同，每次取偶数对中的一个才有可能赢，但是小明的同样的偶数操作会使得小红拿最后一个，小红必输
            
            '''
            return False
        else:
            '''
            同样，如果nums为偶数，依旧为num^num|0^num=0，偶数对后，num1*num2!=0,小红的每次操作只要满足实现num1*num2!=0，因为倒数第二次拿走num1或者num2之后，小明的num1/num2的^结果只能还是原值，小红必胜
            
            总结的来说，要想结束游戏，此时必定是n个数字相同，而一个数字不同的局面，所以只要考虑n+1的奇偶性
            '''
            return True