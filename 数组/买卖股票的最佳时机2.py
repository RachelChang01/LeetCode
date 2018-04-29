class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        else:
            min_lst,max_lst = [],[]
            profit = 0
            if prices[0]<prices[1]:
                min_lst.append(0)
            for i in range(len(prices)-2):
                if prices[i+1]>prices[i] and prices[i+1]>=prices[i+2]: #至高点要平的部分的第一个点，要后面加等号
                    max_lst.append(i+1)
                if prices[i+1]<=prices[i] and prices[i+1]<prices[i+2]: #至低点要平的部分的最后一个点，要前面加等号
                    min_lst.append(i+1)
            if prices[-1]>prices[-2]:
                max_lst.append(len(prices)-1)
            for m,n in zip(max_lst,min_lst):
                profit = profit+prices[m]-prices[n]  #至高点和至低点一定会是成对的，加入机制导致的
            return profit