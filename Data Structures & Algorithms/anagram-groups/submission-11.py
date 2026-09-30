class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using hash, and hashMap
        duplicates = {}

        for phrase in strs:
            key = ''.join(sorted(phrase))
            l = duplicates.get(key, [])
            l.append(phrase)
            duplicates[key] = l

        return list(duplicates.values())
