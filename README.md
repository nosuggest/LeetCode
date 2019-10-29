# Purpose
In order to solving the interesting alogrithm problems which meeting at the interviews frequently by me and some interesting LeetCode problems.
You can click the title with blue url linking to the code, the original problems may be archived by the Coming from URL.

****

1.solved with python,folder named as **Leetcode? + details**

2.solved with java,folder named as **src/Solution? + details**

3.others solved,folder named as **random**
****

# interviews 
- [EggTopFloor](random/EggTopFloor.py)
	- **Tencent** - Machine learning Engineer
- [HuffmanEncoding](random/HuffmanEncoding.py)
	- **Didichuxing** -  Statistical Analyst
- [最大公共字符串长度](random/最大公共字符串长度.py)
	- 字节跳动
- [素数伴侣](random/素数伴侣.py)
	- **HuaWei** - Machine learning Engineer
	- ```核心在于匈牙利算法```
- [Lru_Cache](random/Lru_Cache.py)
	- **360** - Deep learning Engineer
- [消消乐](random/消消乐.py)
	- **Tencent** - Deep learning Engineer
- [花匠摆花](random/花匠摆花.py)

	- **Tencent** - Deep learning Engineer
	
Coming from:http://codeforces.com/contest/474/problem/D
- [意图相似度](random/意图相似度.py)
	- **阿里** - Algorithm Engineer
- [数组分组问题](random/数组分组问题.py)
	- **携程** - Deep learning Engineer
- [连乘质数和](random/连乘质数和.py)
	- **快手2020校招**
- [binarySearchTree](random/binarySearchTree.py)
	- 搜索二叉树
- [文本编辑距离](random/文本编辑距离.py)
- [01背包](random/01背包.py)
- [约瑟夫环问题](random/约瑟夫环问题.py)
- [按递增间隔删数，直到最后只剩下一个数](random/递增间隔删数.py)
-  [SortAlgorithm](random/SortMethod.py)
	- Almost everytime such as **Alibaba、JD、Didichuxing**...
- [GapCount](random/GapCount.py)
	- **Hp(Hewlett-Packard)** - Model Engineer
- [无序数组排序（时间复杂度为O(n)）](random/无序数组排序（时间复杂度为O(n)）.py)
	- 蚂蚁金服
- [计数排序](random/计数排序.py)
	- **阿里-推荐算法工程师**
- [插入排序](random/插入排序.py)
- [希尔排序](random/希尔排序.py)
- [归并排序](random/归并排序.py)
- [堆排序](random/堆排序.py)

***

# array

- [two-sum](LeetCode/LeetCode1two-sum.py)

Coming from :https://leetcode-cn.com/problems/two-sum/

- [container-with-most-water](LeetCode/LeetCode11container-with-most-water.py)

    - source from:https://leetcode-cn.com/problems/container-with-most-water/

- [3Sum](src/Solution15.java)
    - 左右双指针,亮点在于定义了很多提前跳出条件，在相同值跳过的条件判断中用nums[i+1]还是nums[i-1]尤为灵活

    - source from:https://leetcode-cn.com/problems/3sum/

- [3Sum Closest](src/Solution16.java)
    - 这题和上面一题很类似，只是最好不要在多生产变量了，直接拿num[first]+num[last]+num[i]去和target比，而不要考虑差值是否大于0，很容易绕进去

    - source from:https://leetcode-cn.com/problems/3sum-closest/

- [4Sum](src/Solution18.java)

    - source from:https://leetcode-cn.com/problems/4sum/

- [Remove Duplicates from Sorted Array](src/Solution26.java)

    - source from:https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

- [Remove Element](src/Solution27.java)

    - source from:https://leetcode-cn.com/problems/remove-element/

- [search-in-rotated-sorted-array](LeetCode/LeetCode33search-in-rotated-sorted-array.py)
    - 螺旋数组二分

    - source from:https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

- [find-first-and-last-position-of-element-in-sorted-array](LeetCode/LeetCode34find-first-and-last-position-of-element-in-sorted-array.py)

    - 这个考的是二分法中的while跳出条件和left、right变化逻辑，本题是找出左右边界

    - source from:https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

- [Search Insert Position](src/Solution35.java)

    - source from:https://leetcode-cn.com/problems/search-insert-position/

