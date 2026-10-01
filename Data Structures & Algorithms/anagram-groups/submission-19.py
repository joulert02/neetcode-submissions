class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using hash, and hashMap
        # Time: O(n)
        # Space: O(n)
        duplicates = defaultdict(list)

        for phrase in strs:
            key = ''.join(sorted(phrase))
            duplicates[key].append(phrase)

        return list(duplicates.values())
