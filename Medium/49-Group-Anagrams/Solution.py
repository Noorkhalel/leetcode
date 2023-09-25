import collections

class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        
        if len(strs) == 1:
            ans[strs[0]].append(strs[0]) 
            return list(ans.values())
        else:
            arr = []
            for i, x in enumerate(strs):
                sorted_word = ''.join(sorted(x))
                arr.append(sorted_word)
            
            for i in range(len(arr)):  # Use a loop to access elements in arr
                ans[arr[i]].append(strs[i])
       
        return list(ans.values())

strs = ["eat","tea","tan","ate","nat","bat"]
# strs = ["","b"]
solution = Solution()
result = solution.groupAnagrams(strs)
print(result)