- [combination-sum](src/Solution39.java)

    - 这题和上面这题很像，递归在for循环里面的回溯算法，把所有情况跑一遍。`画重点，求解过程中存着result 是List<List<Integer>>的，而tmp_list是list的,需要把tmp_list再裹一层new ArrayList<>(tmp_list)再进行add`

    - source from:https://leetcode-cn.com/problems/combination-sum/

- [trapping-rain-water](LeetCode/LeetCode42trapping-rain-water.py)

    - 动态规划和栈的两种方法，很值得看一下

    - source from:https://leetcode-cn.com/problems/trapping-rain-water/

- [rotate-image](LeetCode/LeetCode48rotate-image.py)

    - source from:https://leetcode-cn.com/problems/rotate-image/

- [jump-game](LeetCode/LeetCode55jump-game.py)
    - 记录上次每次可跳的最远距离

    - source from:https://leetcode-cn.com/problems/jump-game/

- [MergeIntervals](LeetCode/LeetCode56MergeIntervals.py)

    - source from:https://leetcode-cn.com/problems/merge-intervals/

- [SpiralMatrixII](LeetCode/LeetCode59SpiralMatrixII.py)

    - `旋转矩阵题型，用了余数判断位置，比较亮点`

    - source from:https://leetcode-cn.com/problems/spiral-matrix-ii/

- [unique-paths-ii](LeetCode/LeetCode63unique-paths-ii.py)

    - source from:https://leetcode-cn.com/problems/unique-paths-ii/

- [sort-colors](LeetCode/LeetCode75sort-colors.py)

    - source from:https://leetcode-cn.com/problems/sort-colors/

- [Subsets](LeetCode/LeetCode78Subsets.py)

    - 这题利用了python的语言机制，很有意思

Coming from :https://leetcode.com/problems/subsets/

- [word-search](LeetCode/LeetCode79word-search.py)

    - source from:https://leetcode-cn.com/problems/word-search/

- [largest-rectangle-in-histogram](src/Solution84.java)

    - source from:https://leetcode-cn.com/problems/largest-rectangle-in-histogram/

- [merge-sorted-array](LeetCode/LeetCode88merge-sorted-array.py)
- [merge-sorted-array](src/Solution88.java)

    - source from:https://leetcode-cn.com/problems/merge-sorted-array/

- [majority-element](LeetCode/LeetCode169majority-element.py)

    - source from:https://leetcode-cn.com/problems/majority-element/

- [product-of-array-except-self](LeetCode/LeetCode238product-of-array-except-self.py)

    - 两侧分别扫描一遍

    - source from:https://leetcode-cn.com/problems/product-of-array-except-self/

- [move-zeroes](LeetCode/LeetCode283move-zeroes.py)

    - source from:https://leetcode-cn.com/problems/move-zeroes/

- [find-the-duplicate-number](LeetCode/LeetCode287find-the-duplicate-number.py)
    - 抽屉原理+环+快慢指针

    - source from:https://leetcode-cn.com/problems/find-the-duplicate-number/

- [find-all-duplicates-in-an-array](LeetCode/LeetCode442find-all-duplicates-in-an-array.py)

    - 和上面一样，核心是每次对abs(nums[idx])-1的处理获得nums的index很有意思

    - source from:https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/

- [find-all-numbers-disappeared-in-an-array](LeetCode/LeetCode448find-all-numbers-disappeared-in-an-array.py)

    - nums[abs(nums[idx]) - 1] = -abs(nums[abs(nums[idx]) - 1]),两个abs保证了所有存在的idx都被置负了

    - source from:https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/

- [teemo-attacking](src/Solution495.java)

    - source from:https://leetcode-cn.com/problems/teemo-attacking/

- [SubarraySumEqualsK](LeetCode/LeetCode560SubarraySumEqualsK.py)

    - source from:https://leetcode-cn.com/problems/subarray-sum-equals-k/

- [shortest-unsorted-continuous-subarray](LeetCode/LeetCode581shortest-unsorted-continuous-subarray.py)

    - source from:https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/

- [can-place-flowers](src/Solution605.java)

    - source from:https://leetcode-cn.com/problems/can-place-flowers/

