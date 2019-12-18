class Solution {
    public int subarraysDivByK(int[] A, int K) {
        int[] tmp = new int[A.length + 1];
        tmp[0] = 0;
        for (int i = 1; i < A.length + 1; i++) {
            tmp[i] = tmp[i - 1] + A[i - 1];
        }
        System.out.println(Arrays.toString(tmp));
        Map<Integer, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < tmp.length; i++) {
            if (hashMap.containsKey(((tmp[i] % K) + K) % K)) {
                hashMap.put(((tmp[i] % K) + K) % K, hashMap.get(((tmp[i] % K) + K) % K) + 1);
            } else {
                hashMap.put(((tmp[i] % K) + K) % K, 1);
            }
        }
        System.out.println(hashMap.keySet());
        System.out.println(hashMap.values());
        int ans = 0;
        Iterator<Integer> iterator = hashMap.values().iterator();
        while (iterator.hasNext()) {
            int value = iterator.next();
            ans += value * (value - 1) / 2;
        }
        return ans;
    }
}