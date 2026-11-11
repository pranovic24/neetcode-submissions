class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time: O(m * nlogn), Space: O(m * n)
        result = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            result[sorted_str].append(s)
        return list(result.values())
        