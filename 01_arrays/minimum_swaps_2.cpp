//
// Created by sakhant on 12/13/24.
//
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

size_t find_min(vector<int>& nums, size_t beginning) {
    int min_val = nums[beginning];
    size_t min_ind = beginning;
    for (size_t i = beginning; i < nums.size(); i++) {
        if (nums[i] < min_val) {
            min_val = nums[i];
            min_ind = i;
        }
    }
    return min_ind;
}

int sort(vector<int>& vec) {
    int n_swaps = 0;
    size_t min_ind = find_min(vec, 0);
    cout << min_ind << endl;
    for(int i = 0; i < vec.size(); i++) {
        size_t min_ind = find_min(vec, i);
        //cout << min_ind << endl;
        if (i != min_ind) {
            int temp = vec[min_ind];
            vec[min_ind] = vec[i];
            vec[i] = temp;
            n_swaps++;
            cout << "swapped (" << i << " " << min_ind << ")" << endl;
        }
    }

    return n_swaps;
}

int main() {
    vector<int> arr = {7,1,3,2,4,5,6};
    // for(int i = 0; i < arr.size(); i++) {
    //     cout << arr[i] << " ";
    // }
    // cout << endl;
    int n_swaps = sort(arr);
    // cout << n_swaps << endl;
    return 0;
}