- [valid-triangle-number](LeetCode/LeetCode611valid-triangle-number.py)
- [valid-triangle-number](src/Solution611.java)

    - source from:https://leetcode-cn.com/problems/valid-triangle-number/

- [task-scheduler](LeetCode/LeetCode621task-scheduler.py)

    - 理解一下，出现次数最多的那个字母（出现次数-1）x时间窗口及为最小次数，剩余要考虑的是都为最多次数的字母数

    - source from:https://leetcode-cn.com/problems/task-scheduler/

- [maximum-average-subarray-i](src/Solution643.java)

    - source from:https://leetcode-cn.com/problems/maximum-average-subarray-i/

- [largest-number-at-least-twice-of-others](src/Solution747.java)

    - source from:https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/

- [transpose-matrix](LeetCode/LeetCode867transpose-matrix.py)

    - source from:https://leetcode-cn.com/problems/transpose-matrix/

- [AdvantageShuffle](LeetCode/LeetCode870AdvantageShuffle.py)
    - 这道题的难点在于耗时，贪心算法即可，田忌赛马，可以看下

    - source from:https://leetcode-cn.com/problems/advantage-shuffle/

- [sort-array-by-parity-ii](src/Solution922.java)

    - source from:https://leetcode-cn.com/problems/sort-array-by-parity-ii/

- [squares-of-a-sorted-array](src/Solution977.java)

    - source from:https://leetcode-cn.com/problems/squares-of-a-sorted-array/

- [add-to-array-form-of-integer](src/Solution989.java)

    - source from:https://leetcode-cn.com/problems/add-to-array-form-of-integer/

- [binary-prefix-divisible-by-5](src/Solution1018.java)

    - source from:https://leetcode-cn.com/problems/binary-prefix-divisible-by-5/

- [HeightChecker](LeetCode/LeetCode1051HeightChecker.py)

    - source from:https://leetcode-cn.com/problems/height-checker/
    

***

# dynamic programming

- [longest-palindromic-substring](LeetCode/LeetCode5longest-palindromic-substring.py)

    - 中心展开，从中间值往两边展开，判断展开终止点的长度

    - source from:https://leetcode-cn.com/problems/longest-palindromic-substring/

- [maximum-subarray](LeetCode/LeetCode53maximum-subarray.py)

    - 简单递归

    - source from:https://leetcode-cn.com/problems/maximum-subarray/

- [unique-paths](LeetCode/LeetCode62unique-paths.py)

    - source from:https://leetcode-cn.com/problems/unique-paths/

- [unique-paths-ii](LeetCode/LeetCode63unique-paths-ii.py)
- [unique-paths-ii](src/Solution63.java)

    - 最优路径下的dp

    - source from:https://leetcode-cn.com/problems/unique-paths-ii/

- [minimum-path-sum](LeetCode/LeetCode64minimum-path-sum.py)

    - 非常基础简单的动态规划问题，适合理解动态规范的想法

    - source from:https://leetcode-cn.com/problems/minimum-path-sum/

- [maximal-rectangle](src/Solution85.java)

    - source from:https://leetcode-cn.com/problems/maximal-rectangle/ 

- [decode-ways](LeetCode/LeetCode91decode-ways.py)

    - 状态转移方程式dp[i] = dp[i-1]+dp[i-2],复杂在什么时候加前项什么时候加后项，什么时候加两项，0的位置的考虑

    - source from:https://leetcode-cn.com/problems/decode-ways/

- [triangle](LeetCode/LeetCode120triangle.py)

    - source from:https://leetcode-cn.com/problems/triangle/

- [best-time-to-buy-and-sell-stock](LeetCode/LeetCode121best-time-to-buy-and-sell-stock.py)
- [best-time-to-buy-and-sell-stock](src/Solution121.java)

    - source from:https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

- [best-time-to-buy-and-sell-stock-ii](LeetCode/LeetCode122best-time-to-buy-and-sell-stock-ii.py)
- [best-time-to-buy-and-sell-stock-ii](src/Solution122.java)

    - source from:https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/

- [word-break](LeetCode/LeetCode139word-break.py)

    - 第一轮用的traceback，时间复杂度是n的n次方，扑gai；然后我想了下，既然可以考虑回溯，为什么不能递归，其实只要把方程：flag[j] = flag[i]+s[i:j] in wordDict 这个想到就行，这个算是是像加限制性条件的dp，比如20届拼多多校招，多多鸡砍树问题

    - source from:https://leetcode-cn.com/problems/word-break/

