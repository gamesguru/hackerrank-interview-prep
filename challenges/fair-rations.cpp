#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'fairRations' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts INTEGER_ARRAY B as parameter.
 */

string fairRations(vector<int> B) {

    /** sample test cases
     *
     * 2 2 2 3 3 ans= 2 loaves [2 inversions, 2 adjacent]
     * 2 3 3 3 3
     * 2 2 3 3 3 ans= NO       [3 inversions]
     * 2 3 4 5 6 ans= 4 loaves [2 inversions]
     *
     * 2 3 4 5 5 5 6
     * 2 4 5 5 5 5 6
     * 2 4 6 6 5 5 6
     * 2 4 6 6 6 6 6 --> 6 loaves total
     *
     * 2 3 6 5 4 5 6 5
     * 2 4.7 5 4 5 6 5
     * 2 4 8.6 4 5 6 5
     * 2 4 8 6 4 6.5 5
     * 2 4 8 6 4 6 6.6 --> 8 loaves total
     *
     * Conjecture:
     *              n_loaves = 2 * n_inversions (if n_inversions is even)
     *              NO solution                 (if n_inversions is odd)
     */

    int n_odds = 0;
    int n_odds_adjacent = 0;

    // initial loop through data
    std::cout << "B= ";
    for (int i: B) {
        std::cout << i << ' ';
        if (i % 2 == 1) {
            n_odds++;
        }
    }
    // count adjacent odds
    for (int i=0; i<=B.size(); i++) {
        if (B[i]%2 == 1 && B[i+1]%2 == 1)
            n_odds_adjacent++;
    }
    std::cout << "(len=" << B.size();
    std::cout << ", n_odds_adjacent=" << n_odds_adjacent;
    std::cout << ", n_odds=" << n_odds << ")" << "\n";

    // return if odd number of odds (impossible to solve due to invariant constraint)
    if (n_odds % 2 == 1) {
        std::cout << "NO" << "\n";
        return "NO";
    }

    // otherwise, compute the minimum number of bread loaves needed

    std::cout << "UNKNOWN" << "\n";
    return "UNKNOWN";
}

int main() {
    ofstream fout(getenv("OUTPUT_PATH"));

    string N_temp;
    getline(cin, N_temp);

    int N = stoi(ltrim(rtrim(N_temp)));

    string B_temp_temp;
    getline(cin, B_temp_temp);

    vector<string> B_temp = split(rtrim(B_temp_temp));

    vector<int> B(N);

    for (int i = 0; i < N; i++) {
        int B_item = stoi(B_temp[i]);

        B[i] = B_item;
    }

    string result = fairRations(B);

    fout << result << "\n";

    fout.close();

    return 0;
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

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}

