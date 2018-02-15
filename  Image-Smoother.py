class Solution(object):
    def valid(self, rC, cC, row, col):
        if rC>=0 and cC >=0 and row > rC and col > cC:
            return True
        else:
            return False
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if not M:
            return None
        rows = len(M)
        if rows == 0:
            return []
        cols = len(M[0])
        res = []
        for row in range(rows):
            res.append([])
            for col in range(cols):
                count = 0
                s = 0
                for rowC in [-1, 0, 1]:
                    for colC in [-1, 0, 1]:
                        if self.valid(row+rowC, col+colC, rows, cols):
                            count+=1
                            s+=M[row+rowC][col+colC]
                res[row].append(s/count)
        return res