- [maximum-product-subarray](LeetCode/LeetCode152maximum-product-subarray.py)

    - 需要存一个max和min，来做条件判断

    - source from:https://leetcode-cn.com/problems/maximum-product-subarray/

- [dungeon-game](LeetCode/LeetCode174dungeon-game.py)

    - 反向递归

    - source from:https://leetcode-cn.com/problems/dungeon-game/

- [house-robber](LeetCode/LeetCode198house-robber.py)

    - dp算法很经典的一道题

    - source from:https://leetcode-cn.com/problems/house-robber/

- [maximal-square](LeetCode/LeetCode221maximal-square.py)

    - source from:https://leetcode-cn.com/problems/maximal-square/

- [Ugly Number II](src/Solution264.java)

    - source from:https://leetcode-cn.com/problems/ugly-number-ii/

- [perfect-squares](src/Solution279.java)
- [perfect-squares](LeetCode/LeetCode279perfect-squares.py)


    - 双循环的dp，同样的思路python会超时，Java不会

    - source from:https://leetcode-cn.com/problems/perfect-squares/

- [longest-increasing-subsequence](LeetCode/LeetCode300longest-increasing-subsequence.py)
- [longest-increasing-subsequence](src/Solution300.java)

    - dp和递归理解的好题目，值得看

    - source from:https://leetcode-cn.com/problems/longest-increasing-subsequence/

- [range-sum-query-immutable](LeetCode/LeetCode303range-sum-query-immutable.py)

    - source from:https://leetcode-cn.com/problems/range-sum-query-immutable/

- [best-time-to-buy-and-sell-stock-with-cooldown](LeetCode/LeetCode309best-time-to-buy-and-sell-stock-with-cooldown.py)

    - dp的高难题，代码中带完整带解题方法

    - source from:https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

- [burst-balloons](LeetCode/LeetCode312burst-balloons.py)

    - dp的超高难题，代码中带完整带解题方法

    - source from:https://leetcode-cn.com/problems/burst-balloons/

- [coin-change](LeetCode/LeetCode322coin-change.py)

    - 斐波纳切动态规划

    - source from:https://leetcode-cn.com/problems/coin-change/

- [counting-bits](src/Solution338.java)

    - source from:https://leetcode-cn.com/problems/counting-bits/

- [split-array-largest-sum](LeetCode410split-array-largest-sum.py)

    - source from:https://leetcode-cn.com/problems/split-array-largest-sum/

- [partition-equal-subset-sum](LeetCode/LeetCode416partition-equal-subset-sum.py)

    - 01背包问题，这题主要考虑提前跳出条件

    - source from:https://leetcode-cn.com/problems/partition-equal-subset-sum/

- [target-sum](LeetCode/LeetCode494target-sum.py)
    - 01背包+递归逻辑
    
    - source from:https://leetcode-cn.com/problems/target-sum/

- [palindromic-substrings](LeetCode/LeetCode647palindromic-substrings.py)

    - 回文子串问题

    - source from:https://leetcode-cn.com/problems/palindromic-substrings/

- [Partition to K Equal Sum Subsets](src/Solution698.java)

    - 依旧是递归，区别在递归逻辑在for循环中，相当于并发了n条处理逻辑，有点像树展开

    - source from:https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/

- [delete-and-earn](LeetCode/LeetCode740delete-and-earn.py)

    - 核心在于bitmap+dp，与198题类似

    - source from:https://leetcode-cn.com/problems/delete-and-earn/

- [valid-permutations-for-di-sequence](LeetCode/LeetCode903valid-permutations-for-di-sequence.py)

    - 爱奇艺2020届校招

    - source from:https://leetcode-cn.com/problems/valid-permutations-for-di-sequence/

- [VideoStitching](LeetCode/LeetCode1024VideoStitching.py)

    - 贪心算法概念的比较好理解的一道题

    - source from:https://leetcode-cn.com/problems/video-stitching/

- [n-th-tribonacci-number](src/Solution1137.java)

    - 最简单的dp

    - source from:https://leetcode-cn.com/problems/n-th-tribonacci-number/