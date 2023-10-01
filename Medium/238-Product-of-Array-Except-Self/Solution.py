class Solution(object):
    def productExceptSelf(self, nums):
        res = [1]*len(nums)
        
        for x in range(1,len(nums)):
            res[x] =  res[x-1] * nums[x-1]

        postfix = 1
        for x in range(len(nums) - 1,-1,-1):
            res[x] = res[x] * postfix
            postfix =postfix * nums[x]

        return(res)

strs =  [1, 2, 3,4]
solution = Solution()
result = solution.productExceptSelf(strs)
print(result)
