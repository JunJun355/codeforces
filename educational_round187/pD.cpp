// #include <stdlib.h>
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

struct Node {
    unordered_map<int, Node*> next;
    bool curr;

    Node() {
        curr = false;
        next = {};
    }
};

// issue here
struct Tree {
    Node* root;
    vector<int> primes;
    void init() {
        for (int i=2; i<2000; i++) {
            bool b = false;
            for (int j=0; j<primes.size(); j++) {
                if (i % primes[j] == 0) {
                    b = true;
                    break;
                }
            }
            if (b) continue;
            primes.push_back(i);
        }
        root = new Node();
    }

    void create(vector<int> nums) {
        for (int num : nums) {
            Node* curr = root;
            // cout << num << endl;
            int pi = 0;
            while (num != 1 && pi < primes.size()) {
                if (curr->curr) break;
                if (num % primes[pi]) pi++;
                else {
                    if (curr->next.find(primes[pi]) == curr->next.end()) curr->next[primes[pi]] = new Node();
                    curr = curr->next[primes[pi]];
                    num /= primes[pi];
                }
            }
            if (pi == primes.size() && num != 1) {
                if (curr->next.find(num) == curr->next.end()) curr->next[num] = new Node();
                curr = curr->next[num];
            }
            curr->curr = true;
        }
    }

    bool find(int x) {
        Node* curr = root;
        int pi = 0;
        while (x != 1 && pi < primes.size()) {
            if (curr->curr) return true;
            if (x % primes[pi]) pi++;
            else {
                if (curr->next.find(primes[pi]) != curr->next.end()) curr = curr->next[primes[pi]];
                else return false;
                x /= primes[pi];
            }
        }
        if (pi == primes.size()) {
            if (curr->next.find(x) != curr->next.end()) return true;
        }
        return false;
    }
};

int gcd(int a, int b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

void solve() {
    int n, m;
    cin >> n >> m;
    Tree tree;
    tree.init();
    vector<int> a(n), b(m);
    for (int i =0; i<n; i++) {
        cin >> a[i];
    }
    for (int i=0; i<m; i++) {
        cin >> b[i];
    }
    sort(a.begin(), a.end());
    // vector<bool> some(m, false), none(m, false), all(m, false);
    vector<int> divs;
    for (int thing : a) {
        if (divs.empty()) divs.push_back(thing);
        else {
            if (divs.back() == thing) continue;
            divs.push_back(thing);
        }
    }
    tree.create(divs);

    long long L = 1;
    for (int i=0; i<divs.size(); i++) {
        L = L * divs[i] / gcd(L, divs[i]);
        if (L > 2000000) L = 2000001;
    }

    int some = 0;
    int none = 0;
    int all = 0;
    for (int i=0; i<m; i++) {
        if (b[i] % L == 0) all++;
        else if (tree.find(b[i])) some++;
        else none++;
    //     bool s = false;
    //     bool no = false;
    //     bool al = false;
    //     for (int j=0; j<k && divs[j] * divs[j] <= b[i]; j++) {
    //         if (b[i] % divs[j] == 0) {
    //             if (no) s = true;
    //             else al = true;
    //         }
    //         else {
    //             if (al) s = true;
    //             else no = true;
    //         }
    //     }
    //     if (s) some++;
    //     else if (al) all++;
    //     else none++;
    }
    // cout << none << ' ' << some << ' ' << all << endl;
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