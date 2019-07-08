import java.util.Stack;

/**
 * Created by slade on 2019/7/8.
 */
public class Solution84 {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        int heightsLen = heights.length;
        int area = 0;
        for (int i = 0; i < heightsLen; i++) {
            while (stack.peek() != -1 && heights[stack.peek()] >= heights[i]) {
                int curIdx = stack.pop();
                area = Math.max(area, heights[curIdx] * (i - stack.peek() - 1));
            }
            stack.push(i);
        }

        while (stack.peek() != -1) {
            int curIdx = stack.pop();
            area = Math.max(area, heights[curIdx] * (heightsLen - stack.peek() - 1));
        }

        return area;
    }
}
