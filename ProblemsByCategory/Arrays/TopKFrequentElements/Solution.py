from typing import List, Any


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> list[Any] | None:

        count = {}  # dictionory for frequency of nums
        freq = [[] for i in range(len(nums) + 1)]  # fequency bucket that stores count:number pairs

        for n in nums:
            count[n] = 1 + count.get(n, 0)  # adding frequency for numbers

        for n, c in count.items():
            freq[c].append(n)  # add count and their number to bucket

        result = []
        ## looping over the bucket list from the highest count and return the k most counts
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
        return result

o = Solution()
print(o.topKFrequent([1, 2, 3], 2))
print(o.topKFrequent([1, 2, 2, 3, 3], 2))
