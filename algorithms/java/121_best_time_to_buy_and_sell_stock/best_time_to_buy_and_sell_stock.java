/**
 * @author Peng
 * Redo this problem using java
 * 
 * @Problem_Description:
 *      Say you have an array for which the i-th element is the price of a given stock on day i.
 *      If you were only permitted to complete at most one transaction 
 *      (ie, buy one and sell one share of the stock), 
 *      design an algorithm to find the maximum profit.
 *      
 *    example 1:
 *      Input: [7, 1, 5, 3, 6, 4]
 *      Output: 5
 *      max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
 *    exmaple 2:
 *      Input: [7, 6, 4, 3, 1]
 *      Output: 0
 *      In this case, no transaction is done, i.e. max profit = 0.
 *      
 */
public class best_time_to_buy_and_sell_stock {

    /**
     * Solution 1:
     *    idea: we need to find the lowest price to buy and the highest price to sell after buying     
     *    in traversal:
     *      1. finding the min_price.
     *      2. finding the biggest profit between min_price and sell price
     * @param prices array refer to each day
     * @return the max profit
     */
    public static int maxProfit(int[] prices) {
        // boundary check
        if(prices.length <= 1)  return 0;
        
        // initial
        int max_profit = 0;
        int min_price = prices[0];
        
        // traverse
        for(int i = 1; i < prices.length; i++) {
            if(prices[i] < min_price)  min_price = prices[i];
            else if(max_profit < prices[i] - min_price)  max_profit = prices[i] - min_price;
        }
        
        // return the result
        return max_profit;
    }
    
    // test code
    public static void main(String[] args) {
        int [] prices = {7, 1, 5, 3, 6, 4}; 
        int max_profit = maxProfit(prices);
        System.out.println("max profit is " + max_profit);
    }

}
