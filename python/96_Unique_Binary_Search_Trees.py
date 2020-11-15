class Solution1(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        record={0:1,1:1,2:2}
        if n in record:
            return record[n]
        for x in range(3,n+1):
            t=0
            for i in range(1,x+1):
                a=record[i-1]
                b=record[x-i]
                t=t+a*b
            record[x]=t
        return record[n]

class Solution2(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.cal(n,{1:1,2:2,0:1})
    
    def cal(self,n,record):
        if n in record:
            return record[n]
        t=0
        for i in range(1,n+1):
            record[i-1]=self.cal(i-1,record)
            record[n-i]=self.cal(n-i,record)
            t=t+record[i-1]*record[n-i]
        record[n]=t
        return record[n]