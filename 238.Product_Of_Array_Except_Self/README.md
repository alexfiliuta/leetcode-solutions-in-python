# LeetCode Problem: Product of Array Except Self

## Problem Description

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.

### Examples

- **Example 1:**
  - **Input:** `nums = [1,2,3,4]`
  - **Output:** `[24,12,8,6]`
  
- **Example 2:**
  - **Input:** `nums = [-1,1,0,-3,3]`
  - **Output:** `[0,0,9,0,0]`

### Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

### Follow-up

Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

## Approach

The function uses a two-pass solution to achieve the required result without using division. The first pass constructs an array where each position contains the product of all elements before it. The second pass adjusts this array by the product of all elements after each position.

### Steps

1. **Initial Pass to Set Prefix Products:**
   - Traverse from the left to the right of the input array. Multiply the current value of `pre` (initially 1) with the current element and update `pre`. Set the corresponding index in the answer array with the value of `pre`.

2. **Reverse Pass to Set Final Products:**
   - Traverse from the right to the left of the input array. Multiply the current value of `post` (initially 1) with the current element and update `post`. Multiply the corresponding index in the answer array with the value of `post` to get the final product.

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of elements in the input array. Each element is processed exactly twice.
- **Space Complexity:** O(1), ignoring the output array as per the problem's follow-up space complexity requirement.

## Source

This problem is sourced from [LeetCode](https://leetcode.com). The solution provided here is my implementation and understanding of the problem and its solution.