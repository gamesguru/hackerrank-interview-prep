#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
void printArr(const vector<string>);
/*
 * Complete the 'gridChallenge' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING_ARRAY grid as parameter.
 */

string gridChallenge(vector<string> grid) {
    int n = grid.size();

    // sort each row's elements
    printArr(grid);
    for (int i=0; i<n; i++) {
        std::sort(grid[i].begin(), grid[i].end());
    }
    std::cout << "\n";
    printArr(grid);

    // look for any out of order column element, return NO if found
    for (int i=0; i<n-1; i++) {
        for (int j=0; j<n; j++) {
            if (grid[i][j] > grid[i+1][j]) {
                std::cout << "NO" << "\n\n\n";
                return "NO";
            }
        }
    }

    std::cout << "YES" << "\n\n\n";
    return "YES";
}

int main() {
    ofstream fout(getenv("OUTPUT_PATH"));

    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string n_temp;
        getline(cin, n_temp);

        int n = stoi(ltrim(rtrim(n_temp)));

        vector<string> grid(n);

        for (int i = 0; i < n; i++) {
            string grid_item;
            getline(cin, grid_item);

            grid[i] = grid_item;
        }

        string result = gridChallenge(grid);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}

void printArr(vector<string> arr) {
    for (string s: arr)
        std::cout << s << "\n";
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

