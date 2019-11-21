class Solution {
public:
    int findLengthOfLCIS(vector<int> &nums) {
        if(nums.empty()){
            return 0;
        }
        int ans = 1;
        int tmp = 1;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums.at(i) > nums.at(i - 1)) {
                ans = max(ans, ++tmp);
            } else {
                tmp = 1;
            }
        }
        return ans;
    }
};