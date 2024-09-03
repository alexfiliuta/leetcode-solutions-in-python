# LeetCode Problem: Climbing Stairs

## Problem Description

You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

### Examples

- **Example 1:**
  - **Input:** `n = 2`
  - **Output:** `2`
  - **Explanation:** There are two ways to climb to the top:
    1. 1 step + 1 step
    2. 2 steps

- **Example 2:**
  - **Input:** `n = 3`
  - **Output:** `3`
  - **Explanation:** There are three ways to climb to the top:
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

### Constraints

- `1 <= n <= 45`

## Approach

The problem is solved using a dynamic programming approach with memoization to store previously calculated results, which helps in reducing the computation time significantly by avoiding repeated calculations for the same inputs.

### Steps

1. **Memoization Setup:**
   - Initialize a dictionary `memo` to store the results of subproblems.

2. **Base Case Handling:**
   - If `n` is 1 or 0, return 1 since there is only one way to climb one step or stay at the ground.

3. **Recursive Relation:**
   - If `n` is in the `memo`, return `memo[n]`.
   - Otherwise, compute the number of ways to climb `n` steps by summing the ways to climb `n-1` and `n-2` steps. This is based on the decision to take either a single step or two steps from a given position.

4. **Return the Computed Value:**
   - Store the computed result in `memo` and return it.

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of steps. Each step's number of ways is computed once and then retrieved from the memo, resulting in linear complexity.
- **Space Complexity:** O(n), due to the memoization dictionary holding up to `n` key-value pairs. (Keep in mind that this problem could have been easily implemented in O(1) but I decided to solve it using memoization in order to showcase the power of top-down DP)

## Source

This problem is sourced from [LeetCode](https://leetcode.com). The solution provided here is my implementation and understanding of the problem and its solution.