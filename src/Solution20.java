import com.sun.org.apache.bcel.internal.generic.IF_ACMPEQ;

import java.util.*;

public class Solution20 {
    public boolean isValid(String s) {
        boolean tag=true;
        HashMap<String,String> deafult_map = new HashMap<>();

        deafult_map.put("}","{");
        deafult_map.put("]","[");
        deafult_map.put(")","(");

        String[] right_list = {"}","]",")"};
        List<String> right_list_array = Arrays.asList(right_list);

        String[] left_list = {"{","[","("};
        List<String> left_list_array = Arrays.asList(left_list);

        LinkedList<String> ans = new LinkedList<String>();

        int length = s.length();

        //如果是奇数个必然不满足条件
        if (length%2==1){
            tag = false;
            return tag;
        }

        //如果是空则满足条件
        if (length==0){
            return tag;
        }

        //如果起始位不满足条件则为空
        if (right_list_array.contains(String.valueOf(s.charAt(0)))){
            tag = false;
            return tag;
        }

        //初始化加载第一个字符到待消除链表
        ans.addFirst(String.valueOf(s.charAt(0)));
        for (int i =1;i<length;i++){
            //目标字符
            String chari = String.valueOf(s.charAt(i));
            //拿出最近的一个字符进行匹配
            String charl = ans.getFirst();
            //如果最近的一个字符等于目标字符则进行下一个，如果目标字符为left_list_array，则加入待审链表
            if (left_list_array.contains(chari)){
                ans.addFirst(String.valueOf(s.charAt(i)));
            }else if (charl.equals(deafult_map.get(chari))){
                ans.pop();
                // 如果待审链表为空则检查是否遍历了整个字符串，未遍历则继续循环
                if (ans.isEmpty()){
                    if (i == length-1){
                        return tag;
                    }
                    String charn = String.valueOf(s.charAt(i+1));
                    ans.addFirst(charn);
                    i= i+1;
                }
                continue;
            }else {tag = false;break;}
        }

        //检查ans里面的待审核元素是否还有剩余
        if (!ans.isEmpty()){tag = false;}

        return tag;
    }

    public static void main(String[] args) {
        Solution20 s = new Solution20();
        System.out.println(s.isValid("{{"));
    }
}
