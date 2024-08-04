# LeetCode Problem: Trapping Rain Water

## Problem Description

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

### Examples

- **Example 1:**
  - **Input:** `height = [0,1,0,2,1,0,1,3,2,1,2,1]`
  - **Output:** `6`
  - **Explanation:** The above elevation map (black section) is represented by array `[0,1,0,2,1,0,1,3,2,1,2,1]`. In this case, 6 units of rain water (blue section) are being trapped.
  
- **Example 2:**
  - **Input:** `height = [4,2,0,3,2,5]`
  - **Output:** `9`
  
### Constraints

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Approach

The problem is approached using a two-pointer technique that helps track the maximum heights from both the left and right sides. The trapped water above each bar is determined by the difference between the minimum of the maximum heights from both sides and the height of the current bar.

### Steps

1. **Initialize Pointers and Variables:**
   - Set two pointers, one at the beginning (`l`) and one at the end (`r`) of the height array. Also, initialize two variables to track the maximum heights encountered from the left (`leftMax`) and from the right (`rightMax`).

2. **Iterate with Two Pointers:**
   - Traverse the array using the two pointers. The direction of traversal for each pointer is determined by the comparison of `leftMax` and `rightMax`.

3. **Calculate Trapped Water:**
   - If the height at the current pointer is less than the respective maximum height, compute the trapped water for that position and add it to the result. Then update the maximum heights and move the pointer inward.

4. **Continue Until Pointers Meet:**
   - Continue the process until the two pointers meet.

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of the height array. Each element is visited at most once.
- **Space Complexity:** O(1). Only constant space is used beyond the input list.

## Source

This problem is sourced from [LeetCode](https://leetcode.com). The solution provided here is my implementation and understanding of the problem and its solution.