# LeetCode Problem: Candy

## Problem Description

There are n children standing in a line. Each child is assigned a rating value given in the integer array `ratings`. You are tasked with giving candies to these children subjected to the following requirements:

- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to distribute the candies to the children.

### Examples

- **Example 1:**
  - **Input:** `ratings = [1,0,2]`
  - **Output:** `5`
  - **Explanation:** You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

- **Example 2:**
  - **Input:** `ratings = [1,2,2]`
  - **Output:** `4`
  - **Explanation:** You can allocate to the first, second and third child with 1, 2, 1 candies respectively. The third child gets 1 candy because it satisfies the above two conditions.

### Constraints

- `n == ratings.length`
- `1 <= n <= 2 * 10^4`
- `0 <= ratings[i] <= 2 * 10^4`

## Approach

The solution involves a two-pass method using an array to store the minimum candies required for each child. The first pass ensures that each child has more candies than the previous child if their rating is higher. The second pass adjusts the candies to ensure that children with a higher rating than their next child have more candies.

### Steps

1. **Initialize Candies Array:**
   - Start with an array `candies` where each child has at least one candy.

2. **Left to Right Pass:**
   - Traverse from left to right, increasing the candy count for a child if their rating is higher than the previous child's rating.

3. **Right to Left Pass:**
   - Traverse from right to left, adjusting the candy count to ensure that any child who has a higher rating than the next child has more candies.

4. **Sum Up Candies:**
   - The result is the sum of all values in the `candies` array, providing the minimum number of candies required.

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of children. Each child's rating is processed twice.
- **Space Complexity:** O(n), for storing the candy distribution.

## Source

This problem is sourced from [LeetCode](https://leetcode.com). The solution provided here is my implementation and understanding of the problem and its solution.