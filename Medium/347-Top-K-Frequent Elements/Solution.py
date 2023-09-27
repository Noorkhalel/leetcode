import heapq
class Solution(object):
    def topKFrequent(self, nums, k):

        my_dict = {}
        for x in nums:
            if x not in my_dict:
                my_dict[x] = 1
            else:
                my_dict[x] = my_dict[x]+1
        
        heap = [(-freq, num) for num, freq in my_dict.items()]
        heapq.heapify(heap)
        topK = []
        for x in range(k):
            freq,num = heapq.heappop(heap)
            topK.append(num)

        return topK


strs = [1,1,2,2,3,1,3,3,3,3,3,3]
k = 3
solution = Solution()
result = solution.topKFrequent(strs,k)
print(result)
