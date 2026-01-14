#include <iostream>
#include <string>
#include <vector>
using namespace std;

void solve() {
    int n; 
    cin >> n;

    vector<string> arr(n);

    // input in arr
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    string s = arr[0];

    // adding to the back or front
    for (int i = 1; i < n; ++i) {
        string option_front = arr[i] + s;
        string option_back = s + arr[i];

        if (option_front < option_back) {
            s = option_front;
        } else {
            s = option_back;
        }
    }
    
    cout << s << endl; 
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        solve();
    }
    
    return 0;
}