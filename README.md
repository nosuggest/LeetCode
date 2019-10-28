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

**Tencent** - Machine learning Engineer
- [HuffmanEncoding](random/HuffmanEncoding.py)

**Didichuxing** -  Statistical Analyst
-  [SortAlgorithm](random/SortMethod.py)

Almost everytime such as **Alibaba、JD、Didichuxing**...
- [GapCount](random/GapCount.py)

**Hp(Hewlett-Packard)** - Model Engineer
- [无序数组排序（时间复杂度为O(n)）](random/无序数组排序（时间复杂度为O(n)）.py)

```
问题：给你n个无序的int整型数组arr，并且这些整数的取值范围都在0-20之间，要你在 O(n) 的时间复杂度中把这 n 个数按照从小到大的顺序打印出来。
```
- [最大公共字符串长度](random/最大公共字符串长度.py)

`有两个字符串，你只可以进行删除操作，问你最少进行多少次操作可以使两个字符串相等`

Coming from:`字节跳动面试题`

- [素数伴侣](random/素数伴侣.py)

**HuaWei** - Machine learning Engineer

```核心在于匈牙利算法```

>题目描述:
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。现在密码学会请你设计一个程序，从已有的N（N为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，而将2和5、6和13编组将得到两组“素数伴侣”，能组成“素数伴侣”最多的方案称为“最佳方案”，当然密码学会希望你寻找出“最佳方案”。

- [Lru_Cache](random/Lru_Cache.py)

**360** - Deep learning Engineer

```Lru_Cache实现```

- [消消乐](random/消消乐.py)

**Tencent** - Deep learning Engineer

>有n个数字，每次可以选择任意两个不同的数字，并同时删除它们，请问最后是否可以删完

```
两个坑：
1.汇总每个数字出现的次数的时候，不要用.count()，会超时；遍历hashmap
2.汇总后的数组中的每个数字是可拆的，并不是把一个数组切分成n个和相等的子数组，只需要max_value<=sum/2即可
```

- [花匠摆花](random/花匠摆花.py)

**Tencent** - Deep learning Engineer

```
原题参考代码注释
```
```
两个坑：
1.用traceback的就直接gg，比如我
2.dp[i]为当前的长度为i的可摆放个数，dp[i] = dp[i-1]+dp[i-k]为状态转移矩阵，更多解释看代码注释
```

Coming from:http://codeforces.com/contest/474/problem/D

- [意图相似度](random/意图相似度.py)

**阿里** - Algorithm Engineer

>找出相似意图（编辑距离<阈值）的pair，且每一个意图要满足一定长要求条件`[minSeqLen,maxSeqLen]`，一个子序列可能存在多个重复的，比如如下就是满足长度`[5,8]`(编辑距离为1，小于阈值等于2)子意图序列pair：
```
>A:weather,joker,music,stock,joker,joker,news
>B:weather,joker,music,stock,joker,joker,texi
输入：
第一行：阈值
第二行：最小序列长度
第三行：最多序列长度
第四行：A用户的意图序列
第五行：B用户的意图序列
```

- [数组分组问题](random/数组分组问题.py)

**携程** - Deep learning Engineer

>给定一个时刻表，根据目的地进行分组，同一个目的地必须尽可能的多分，不能打乱顺序，比如aabbcddc，需要分成aa|bb|cddc,而不能分成aabb|cddc，因为这种情况下不是最多，也不能分成aa|bb|c|dd|c,因为相同的c没有被分在一起；求分组个数；

用了两种方法解，数组区间合并和动态规划

- [连乘质数和](random/连乘质数和.py)

**快手2020校招**

>给定一个(1,N]之间的正整数，需要统计质数分解之后的质数的个数；
>举例:N=6,(1,6]之间包括2,3,4,5,6,2=2,3=3,4=2*2,5=5,6=2*3,所以对应质数和位1+1+2+1+2=7

```我做的是最简单的实现，回溯求解```

- [binarySearchTree](random/binarySearchTree.py)

`搜索二叉树`

- [文本编辑距离](random/文本编辑距离.py)

- [01背包](random/01背包.py)

- [约瑟夫环问题](random/约瑟夫环问题.py)

