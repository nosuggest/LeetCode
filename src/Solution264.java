import java.util.ArrayList;

public class Solution264 {
    public int nthUglyNumber(int n) {
        n = n-1;
        ArrayList<Integer> init_ans = new ArrayList<>();
        init_ans.add(1);
        int i2 = 0;
        int i3 = 0;
        int i5 = 0;
        for (int i =0;i<=n;i++){
            int last_2 =  init_ans.get(i2) * 2;
            int last_3 = init_ans.get(i3)*3;
            int last_5 = init_ans.get(i5)*5;
            int minval = Math.min(last_2,Math.min(last_3,last_5));
            init_ans.add(minval);
            if(minval==last_2){
                i2= i2+1;
            }
            if (minval==last_3){
                i3 = i3+1;
            }
            if (minval==last_5){
                i5 = i5+1;
            }
        }
        System.out.println(init_ans);
        return init_ans.get(n);
    }

    public static void main(String[] args) {
        Solution264 s = new Solution264();
        System.out.println(s.nthUglyNumber(10));
    }
}
