import java.util.*;

class Solution13 {
    public int romanToInt(String s) {
        int amount = 0;
        Map hashMap = new HashMap();
        hashMap.put("I", 1);
        hashMap.put("V", 5);
        hashMap.put("X", 10);
        hashMap.put("L", 50);
        hashMap.put("C", 100);
        hashMap.put("D", 500);
        hashMap.put("M", 1000);
        hashMap.put("IV", 4);
        hashMap.put("IX", 9);
        hashMap.put("XL", 40);
        hashMap.put("XC", 90);
        hashMap.put("CD", 400);
        hashMap.put("CM", 900);


        String[] S = {"IX", "IV", "XL", "XC", "CD", "CM"};
        List<String> first_search = Arrays.asList(S);

        int add = 1;
        for (int i = 0; i < s.length(); i = i + add) {
            String two_letters = "";
            if (i < s.length() - 1) {

                two_letters = s.substring(i, i + 2);
            }
            String one_letter = s.substring(i, i + 1);
            if (first_search.contains(two_letters)) {
                int val = (int) hashMap.get(two_letters);
                amount = amount + val;
                add = 2;
            } else {
                int val1 = (int) hashMap.get(one_letter);
                amount = amount + val1;
                add = 1;
            }
        }

        return amount;
    }

    public static void main(String[] args) {
        Solution13 s = new Solution13();
        System.out.println(s.romanToInt("IX"));
    }
}