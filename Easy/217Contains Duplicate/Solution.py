class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)
        return False
    
    
            