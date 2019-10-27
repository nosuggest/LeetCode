import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution17 {
    public List<String> letterCombinations(String digits) {
    if (digits==null||digits.length()==0){
        return new ArrayList<>();}
    Map<Character,String> map = new HashMap<>();
    map.put('2', "abc");
    map.put('3', "def");
    map.put('4', "ghi");
    map.put('5', "jkl");
    map.put('6', "mno");
    map.put('7', "pqrs");
    map.put('8', "tuv");
    map.put('9', "wxyz");
    List res = new ArrayList<>();
    getCombinations("",digits,0,res,map);
    return res;
    }
    void getCombinations(String str,String digits,int position,List<String> res,Map<Character,String> map){
        if (digits.length()==position){
            res.add(str);
            return;
        }

        String letters = map.get(digits.charAt(position));

        for (int j = 0;j<letters.length();j++){
            //char和char不能直接相加，char+string可以，char+char返回的是int，ASCII对应整数
            getCombinations(str+letters.charAt(j),digits,position+1,res,map);
        }

    }
    public static void main(String[] args) {
        Solution17 s = new Solution17();
        System.out.println(s.letterCombinations("23"));


    }
}
