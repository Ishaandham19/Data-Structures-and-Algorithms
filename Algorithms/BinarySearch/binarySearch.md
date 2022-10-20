# Binary Search

``` Python
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
```
The above code returns the minimum k such that condition(k) is True

``` Python
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left - 1
```
This is the same as the template expect we return the "left - 1".
Doing this return maximum k such that condition(k) is False




Problem : Search for target in sorted array. Return index of target, else -1

``` Python
def search(self, array: List[int], target: int) -> int:
    left, right = 0, len(array) - 1
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left if array[left] == target else -1
```




## References
1. [leetcode comment](https://leetcode.com/problems/first-bad-version/discuss/769685/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.)