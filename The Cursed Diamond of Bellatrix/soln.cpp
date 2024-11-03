#include <bits/stdc++.h>
using namespace std;
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n = 0;
        cin>>n;
        string s;
        cin >> s;
        for (int i = 0; i < (n + 1) / 2; i++) {
            for (int j = 0; j < (n - 1) / 2 - i; j++) {
                cout << " " << " ";     //Written separately only for ease of understanding
            }
            for (int j = 0; j <= 2 * i && j < n; j++) {
                cout << s[j];
                if (j != 2 * i && j < n - 1) cout << " ";
            }
            cout << endl;
        }
        for (int i = (n - 1) / 2 - 1; i >= 0; i--) {
            for (int j = 0; j < (n - 1) / 2 - i; j++) {
                cout << " " << " ";
            }
            for (int j = 0; j <= 2 * i && j < n; j++) {
                cout << s[j];
                if (j != 2 * i && j < n - 1) cout << " ";
            }
            cout << endl;
        }
    }
    return 0;
}
