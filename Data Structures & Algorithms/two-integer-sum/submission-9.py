class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # This is a brute force solution
        # Time: O(n^2)
        # Space: O(n^2)
        # if len(nums) <= 2: return [0, 1]
        
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # return []

        # Using HashMap
        # Time: O(n)
        # Space O(n)
        if len(nums) == 2: return [0, 1]

        visited = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in visited:
                return [visited.get(difference), i]
            
            visited[nums[i]] = i
        
        return []



