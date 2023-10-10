class Solution(object):
    def reverseWords(self, s):

        a = []
        f=""
        s = s +" "
        for x in s:
            f=f+x
            if x ==" ":
               a.append(f)
               f =""
        txt =""
        for x in range(len(a)-1,-1,-1):
            txt += a[x] 
        print(txt)
        txt = txt[::-1]
        txt = txt[1:]   
        return txt
    

solution = Solution()
s = "Let's take LeetCode contest"
result = solution.reverseWords(s)
print(result)
