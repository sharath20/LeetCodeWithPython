from collections import defaultdict
from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            anagrams[tuple(count)].append(s)

        return list(anagrams.values())


solution = Solution()
strs = ["eat","tea","pat","tap","s","shavar","varsha"]
print(solution.group_anagrams(strs))