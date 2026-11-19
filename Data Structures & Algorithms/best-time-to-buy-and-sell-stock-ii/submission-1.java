class Solution {
    public int maxProfit(int[] prices) {
        // Understanding:
        // I need to hold at most one share - I must buy and hold share
        // Buy on day 1 and you’re holding one share.
        // You can’t buy again on day 2 while you’re still holding it.
        // You must sell first, and then you can buy again.

        // greedy algorithm approach
        // loop over the array, starting with index 1, compare with the prev one
        // if it is greater than the provious one - it means you are buying on this day and 
        // and selling on the next one: calculating running total of the prices 
        // adding the difference between todays price and prev day price
        int profit = 0;

        for(int i = 1; i < prices.length; i++){
            if(prices[i] > prices[i-1]){
                profit += (prices[i] - prices[i-1]);

            }
        }

        return profit;
    }
}