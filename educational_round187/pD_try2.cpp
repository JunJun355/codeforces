// #include <stdlib.h>
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

void solve() {
    int n, m;
    cin >> n >> m;
    vector<int> a(n), b(m);
    for (int i =0; i<n; i++) {
        cin >> a[i];
    }
    for (int i=0; i<m; i++) {
        cin >> b[i];
    }
    sort(a.begin(), a.end());
    vector<int> divs;
    for (int thing : a) {
        if (divs.empty()) divs.push_back(thing);
        else {
            if (divs.back() == thing) continue;
            divs.push_back(thing);
        }
    }
    vector<int> sieve(2000001, false);
    for (int div : divs) {
        if (sieve[div]) continue;
        for (int i=div; i<2000001; i += div) {
            sieve[i] = true;
        }
    }
    long long lcm = 1;
    for (int div : divs) {
        lcm = lcm * div / gcd(lcm, div);
        if (lcm > 2000000) lcm = 2000001;
    }

    int none = 0, some = 0, all = 0;
    for (int thing : b) {
        if (thing % lcm == 0) all++;
        else if (sieve[thing]) some++;
        else none++;
    }

    int alice = (some + 1) / 2 + all;
    int bob = (some) / 2 + none;
    if (alice > bob) {
        cout << "Alice" << endl;
    }
    else {
        cout << "Bob" << endl;
    }
}

int main() {
    int t;
    cin >> t;
    for (int i=0; i<t; i++) {
        solve();
    }
}