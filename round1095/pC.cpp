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
        
        int bot = 1;
        int top = n;
        while (bot < top) {
            int mid = (bot + top + 1) / 2;
            
            bool works = true;
            vector<int> temp;
            vector<bool> covered(mid, false);
            for (int i : arr) {
                if (i < mid && !covered[i]) {
                    covered[i] = true;
                    continue;
                }
                temp.push_back(i);
            }
            sort(temp.begin(), temp.end());
            for (int i=mid - 1; i>=0; i--) {
                if (covered[i]) continue;
                // cout << i << ' ' << temp.back() << endl;
                if (temp.back() <= i * 2) {
                    works = false;
                    break;
                }
                temp.pop_back();
            }

            if (works) bot = mid;
            else top = mid - 1;
        }
        cout << bot << endl;
    }
}