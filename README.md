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

### [文本编辑距离](random/文本编辑距离.py)

### [01背包](random/01背包.py)

### [约瑟夫环问题](random/约瑟夫环问题.py)

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
