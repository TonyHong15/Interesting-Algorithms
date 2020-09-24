# This algorithm takes an unsorted List and returns the number of inversions in the list (pairs with i<j but a[i]>a[j])
from typing import List


def counting_inversions(a: List) -> int:
    if len(a) <= 1:
        return 0
    else:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]
        left_inversions = counting_inversions(left)
        right_inversions = counting_inversions(right)
        cross = 0
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                cross += len(left) - i
                j += 1
            k += 1
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
        print(a)
        return left_inversions + right_inversions + cross


if __name__ == "__main__":
    example_list = [1, 5, 4, 8, 10, 2, 6, 9, 3, 7]
    print(counting_inversions(example_list))
