class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using hash, and hashMap
        # Time: O(n * k log k)
        # Space: O(n * k)
        duplicates = defaultdict(list)

        for phrase in strs:
            # Order something takes log k, to prevent this we can use a key using ord (a hash using the character code) and takes O(n) witch reduce the complexity
            key = ''.join(sorted(phrase))
            duplicates[key].append(phrase)

        return list(duplicates.values())
