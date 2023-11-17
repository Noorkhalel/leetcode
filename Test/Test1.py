class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)  
        return False  

nums = [1, 2, 3, 1]
solution_instance = Solution()
result = solution_instance.containsDuplicate(nums)

print(result)
