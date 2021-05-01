/*
   Binary search function that returns the index of the target element in the vector containing T.

   Precondtions:  Data type T must be compatible with relational operators <, >, =
                  Must be a sorted vector
   Postconditions: Returns the index(int value from 0 to [size-1]) of the first occurence of target T in the vector
                   Returns -1 if the target value is not present in the vector
*/


#include <vector>
using namespace std;

template <class T>
int binary_search_helper(vector<T> a, T target, int left, int right) {
    int mid = left + (right - left) / 2;

    if (right < left)    //base case
        return -1;

    if (target == a[mid]) {   //target eleme is found
        return mid;
    }
    else if (target < a[mid]) {
        return binary_search_helper(a, target, left, mid - 1);   //divides array in half towards left side
    } 
    else {
        return binary_search_helper(a, target, mid + 1, right);   //divides array in half towards right side
    }
}

template <class T>
int binary_search(vector<T> nums, T target) {
    int left = 0;
    int right = nums.size() - 1;
    return binary_search_helper(nums, target, left, right);
}
