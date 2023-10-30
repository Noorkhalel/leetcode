class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s=source, d=dest, p=price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]

# Example usage
n = 3  # Number of cities
flights = [[0, 1, 100], [1, 2, 200], [0, 2, 500]]
src = 0  # Source city
dst = 2  # Destination city
k = 1  # Maximum stops allowed

solution = Solution()
cheapest_price = solution.findCheapestPrice(n, flights, src, dst, k)
print(cheapest_price)