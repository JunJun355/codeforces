#include <bits/stdc++.h>

using namespace std;


int main() {
    int t;
    cin >> t;
    vector<int> index;
    vector<int> digs;
    for (int test = 0; test < t; test++) {
        int n;
        cin >> n;
        digs.clear();
        for (int i=0; i<n; i++) {
            int temp;
            cin >> temp;
            digs.push_back(temp);
        }
        for (int i=0; i<n; i++) {
            index[digs[i]] = i;
        }
        for (int bot=0, top=n - 1; bot < top; bot++, top--) {
            if (index[digs[bot]] == bot)
        }
    }
}