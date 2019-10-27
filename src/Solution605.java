import java.util.Arrays;

/**
 * Created by slade on 2019/6/26.
 */
public class Solution605 {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int[] tmp = new int[flowerbed.length+2];
        tmp[0] = 0;
        System.arraycopy(flowerbed,0,tmp,1,flowerbed.length);
        tmp[tmp.length-1]=0;
        int restPlace = 0;
        for (int i =0;i<tmp.length-2;){
            if (tmp[i]+tmp[i+1]+tmp[i+2]==0){
                restPlace+=1;
                i = i+2;
            }else if (tmp[i+2]==1){
                i=i+3;
            }else if (tmp[i+1]==1){
                i=i+2;
            }else if (tmp[i]==1){
                i=i+1;
            }
        }
        if (restPlace>=n){
            return true;
        }else {
            return false;
        }
    }

    public static void main(String[] args) {
        int[] f = {0,0,0,1,0};
        Solution605 s = new Solution605();
        System.out.println(s.canPlaceFlowers(f,2));
    }
}
