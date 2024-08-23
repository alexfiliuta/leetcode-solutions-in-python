# LeetCode Problem: Jump Game

## Problem Description

You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.

### Examples

- **Example 1:**
  - **Input:** `nums = [2,3,1,1,4]`
  - **Output:** `true`
  - **Explanation:** Jump 1 step from index 0 to 1, then 3 steps to the last index.

- **Example 2:**
  - **Input:** `nums = [3,2,1,0,4]`
  - **Output:** `false`
  - **Explanation:** You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

### Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## Approach

This solution uses a **greedy algorithm** to determine if the last index can be reached. We keep track of the furthest position we can reach at each step.

### Steps

1. **Initialize `furthest`:** Set the variable `furthest` to 0, representing the farthest index we can reach.
2. **Iterate Over `nums`:** Loop through the array using the index `x`. For each index, check:
   - If `x` is greater than `furthest`, return `false` since we cannot reach this position.
   - Otherwise, update `furthest` to be the maximum of `furthest` and `x + nums[x]`.
   - If `furthest` is greater than or equal to the last index, return `true`.
3. **Return Result:** After the loop, return `false` if the last index is not reachable.

## Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of `nums`. We only traverse the array once.
- **Space Complexity:** O(1), since we only use a single variable `furthest` to track the farthest reachable index.

## Source

This problem is sourced from [LeetCode](https://leetcode.com). The solution provided here is my implementation and understanding of the problem and its solution.
