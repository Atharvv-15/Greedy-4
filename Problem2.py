# Problem 1: Shortest Way to Form String
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if not source:
            return -1
        if not target:
            return 0

        i, j = 0, 0
        Map = {}
        count = 0

        for idx, char in enumerate(source):
            if char not in Map:
                Map[char] = []
            Map[char].append(idx)

        def binarySearch(li, target):
            low, high = 0, len(li) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if li[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        i = 0
        while j < len(target):
            tChar = target[j]

            if tChar not in Map:
                return -1

            li = Map[tChar]

            k = binarySearch(li, i)

            if k == len(li):
                i = 0
                count += 1

            else:
                i = li[k]
                i += 1
                j += 1
                if j == len(target): return count + 1
                if i == len(source):
                    i = 0
                    count += 1

        return -1