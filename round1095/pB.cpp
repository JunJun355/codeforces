#include <queue>
#include <set>
#include <iostream>
#include <vector>


using namespace std;

int main() {
    int t;
    cin >> t;
    for (int test=0; test < t; test++) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i=0; i<n; i++) cin >> arr[i];
        int ans = 0;
        for (int i=0; i<n - 1; i++) {
            if (arr[i] % abs(arr[i] - arr[i + 1]) == 0) ans += 1;
        }
        // set<int> ini;
        // deque<int> q;
        // for (int i=0; i<n - 1; i++) {
        //     if (abs(arr[i] - arr[i + 1]) == 1 && min(arr[i], arr[i + 1]) != 1) {
        //         ans++;
        //     }
        // }
        // for (int i=0; i<n; i++) {
        //     if (arr[i] % 2 == 0 && ini.find(arr[i] / 2) != ini.end()) ans++;
        //     while (!q.empty() && q.front() <= arr[i] / 2) {
        //         ini.erase(q.front());
        //         q.pop_front();
        //     }
        //     while (!q.empty() && q.back() > arr[i]) {
        //         ini.erase(q.back());
        //         q.pop_back();
        //     }
        //     q.push_back(arr[i]);
        //     ini.insert(arr[i]);
        // }
        // ini.clear();
        // while (!q.empty()) q.pop_back();
        // for (int i=n - 1; i>= 0; i--) {
        //     if (arr[i] % 2 == 0 && ini.find(arr[i] / 2) != ini.end()) ans++;
        //     while (!q.empty() && q.front() <= arr[i] / 2) {
        //         ini.erase(q.front());
        //         q.pop_front();
        //     }
        //     while (!q.empty() && q.back() > arr[i]) {
        //         ini.erase(q.back());
        //         q.pop_back();
        //     }
        //     q.push_back(arr[i]);
        //     ini.insert(arr[i]);
        // }
        cout << ans << endl;
    }
}