class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute Force
        cont = defaultdict(int)
        bucket = [[] for i in range(len(nums) + 1)]

        for n in nums:
            cont[n] += 1
        
        for num, cnt in cont.items():
            bucket[cnt].append(num)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res