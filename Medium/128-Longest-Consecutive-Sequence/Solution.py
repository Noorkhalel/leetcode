class Solution(object):
    def longestConsecutive(self, nums):

        numSet = set(nums)
        longest = 0
        print(set(nums))
        for n in numSet:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    

strs = [100,4,200,1,3,2]
solution = Solution()
result = solution.longestConsecutive(strs)
print(result)
