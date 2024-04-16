#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> arr, int days_til_exam) {
    // number of chapters
    int n_chaps = arr.size();
    // longest chapter
    int m = *max_element(arr.begin(), arr.end());

    std::cout << "num of chapters: " << n_chaps << endl;
    std::cout << "largest chapter: " << m << endl;
    std::cout << "days until exam: " << days_til_exam << endl;

    // can't read more than 1 chapter per day
    if (n_chaps > days_til_exam)
        return -1;

    // find the minimum solution
    for (int ppd=1; ppd<m; ppd++) {
        std::cout << endl << "testing pages per day: " << ppd << endl;

        // iterate through the list, knocking out chapters
        int days_read = 0;
        int chap_index = 0;

        for (chap_index=0; chap_index<n_chaps; chap_index++) {
            std::cout << "CHAPTER " << chap_index << endl;

            // go for however many days to finish this chapter
            int pages_read = 0;

            while (pages_read < arr[chap_index]) {
                std::cout << "Pages remaining " << arr[chap_index] - pages_read
                          << endl;
                pages_read += ppd;
                days_read++;
            }

            // break out if we exceed the days til the exam
            if (days_read >= days_til_exam)
                break;
        }

        // if we didn't finish all chapters or we exceeded days til test, fail
        if (chap_index < n_chaps - 1 or days_read > days_til_exam) {
            std::cout << "Failed to complete book" << endl;
        } else {
            std::cout << "Finished BOOK in " << days_read
                      << " days (" << ppd << " pages per day)" << endl;
            return ppd;
        }
    }

    // return max(chapter_length) since nothing smaller solved it
    // note that we iterated up to m-1, and m is guaranteed to solve
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
