# LeetCode Problem: Best Time To Buy And Sell Stock

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If no profit can be made, return 0.

### Examples

- **Example 1:**
  - **Input:** `prices = [7,1,5,3,6,4]`
  - **Output:** `5`
  - **Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5. Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

- **Example 2:**
  - **Input:** `prices = [7,6,4,3,1]`
  - **Output:** `0`
  - **Explanation:** In this case, no transactions are done and the max profit = 0.

### Constraints

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

## Approach

This solution uses a **two-pointer approach** to solve the problem in a single pass.

### Steps

1. **Initialize Pointers:** We use two pointers, `buy` and `sell`. Initially, `buy` is set to 0 (first day) and `sell` is set to 1 (next day).
2. **Traverse Prices:** As we iterate through the `prices` list:
   - If the price at `buy` is less than the price at `sell`, calculate the potential profit and update the `profit` if it's greater than the current maximum profit.
   - If the price at `sell` is less than or equal to the price at `buy`, we move the `buy` pointer to the position of `sell` (indicating the lowest price seen so far).
   - Continue iterating, moving the `sell` pointer forward after each comparison.
3. **Return Profit:** The maximum profit calculated during the iteration is returned at the end.

## Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of `prices`. We only iterate through the list once, comparing prices in constant time.
- **Space Complexity:** O(1), since we only use a few variables (`buy`, `sell`, and `profit`) to track the state of the computation.

## Source

This problem is sourced from [LeetCode](https://leetcode.com). The solution provided here is my implementation and understanding of the problem and its solution.