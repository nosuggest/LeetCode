#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 2:26 PM
# @Author  : Slade
# @File    : 1024. 视频拼接.py


class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        # 贪心算法，t标注可以截到的最长的数据
        # [0,?]下最大的？
        n = 1
        start = max(clips, key=lambda x: x[1] if x[0] == 0 else 0)[0]
        end = max(clips, key=lambda x: x[1] if x[0] == 0 else 0)[1]

        if end == 0 or start != 0:
            return -1

        while end < T:
            tmp = end
            for clip in clips:
                if clip[0] <= end:  # 必须满足能覆盖上一次的终点
                    tmp = max(clip[1], tmp)
            # 如果没有找到能覆盖上次终点且覆盖范围更大的区间则返回-1
            if tmp == end:
                return -1
            n += 1
            end = tmp
        return n

    def videoStitching1(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        超时了
        """
        clips.sort()
        if clips[0][0] > 0 or clips[-1][1] < T:
            return -1

        cnt = 0
        start = 0
        end = 0

        # 保证从第一项开始搜索
        index = -1

        while (end < T):
            while (index + 1 < len(clips) and clips[index + 1][0] <= start):
                index += 1
                end = max(end, clips[index][1])

            if index < len(clips):
                start = end
                cnt += 1
            else:
                return -1
        return cnt


if __name__ == "__main__":
    clips = [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4],
             [4, 5], [5, 7], [6, 9]]
    T = 9
    s = Solution()
    print(s.videoStitching(clips, T))
