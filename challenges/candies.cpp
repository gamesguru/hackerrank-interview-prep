#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

void printArr(vector<int> arr) {
    for(int i: arr)
        std::cout << i << " ";
    std::cout << "\n";
}

/*
 * Complete the 'candies' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY arr
 */

long candies(int n, vector<int> arr) {
    printArr(arr);

    long total = 0;
    int c = 1;
    for (int i=0; i<n; i++) {
        // add current index
        total += c;

        std::cout << "c= " << c << "\n";

        // handle forward step
        if (arr[i+1] > arr[i]) {
            c++;
            continue;
        }

//         // handle plateau?
//         if (arr[i+1] == arr[i])
//             continue;

        // handle backward or plateau trend
        for (int j=i+1; j<n-1; j++) {
            if (arr[j+1] > arr[j])
                break;
            c--;
        }
    }
//     for (int i=0; i<n; i++) {
//         // handle base case
//         total += c;
//
//         // handle forward trends: 1 4 5 8 10
//         if (arr[i+1] > arr[i])
//             c++;
//
//         // handle backward trends (10, 8, 5, 2, 1)
// //         for (int j=i+1; j<n-1; j++) {
// //             if (arr[j+1] < arr[j])
// //                 c++;
// //             else {
// //                 i = j;
// //                 break;
// //             }
// //         }
//         std::cout << "i= " << i << "\n";
//         std::cout << "c= " << c << "\n";
//         std::cout << "total= " << total << "\n\n";
//     }

//     std::cout << total << "\n";
    return total;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        string arr_item_temp;
        getline(cin, arr_item_temp);

        int arr_item = stoi(ltrim(rtrim(arr_item_temp)));

        arr[i] = arr_item;
    }

    long result = candies(n, arr);

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

