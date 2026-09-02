# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)
    
    def mergeSortHelper(self, pairs: List[Pair], start: int, end: int) -> List[Pair]:
        if (end - start + 1) <= 1:
            return pairs
        
        middle = (start + end) // 2

        self.mergeSortHelper(pairs, start, middle)
        self.mergeSortHelper(pairs, middle + 1, end)
        self.merge(pairs, start, middle, end)

        return pairs
    
    def merge(self, arr: List[Pair], start: int, middle: int, end: int) -> None:
        left = arr[start: middle + 1]
        right = arr[middle + 1: end + 1]

        i = 0 
        j = 0
        k = start

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1



