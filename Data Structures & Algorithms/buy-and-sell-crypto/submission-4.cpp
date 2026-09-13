class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() < 2) return 0;

        int minBuy = INT_MAX;
        int maxProfit = 0;

        for(int& p: prices){
            int sell = p - minBuy;
            maxProfit = sell > maxProfit ? sell : maxProfit;
            minBuy = p < minBuy ? p : minBuy;

        }

        return maxProfit;
    }
};
