#include <vector>
#include <iostream>

using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }

    if (n == 1) {
        cout << 1 << endl;
    }
    else {
        for (int i=0; i<n; i++) {
            cout << 2 << ' ';
        }
        cout << endl;
    }
}

int main() {
    int t;
    cin >> t;
    for (int i=0; i<t; i++) {
        solve();
    }
}