# LeetCode Problem: Rotate Array

## Problem Description

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

### Examples

- **Example 1:**
  - **Input:** `nums = [1,2,3,4,5,6,7]`, `k = 3`
  - **Output:** `[5,6,7,1,2,3,4]`
  - **Explanation:**
    - Rotate 1 step to the right: `[7,1,2,3,4,5,6]`
    - Rotate 2 steps to the right: `[6,7,1,2,3,4,5]`
    - Rotate 3 steps to the right: `[5,6,7,1,2,3,4]`

- **Example 2:**
  - **Input:** `nums = [-1,-100,3,99]`, `k = 2`
  - **Output:** `[3,99,-1,-100]`
  - **Explanation:**
    - Rotate 1 step to the right: `[99,-1,-100,3]`
    - Rotate 2 steps to the right: `[3,99,-1,-100]`

### Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

### Follow-Up

- **Can you come up with as many solutions as you can?** There are at least three different ways to solve this problem.
- **Could you do it in-place with O(1) extra space?**

## Approach

The problem can be solved using a **three-step reversal approach** which achieves the desired rotation in-place with O(1) extra space. The main idea is to reverse the entire array, then reverse the first `k` elements, and finally reverse the remaining elements. 

### Steps

1. **Calculate Effective Rotations:**
   - Since rotating the array by `k` steps where `k` is greater than the length of the array is the same as rotating by `k % len(nums)` steps, first compute `k = k % len(nums)`.

2. **Reverse the Entire Array:**
   - Reverse the entire array from the first element to the last. This step puts the last `k` elements in the position where they would be after `k` rotations.

3. **Reverse the First `k` Elements:**
   - Reverse the first `k` elements of the array. This step corrects the order of the first `k` elements.

4. **Reverse the Remaining Elements:**
   - Reverse the elements from index `k` to the end of the array. This step corrects the order of the remaining elements.

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of the array. Each reversal operation runs in O(n) time.
  
- **Space Complexity:** O(1). The algorithm only uses a constant amount of extra space.

## Source

This problem is sourced from [LeetCode](https://leetcode.com). The solution provided here is my implementation and understanding of the problem and its solution.