约瑟夫环问题：一圈共有N个人，开始报数，报到M的人自杀，然后重新开始报数，问最后自杀的人是谁？
问题重述：N个人（编号0~(N-1))，从0开始报数，报到(M-1)的自杀，剩下的人继续从0开始报数。求最后自杀者的编号。

- [按递增间隔删数，直到最后只剩下一个数](random/递增间隔删数.py)

有数组A，每个元素存放相应的下标,即A[i]=i，要求按照1,2,3,...的规律删除数组中的元素,第一次间隔1个数，第二次间隔2个数,依次类推，到末尾时循环至开头继续进行,求最后一个被删掉的数的原始下标位置

以上两条都是属于环问题，更多讲解来自：[约瑟夫环问题整理](http://www.shataowei.com/2019/10/20/约瑟夫环问题整理/)

- [计数排序](random/计数排序.py)

**阿里-推荐算法工程师**

- [插入排序](random/插入排序.py)

- [希尔排序](random/希尔排序.py)

- [归并排序](random/归并排序.py)

- [堆排序](random/堆排序.py)

***

# array

- [two-sum](LeetCode/LeetCode1two-sum.py)

Coming from :https://leetcode-cn.com/problems/two-sum/

- [container-with-most-water](LeetCode/LeetCode11container-with-most-water.py)

Coming from:https://leetcode-cn.com/problems/container-with-most-water/

- [3Sum](src/Solution15.java)
`左右双指针,亮点在于定义了很多提前跳出条件，在相同值跳过的条件判断中用nums[i+1]还是nums[i-1]尤为灵活`

Coming from:https://leetcode-cn.com/problems/3sum/

- [3Sum Closest](src/Solution16.java)
`这题和上面一题很类似，只是最好不要在多生产变量了，直接拿num[first]+num[last]+num[i]去和target比，而不要考虑差值是否大于0，很容易绕进去`

Coming from:https://leetcode-cn.com/problems/3sum-closest/

- [4Sum](src/Solution18.java)

Coming from:https://leetcode-cn.com/problems/4sum/

- [Remove Duplicates from Sorted Array](src/Solution26.java)

Coming from:https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

- [Remove Element](src/Solution27.java)

Coming from:https://leetcode-cn.com/problems/remove-element/

- [search-in-rotated-sorted-array](LeetCode/LeetCode33search-in-rotated-sorted-array.py)

```
因为是螺旋数组，所以理解2点：
1、对于mid = （left+right）>>1来说，要么左侧要么右侧，必然会有一边是有序的
2、判断target在有序侧还是非有序侧，从而决定是修正有序侧还是简单位移
```

ps:二分用的是index:`while end<=right`

Coming from:https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

- [find-first-and-last-position-of-element-in-sorted-array](LeetCode/LeetCode34find-first-and-last-position-of-element-in-sorted-array.py)

这个考的是二分法中的while跳出条件和left、right变化逻辑，本题是找出左右边界

Coming from:https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

- [Search Insert Position](src/Solution35.java)

Coming from:https://leetcode-cn.com/problems/search-insert-position/

- [combination-sum](src/Solution39.java)
`这题和上面这题很像，递归在for循环里面的回溯算法，把所有情况跑一遍`

`画重点，求解过程中存着result 是List<List<Integer>>的，而tmp_list是list的,需要把tmp_list再裹一层new ArrayList<>(tmp_list)再进行add`

Coming from:https://leetcode-cn.com/problems/combination-sum/

- [trapping-rain-water](LeetCode/LeetCode42trapping-rain-water.py)

动态规划和栈的两种方法，很值得看一下

Coming from:https://leetcode-cn.com/problems/trapping-rain-water/

- [rotate-image](LeetCode/LeetCode48rotate-image.py)

Coming from:https://leetcode-cn.com/problems/rotate-image/

- [jump-game](LeetCode/LeetCode55jump-game.py)

```python
max_dis：上次每次可跳的最远距离
本次是在range中产生的，所以需要减去1，剩下的才是还可供跳跃的长度

nums[idx]：是本次新可跳的距离

比较max_ids-1和nums[idx]得出当前可跳的新最远距离
如果max_ids==0代表可跳的距离额度没有了，return False
```

这题和[distribute-coins-in-binary-tree](LeetCode/LeetCode979distribute-coins-in-binary-tree.py)神似。

Coming from:https://leetcode-cn.com/problems/jump-game/

- [MergeIntervals](LeetCode/LeetCode56MergeIntervals.py)

Coming from:https://leetcode-cn.com/problems/merge-intervals/

- [SpiralMatrixII](LeetCode/LeetCode59SpiralMatrixII.py)
`旋转矩阵题型，用了余数判断位置，比较亮点`

Coming from:https://leetcode-cn.com/problems/spiral-matrix-ii/


Coming from:https://leetcode-cn.com/problems/unique-paths-ii/



- [sort-colors](LeetCode/LeetCode75sort-colors.py)

Coming from:https://leetcode-cn.com/problems/sort-colors/

- [Subsets](LeetCode/LeetCode78Subsets.py)

`这题利用了python的语言机制，很有意思`

Coming from :https://leetcode.com/problems/subsets/

- [word-search](LeetCode/LeetCode79word-search.py)

Coming from:https://leetcode-cn.com/problems/word-search/

- [largest-rectangle-in-histogram](src/Solution84.java)

Coming from:https://leetcode-cn.com/problems/largest-rectangle-in-histogram/

- [merge-sorted-array](LeetCode/LeetCode88merge-sorted-array.py)
- [merge-sorted-array](src/Solution88.java)

Coming from:https://leetcode-cn.com/problems/merge-sorted-array/

- [majority-element](LeetCode/LeetCode169majority-element.py)

Coming from:https://leetcode-cn.com/problems/majority-element/

- [product-of-array-except-self](LeetCode/LeetCode238product-of-array-except-self.py)

`两侧分别扫描一遍`

Coming from:https://leetcode-cn.com/problems/product-of-array-except-self/

- [move-zeroes](LeetCode/LeetCode283move-zeroes.py)

Coming from:https://leetcode-cn.com/problems/move-zeroes/

- [find-the-duplicate-number](LeetCode/LeetCode287find-the-duplicate-number.py)

```
（1）使用哈希表判重
（2）排序以后，重复的数相邻
（3）使用“抽屉原理”，当两个数发现要放在同一个地方的时候，就发现了这个重复的元素
（4）既然要定位数，可以对“数”做二分
（5）还可以使用“快慢指针”来完成
```

环概念：代码内部，好好看

Coming from:https://leetcode-cn.com/problems/find-the-duplicate-number/

- [find-all-duplicates-in-an-array](LeetCode/LeetCode442find-all-duplicates-in-an-array.py)
```和上面一样，核心是每次对abs(nums[idx])-1的处理获得nums的index很有意思```

Coming from:https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/

- [find-all-numbers-disappeared-in-an-array](LeetCode/LeetCode448find-all-numbers-disappeared-in-an-array.py)
```nums[abs(nums[idx]) - 1] = -abs(nums[abs(nums[idx]) - 1]),两个abs保证了所有存在的idx都被置负了```

Coming from:https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/

- [teemo-attacking](src/Solution495.java)

Coming from:https://leetcode-cn.com/problems/teemo-attacking/

- [SubarraySumEqualsK](LeetCode/LeetCode560SubarraySumEqualsK.py)

Coming from:https://leetcode-cn.com/problems/subarray-sum-equals-k/

- [shortest-unsorted-continuous-subarray](LeetCode/LeetCode581shortest-unsorted-continuous-subarray.py)

Coming from:https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/

- [can-place-flowers](src/Solution605.java)

Coming from:https://leetcode-cn.com/problems/can-place-flowers/

- [valid-triangle-number](LeetCode/LeetCode611valid-triangle-number.py)
- [valid-triangle-number](src/Solution611.java)

Coming from:https://leetcode-cn.com/problems/valid-triangle-number/

- [task-scheduler](LeetCode/LeetCode621task-scheduler.py)

理解一下，出现次数最多的那个字母（出现次数-1）x时间窗口及为最小次数，剩余要考虑的是都为最多次数的字母数

Coming from:https://leetcode-cn.com/problems/task-scheduler/

- [maximum-average-subarray-i](src/Solution643.java)

Coming from:https://leetcode-cn.com/problems/maximum-average-subarray-i/

- [largest-number-at-least-twice-of-others](src/Solution747.java)

Coming from:https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/

- [transpose-matrix](LeetCode/LeetCode867transpose-matrix.py)

Coming from:https://leetcode-cn.com/problems/transpose-matrix/

- [AdvantageShuffle](LeetCode/LeetCode870AdvantageShuffle.py)
`这道题的难点在于耗时，贪心算法即可，田忌赛马，可以看下`

Coming from:https://leetcode-cn.com/problems/advantage-shuffle/

- [sort-array-by-parity-ii](src/Solution922.java)

Coming from:https://leetcode-cn.com/problems/sort-array-by-parity-ii/

- [squares-of-a-sorted-array](src/Solution977.java)

Coming from:https://leetcode-cn.com/problems/squares-of-a-sorted-array/

- [add-to-array-form-of-integer](src/Solution989.java)

Coming from:https://leetcode-cn.com/problems/add-to-array-form-of-integer/

- [binary-prefix-divisible-by-5](src/Solution1018.java)

Coming from:https://leetcode-cn.com/problems/binary-prefix-divisible-by-5/

- [HeightChecker](LeetCode/LeetCode1051HeightChecker.py)

Coming from:https://leetcode-cn.com/problems/height-checker/

***

# dynamic programming

- [longest-palindromic-substring](LeetCode/LeetCode5longest-palindromic-substring.py)

>中心展开，从中间值往两边展开，判断展开终止点的长度

Coming from:https://leetcode-cn.com/problems/longest-palindromic-substring/

- [maximum-subarray](LeetCode/LeetCode53maximum-subarray.py)

```简单递归```

Coming from:https://leetcode-cn.com/problems/maximum-subarray/

- [unique-paths](LeetCode/LeetCode62unique-paths.py)

Coming from:https://leetcode-cn.com/problems/unique-paths/

- [unique-paths-ii](LeetCode/LeetCode63unique-paths-ii.py)
- [unique-paths-ii](src/Solution63.java)
```最优路径下的dp```

- [minimum-path-sum](LeetCode/LeetCode64minimum-path-sum.py)
`非常基础简单的动态规划问题，适合理解动态规范的想法`

Coming from:https://leetcode-cn.com/problems/minimum-path-sum/

- [maximal-rectangle](src/Solution85.java)

Coming from:https://leetcode-cn.com/problems/maximal-rectangle/ 

- [decode-ways](LeetCode/LeetCode91decode-ways.py)
```状态转移方程式dp[i] = dp[i-1]+dp[i-2],复杂在什么时候加前项什么时候加后项，什么时候加两项，0的位置的考虑```

Coming from:https://leetcode-cn.com/problems/decode-ways/

- [triangle](LeetCode/LeetCode120triangle.py)

Coming from:https://leetcode-cn.com/problems/triangle/

- [best-time-to-buy-and-sell-stock](LeetCode/LeetCode121best-time-to-buy-and-sell-stock.py)
- [best-time-to-buy-and-sell-stock](src/Solution121.java)

Coming from:https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

- [word-break](LeetCode/LeetCode139word-break.py)

>第一轮用的traceback，时间复杂度是n的n次方，扑gai；然后我想了下，既然可以考虑回溯，为什么不能递归，其实只要把方程：flag[j] = flag[i]+s[i:j] in wordDict 这个想到就行，这个算是是像加限制性条件的dp，比如20届拼多多校招，多多鸡砍树问题

Coming from:https://leetcode-cn.com/problems/word-break/

- [maximum-product-subarray](LeetCode/LeetCode152maximum-product-subarray.py)

```需要存一个max和min，来做条件判断```

Coming from:https://leetcode-cn.com/problems/maximum-product-subarray/

- [dungeon-game](LeetCode/LeetCode174dungeon-game.py)

```反向递归```

Coming from:https://leetcode-cn.com/problems/dungeon-game/

- [house-robber](LeetCode/LeetCode198house-robber.py)
`dp算法很经典的一道题`

Coming from:https://leetcode-cn.com/problems/house-robber/

- [maximal-square](LeetCode/LeetCode221maximal-square.py)

Coming from:https://leetcode-cn.com/problems/maximal-square/

- [Ugly Number II](src/Solution264.java)

Coming from:https://leetcode-cn.com/problems/ugly-number-ii/

- [perfect-squares](src/Solution279.java)
- [perfect-squares](LeetCode/LeetCode279perfect-squares.py)


```双循环的dp，同样的思路python会超时，Java不会```

Coming from:https://leetcode-cn.com/problems/perfect-squares/

- [longest-increasing-subsequence](LeetCode/LeetCode300longest-increasing-subsequence.py)
- [longest-increasing-subsequence](src/Solution300.java)
```
dp和递归理解的好题目，值得看
```
Coming from:https://leetcode-cn.com/problems/longest-increasing-subsequence/

- [range-sum-query-immutable](LeetCode/LeetCode303range-sum-query-immutable.py)

Coming from:https://leetcode-cn.com/problems/range-sum-query-immutable/

- [best-time-to-buy-and-sell-stock-with-cooldown](LeetCode/LeetCode309best-time-to-buy-and-sell-stock-with-cooldown.py)

`dp的高难题，代码中带完整带解题方法`

Coming from:https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

- [burst-balloons](LeetCode/LeetCode312burst-balloons.py)

`dp的超高难题，代码中带完整带解题方法`

Coming from:https://leetcode-cn.com/problems/burst-balloons/

- [coin-change](LeetCode/LeetCode322coin-change.py)

斐波纳切动态规划

Coming from:https://leetcode-cn.com/problems/coin-change/

- [counting-bits](src/Solution338.java)

Coming from:https://leetcode-cn.com/problems/counting-bits/

- [split-array-largest-sum](LeetCode410split-array-largest-sum.py)

Coming from:https://leetcode-cn.com/problems/split-array-largest-sum/

- [partition-equal-subset-sum](LeetCode/LeetCode416partition-equal-subset-sum.py)

`01背包问题，这题主要考虑提前跳出条件`

Coming from:https://leetcode-cn.com/problems/partition-equal-subset-sum/

- [target-sum](LeetCode/LeetCode494target-sum.py)

```这题有点难，01背包+递归逻辑，值得面试前看一波```

```
难点1：把原问题转换为算背包容积的问题，因为p-n=t,p-n+p+n=sum+t,p=(sum+t)/2
难点2：dp[i]=dp[i]+dp[i-num]
```

Coming from:https://leetcode-cn.com/problems/target-sum/

- [palindromic-substrings](LeetCode/LeetCode647palindromic-substrings.py)

```回文子串问题```

```
方法1：dp
方法2：中间搜索
```

Coming from:https://leetcode-cn.com/problems/palindromic-substrings/

- [Partition to K Equal Sum Subsets](src/Solution698.java)
`依旧是递归，区别在递归逻辑在for循环中，相当于并发了n条处理逻辑，有点像树展开`

Coming from:https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/

- [delete-and-earn](LeetCode/LeetCode740delete-and-earn.py)
`核心在于bitmap+dp，与198题类似`

Coming from:https://leetcode-cn.com/problems/delete-and-earn/

- [valid-permutations-for-di-sequence](LeetCode/LeetCode903valid-permutations-for-di-sequence.py)

`爱奇艺2020届校招`

>这边需要明白一个规则，举个例子：S:[0,1,2,3],P:[DID];dp[i,j]中i指S中的最大范围，此处i最大=3，j为以什么为结尾
dp[2.1]则为S:[0,1,2],且以1为结尾，因为p为DID，所以当i=2的时候，应该满足DI，1为结尾，又因为I为此时P的结尾，所以
[0,1]的前两位组合的末尾应该是比二小就行，所以d[1,1]和dp[1,0]都行，dp[2,2] = dp[1,0]+dp[1,1]=1+0；如果是ID的情况
同上，所以状态转移方程应该是：
if S[i-1] == "D":dp[i,j] += dp[i-1,k] j<=k<=i-1
if S[i-1] == "I":dp[i,j] += dp[i-1,k] k<j

Coming from:https://leetcode-cn.com/problems/valid-permutations-for-di-sequence/

- [VideoStitching](LeetCode/LeetCode1024VideoStitching.py)
`贪心算法概念的比较好理解的一道题`

Coming from:https://leetcode-cn.com/problems/video-stitching/

*** 