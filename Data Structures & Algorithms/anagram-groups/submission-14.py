class Solution:
    def getKey(self, strs):
        count = [0] * 26
        for l in strs:
            count[ord(l) - ord('a')] += 1
        return tuple(count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using hash, and hashMap
        # Time: O(n)
        # Space: O(n)
        res = defaultdict(list)

        for phrase in strs:
            key = self.getKey(phrase)
            res[key].append(phrase)

        return list(res.values())
