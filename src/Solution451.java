class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (hashMap.containsKey(s.charAt(i))) {
                hashMap.put(s.charAt(i), hashMap.get(s.charAt(i)) + 1);
            } else {
                hashMap.put(s.charAt(i), 1);
            }
        }
        StringBuffer res = new StringBuffer();
        Map<Character, Integer> tmpMap = new HashMap<>(hashMap);
        for (int i = 0; i < s.length(); i++) {
            for (char c : tmpMap.keySet()
                    ) {
                tmpMap.put(c, tmpMap.get(c) - 1);
                if (tmpMap.get(c) == 0) {
                    for (int j = 0; j < hashMap.get(c); j++) {
                        res.append(c);
                    }
                }
            }
        }
        return res.reverse().toString();
    }
}