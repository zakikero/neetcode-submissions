class Solution {
   public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() < 2) return 0;

        int left = 0, right = 1;

        int maxProfit = 0;

        while (right < prices.size()) {
            int profit = prices[right] - prices[left];

            if (profit < 0) {
                left = right;
            } else if (profit > maxProfit) {
                maxProfit = profit;
            }

            right++;
        }

        return maxProfit;
    }
};
