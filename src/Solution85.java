import java.util.Arrays;
import java.util.Stack;

/**
 * Created by slade on 2019/7/9.
 */
public class Solution85 {
    public int maximalRectangle(char[][] matrix) {
        int matrixHeight = matrix.length;
        if (matrixHeight == 0) {
            return 0;
        }
        int matrixWide = matrix[0].length;
        int ans = 0;
        int[] lastValue = new int[matrixWide];
        Arrays.fill(lastValue, 0);
        for (int i = 0; i < matrixHeight; i++) {
            int[] tmp = new int[matrixWide];
            for (int j = 0; j < matrixWide; j++) {
                if (matrix[i][j] != '0') {
                    tmp[j] = lastValue[j] + 1;
                    lastValue[j] = lastValue[j] + 1;
                } else {
                    tmp[j] = 0;
                    lastValue[j] = 0;
                }
            }
            ans = Math.max(largestRectangleArea(tmp), ans);
        }
        return ans;
    }


    public int largestRectangleArea(int[] heights) {
        int heightsLen = heights.length;
        Stack<Integer> stack = new Stack<>();
        stack.add(-1);
        int area = 0;

        for (int i = 0; i < heightsLen; i++) {
            while (stack.peek() != -1 && heights[stack.peek()] >= heights[i]) {
                int tmpIdx = stack.pop();
                int tmpVal = stack.isEmpty() ? -1 : stack.peek();
                area = Math.max(area, heights[tmpIdx] * (i - tmpVal - 1));
            }
            stack.push(i);
        }

        while (stack.peek() != -1) {
            int tmpIdx = stack.pop();
            int tmpVal = stack.isEmpty() ? -1 : stack.peek();
            area = Math.max(area, heights[tmpIdx] * (heightsLen - tmpVal - 1));
        }
        return area;
    }

    public static void main(String[] args) {
        Solution85 s = new Solution85();
        char[][] charArray = {{'0', '0', '1'}, {'0', '0', '1'}, {'1', '1', '1'}, {'1', '1', '1'}, {'1', '0', '1'}};
        System.out.println(s.maximalRectangle(charArray));
    }
}
