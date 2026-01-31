// Last updated: 1/31/2026, 2:18:58 PM
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n = word1.size(), m = word2.size();
        string res;
        int i = 0, j = 0;
        while(i < n || j < m){
            if(i < n) res += word1[i++];
            if(j < m) res += word2[j++];
        }
        return res;
    }
};
// ------------------------------------------------------------

// class Solution {
// public:
//     string mergeAlternately(string word1, string word2) {
//         int n = word1.size(), m = word2.size();
//         string res;
//         for (int i = 0; i < n || i < m; i++) {
//             if (i < n) {
//                 res += word1[i];
//             }
//             if (i < m) {
//                 res += word2[i];
//             }
//         }
//         return res;
//     }
// };