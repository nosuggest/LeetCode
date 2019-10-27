class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        area = 0
        for i in range(len(points)-2):
            x1,y1 = points[i][0],points[i][1]
            for j in range(i+1,len(points)-1):
                x2,y2 = points[j][0],points[j][1]
                for k in range(j+1,len(points)):
                    x3,y3 = points[k][0],points[k][1]
                    triangle = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
                    area = max(area,abs(triangle))
        return area/2