# LeetCode Problem: Best Time To Buy And Sell Stock II

## Problem Description

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it and then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

### Examples

- **Example 1:**
  - **Input:** `prices = [7,1,5,3,6,4]`
  - **Output:** `7`
  - **Explanation:** 
    - Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5 - 1 = 4.
    - Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6 - 3 = 3.
    - Total profit is 4 + 3 = 7.

- **Example 2:**
  - **Input:** `prices = [1,2,3,4,5]`
  - **Output:** `4`
  - **Explanation:** Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5 - 1 = 4. Total profit is 4.

- **Example 3:**
  - **Input:** `prices = [7,6,4,3,1]`
  - **Output:** `0`
  - **Explanation:** There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

### Constraints

- `1 <= prices.length <= 3 * 10^4`
- `0 <= prices[i] <= 10^4`

## Approach

This solution utilizes a **greedy approach** where the goal is to maximize profit by accumulating profits from every local upward price trend.

### Steps

1. **Traverse Prices:** Iterate over the `prices` list. At each index `i`, check if the price at the next day `i+1` is higher than the current price at `i`.
2. **Accumulate Profit:** If the price at `i+1` is greater than the price at `i`, calculate the profit (`prices[i+1] - prices[i]`) and add it to the total profit. This models buying and selling stock on consecutive profitable days.
3. **Return Profit:** After traversing all the prices, return the accumulated profit.

1. **Initialize Pointers:** We use two pointers, `buy` and `sell`. Initially, `buy` is set to 0 (first day) and `sell` is set to 1 (next day).
2. **Traverse Prices:** As we iterate through the `prices` list:
   - If the price at `buy` is less than the price at `sell`, calculate the potential profit and update the `profit` if it's greater than the current maximum profit.
   - If the price at `sell` is less than or equal to the price at `buy`, we move the `buy` pointer to the position of `sell` (indicating the lowest price seen so far).
   - Continue iterating, moving the `sell` pointer forward after each comparison.
3. **Return Profit:** The maximum profit calculated during the iteration is returned at the end.

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of the `prices` list. We loop through the list once, making comparisons and additions, so the time complexity is linear.
  
- **Space Complexity:** O(1). The algorithm only uses a constant amount of extra space (for the `profit` variable), regardless of the input size, leading to constant space complexity.


## Source

This problem is sourced from [LeetCode](https://leetcode.com). The solution provided here is my implementation and understanding of the problem and its solution.