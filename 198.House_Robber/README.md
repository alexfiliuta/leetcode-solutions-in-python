# LeetCode Problem: House Robber

## Problem Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected, which will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

### Examples

- **Example 1:**
  - **Input:** `nums = [1,2,3,1]`
  - **Output:** `4`
  - **Explanation:** Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4.

- **Example 2:**
  - **Input:** `nums = [2,7,9,3,1]`
  - **Output:** `12`
  - **Explanation:** Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1). Total amount you can rob = 2 + 9 + 1 = 12.

### Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## Approach

The solution uses a dynamic programming approach where each step decides the maximum money that can be robbed up to that house without triggering the alarm. This is achieved by using a rolling counter that keeps track of the maximum rob-able amount at two previous steps.

### Steps

1. **Initialize Two Trackers:**
   - `last2` starts at 0, representing the maximum rob-able amount from two houses back.
   - `last1` also starts at 0, representing the maximum rob-able amount from the previous house.

2. **Iterate Through Houses:**
   - For each house, calculate the maximum money if this house were robbed, which is the current house's money plus the maximum from two houses back (`last2 + nums[i]`).
   - Compare this with the maximum rob-able amount from not robbing this house (`last1`).

3. **Update Trackers:**
   - Move `last1` to `last2`.
   - Update `last1` to the maximum of robbing or not robbing the current house.

4. **Return the Maximum Rob-able Amount:**
   - After processing all houses, `last1` will contain the maximum amount of money that can be robbed without alerting the police.

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of houses. Each house is processed once.
- **Space Complexity:** O(1), since only a constant amount of space is used for the two trackers.

## Source

This problem is sourced from [LeetCode](https://leetcode.com). The solution provided here is my implementation and understanding of the problem and its solution.