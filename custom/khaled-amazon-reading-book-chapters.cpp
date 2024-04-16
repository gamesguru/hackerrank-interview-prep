#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> arr, int days) {
    // number of chapters
    int n_chaps = arr.size();
    // longest chapter
    int m = *max_element(arr.begin(), arr.end());
    std::cout << "num of chapters: " << n_chaps << endl;
    std::cout << "largest chapter: " << m << endl;

    // can't read more than 1 chapter per day
    if (n_chaps > days)
        return -1;

    // find the minimum solution
    for (int ppd=1; ppd<m; ppd++) {
        std::cout << endl << "testing pages per day: " << ppd << endl;

        // iterate through the list, knocking out chapters
        int days = 0;
        for (int i=0; i<n_chaps; i++) {
            std::cout << "CHAPTER " << i << endl;

            // int pages = 0;
            while (arr[i] > 0) {
                std::cout << "Pages remaining " << arr[i] << endl;
                arr[i] -= ppd;
                days++;
            }
        }
        std::cout << "Read " << n_chaps << " in " << days << " days" << endl;
        // int chapters = 0;
        // int pages = 0;
        // int day = 0;
        // while (pages < ppd) {
        //     if (arr[day] < ppd) {
        //         pages += arr[day];
        //         chapters++;
        //     } else if (pages == ppd) {
        //         pages += arr[day];
        //     } else {
        //         pages += ppd;
        //     }
        //     std::cout << "Read " << pages << " on day #" << day << endl;
        //     day++;
        // }
        // if (day >= n_chaps)

        // for (int j=0; j<n_chaps; j++) {
        //     int k = 0;
        //     while (k<i) {
        //         // pop off all chapters we can finish fully in "p" pages
        //     }
        // }
    }

    // return max(chapter_length) since nothing smaller solved it
    return m;
}

int main() {
    // vector<int> chapters = {3, 1, 5, 3, 2};
    // int days = 2;
    // ans = -1

    vector<int> chapters = {2, 3, 4, 5};
    int days = 5;
    // ans = 4

    int result = solution(chapters, days);
    std::cout << result << endl;
    return 0;
}
