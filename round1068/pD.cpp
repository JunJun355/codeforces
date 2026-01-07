#include <bits/stdc++.h>

using namespace std;


vector<int> digs;
int aux(int i, int left, int prev, int score, int carry) {
    if (i == digs.size()) return score + left;
    if (carry == 1) {
        if (digs[i] == 1) return aux(i + 1, left, 0, score + 1, 1);
        int ans = aux(i + 1, left, 1, score, 0);
        if (left > 0) {
            ans = max(ans, aux(i + 1, left - 1, 0, score + 1, 1));
        }
        return ans;
    }
    int ans = aux(i + 1, left, digs[i], score, 0);
    if (prev == 0 && digs[i] == 1 && left > 0) {
        ans = max(ans, aux(i + 1, left - 1, 0, score + 1, 1));
    }
    return ans;
}

int main() {
    int t;
    cin >> t;
    for (int test = 0; test < t; test++) {
        int n, k;
        cin >> n >> k;
        digs.clear();
        for (;n > 0; n /= 2) {
            digs.push_back(n % 2);
        }

        cout << aux(0,k,0,0,0) << endl;
    }
}