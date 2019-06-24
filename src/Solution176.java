/**
 * Created by slade on 2019/6/24.
 */
public class Solution176 {
    public int singleNumber(int[] nums) {
        int a = 0;
        int b = 0;
        for (int num:nums
             ) {
            a = (a^num)&~b;
            b = (b^num)&~a;
        }
        return a;
    }
}
/*
* 第一轮，a^num会将a赋值为num且b为0，所以a被存储为num
* 第一轮，b^num会将b赋值为num且b为num，但是a已经是num了，所以b又被重新置为0
* 第二轮，a^num会将a赋值为num且b为0，所以a被存储为0
* 第二轮，b^num会将b赋值为num且b为num，但是a已经是非num了，所以b又被存储为num
* 第三轮，a^num会将a赋值为num且b为num，但是b也是num，b&～b=0，所以a被存储为0
* 第三轮，b^num会将b赋值为0，所以b又被存储为0
* 一轮迭代完成
* */