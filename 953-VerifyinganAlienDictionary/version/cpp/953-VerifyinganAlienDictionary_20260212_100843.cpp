// Last updated: 2/12/2026, 10:08:43 AM
/*
 * ### Pattern: Custom Lexicographical Sort (Alien Dictionary)
 * * **The Logic:** Instead of using the standard ASCII alphabet, map each character to a custom rank using a fixed-size array (O(1) space). Compare adjacent words by finding the first differing character; if one word is a prefix of the other, the shorter word must appear first.
 * * **Time Complexity:** O(C) — Where C is the total number of characters across all words in the input. We look at each character at most once.
 * * **Space Complexity:** O(1) — We use a constant-sized array (size 26) to store the character ranks.
*/

1class Solution {
2public:
3    bool isAlienSorted(vector<string>& words, string order) {
4        // Map character to its weight in alien order
5        int weight[26];
6        for (int i = 0; i < 26; i++) weight[order[i] - 'a'] = i;
7
8        for (int i = 0; i < words.size() - 1; i++) {
9            // Use const references to avoid string copies
10            const string& w1 = words[i];
11            const string& w2 = words[i+1];
12            
13            if (isBigger(w1, w2, weight)) return false;
14        }
15        return true;
16    }
17
18private:
19    bool isBigger(const string& w1, const string& w2, int weight[]) {
20        int n = w1.size(), m = w2.size();
21        for (int j = 0; j < min(n, m); j++) {
22            if (w1[j] != w2[j]) {
23                // If the first differing character is out of order
24                return weight[w1[j] - 'a'] > weight[w2[j] - 'a'];
25            }
26        }
27        // If all characters matched, the shorter word must come first
28        // (e.g., "app" should be before "apple")
29        return n > m;
30    }
31};