class Solution(object):
    def swap(self, s, a, b):
        temp = s[a]
        print s[a]
        print s[b]
        print s
        s[a] = s[b]
        s[b] = temp
        return s
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vow = ['a','e','i','o','u', 'A', "E", 'I', 'O', 'U']
        start = 0
        end = len(s)-1
        while(start<end):
            if(start<end and s[start] not in vow):
                start+=1
            if(start<end and s[end] not in vow):
                end-=1
            s = list(s)
            s[start], s[end] = s[end], s[start]
            ''.join(s)
            start+=1
            end-=1
        return ''.join(s)