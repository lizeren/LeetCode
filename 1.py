class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            for k in hashmap:
                if k == complement:
                    if hashmap[complement] != i:
                        return [i, hashmap[complement]] 
            # if complement in hashmap and hashmap[complement] != i:
            #     return [i, hashmap[complement]] 

"""
Use hash map to shortern the search time
https://leetcode.com/problems/two-sum/
"""
