using namespace std;
class Solution {
public:
    int repeatedNTimes(vector<int> &A) {
        for (int i = A.size() - 1; i > 1; --i) {
            if (A[i] == A[i - 1] or A[i] == A[i - 2]) {
                return A[i];
            }
        }
        return A[0];
    }
};