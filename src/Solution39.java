import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution39 {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        ArrayList<Integer> tmp_list = new ArrayList<>();
        Arrays.sort(candidates);
        help(candidates, target, 0, result, tmp_list);
        return result;
    }

    public void help(int[] candidates, int target, int start, List<List<Integer>> result, ArrayList<Integer> tmp_list) {
        // target小于0，匹配失败
        if (target < 0) return;

        // target==0，及目标值
        if (target == 0) {
            //result 是List<List<Integer>>的，而tmp_list是list的,需要把tmp_list再裹一层new ArrayList<>(tmp_list)
            result.add(new ArrayList<>(tmp_list));
            return;
        }

        for (int position = start; position < candidates.length; position++) {
            // 如果最小值大于剩余额度，则无解跳出即可
            if (target < candidates[position]) break;
            tmp_list.add(candidates[position]);
            // 需要注意，这边位置应该是position，而不是start，position是为了避免每次都从头开始找，实际上，只需要考虑当前位置之和的值即可
            help(candidates, target - candidates[position], position, result, tmp_list);
            tmp_list.remove(tmp_list.size() - 1);
        }

    }
}
