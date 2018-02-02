class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = list()
        sList = list(s)
        if len(sList)%2 !=0:
            return False
        for i in range(len(sList)):
            if sList[i] == '{' or sList[i] == '(' or sList[i] == '[':
                a.append(sList[i])
            else:
                if len(a)!=0:
                    k = a.pop()
                    if k == "{" and sList[i]!="}":
                        return False
                        break
                    if k == "(" and sList[i]!=")":
                        return False
                        break
                    if k == "[" and sList[i]!="]":
                        return False
                        break
                else:
                    return False
                    break
        if len(a)!=0:
            return False
        return True