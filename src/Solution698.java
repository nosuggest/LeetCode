import java.util.*;

public class Solution698 {
    public boolean canPartitionKSubsets(int[] nums, int k) {

        int sum=0;
        boolean label = false;

        int len = nums.length;
        //当前元素是否被使用过
        boolean[] mark = new boolean[len];

        //判断是否存在可能
        for (int i = 0; i <len ; i++) {
            sum = sum +nums[i];
        }
        // 每个组内的目标和的值
        int target = sum/k;
        int tag = sum%k;
        if (tag!=0){
            return false;
        }
        //是否存在大于目标值得情况
        LinkedList<Integer> numsList = new LinkedList<Integer>();
        for(int i:nums){
            if (i>target){
                label = true;
                break;
            }
            numsList.add(i);
        }

        if (label){
            return false;
        }else {
            return help(numsList,mark,k, 0,target,0);

        }

    }
    boolean  help(LinkedList<Integer> numsList,boolean[] mark,int k,int start,int target,int curSum){
        //配对完成
        if (k==1) return true;
        //进行下一组配对，重置初始位置，重置初始和
        if (curSum==target) return help(numsList,mark,k-1,0,target,0);
        //for循环为了遍历所有节点，找到所有子集
        for (int i = start;i<numsList.size();i++){
            if (mark[i]) continue;
            //标记已经使用过的元素
            mark[i]=true;
            //递归寻找满足curSum==target条件的元素组合
            if (help(numsList,mark,k,i+1,target,numsList.get(i)+curSum)) return true;
            mark[i] = false;
        }
        return false;
    }
    public static void main(String[] args) {
        Solution698 s = new Solution698();
        int[] a = {2,2,10,5,2,7,2,2,13};
        System.out.println(s.canPartitionKSubsets(a,3));
    }
}
