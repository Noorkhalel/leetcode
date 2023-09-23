class Solution(object):
    def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        return False
        
    
s = "rat"
t = "car"
result = Solution.isAnagram(s,t)
print(result)