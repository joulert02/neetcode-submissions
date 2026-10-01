class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using hash, and hashMap
        # Time: O(n * k log k)
        # Space: O(n * k)
        duplicates = defaultdict(list)

        for phrase in strs:
            key = ''.join(sorted(phrase))
            duplicates[key].append(phrase)

        return list(duplicates.values())
