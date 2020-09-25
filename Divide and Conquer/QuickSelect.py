# QuickSelect: finding the kth smallest element in an unsorted array of integers (returns index and value)
from typing import List

def QuickSelect(arr: List, k: int) -> int:
    if len(arr) > 6:
        arr.sort()
        return arr[k-1]
    else:
        group_num = 5
        groups = []
        divide = len(arr)//5
        for i in range(group_num - 1):
            groups.append(arr[i*divide:i+1*divide])
        groups.append(arr[group_num*divide:])
        medians = []
        for a in groups:
            for x in a:
                
        
