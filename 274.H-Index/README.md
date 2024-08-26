# LeetCode Problem: H-Index

## Problem Description

Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `i`th paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of `h` such that the given researcher has published at least `h` papers that have each been cited at least `h` times.

### Examples

- **Example 1:**
  - **Input:** `citations = [3,0,6,1,5]`
  - **Output:** `3`
  - **Explanation:** 
    - The researcher has 5 papers in total, with the citation counts `[3,0,6,1,5]`.
    - The researcher has 3 papers with at least 3 citations each, and the remaining two papers have no more than 3 citations each.
    - Therefore, the h-index is `3`.

- **Example 2:**
  - **Input:** `citations = [1,3,1]`
  - **Output:** `1`
  - **Explanation:** 
    - The researcher has 3 papers with the citation counts `[1,3,1]`.
    - The researcher has 1 paper with at least 1 citation.
    - Therefore, the h-index is `1`.

### Constraints

- `n == citations.length`
- `1 <= n <= 5000`
- `0 <= citations[i] <= 1000`

## Approach

The problem can be solved using a **count sort-based approach**. The main idea is to count the number of papers that have a certain number of citations and use this information to determine the h-index.

### Steps

1. **Initialize Count Array:**
   - Create a count array `countSort` of size `n+1`, where `n` is the number of papers. This array will store the number of papers with `i` citations, where `i` ranges from `0` to `n`.

2. **Populate Count Array:**
   - Iterate through the `citations` array. For each citation count, update the `countSort` array. If the citation count is greater than `n`, increment the count at index `n` (since a paper with more than `n` citations can contribute to the h-index).

3. **Determine the H-Index:**
   - Iterate through the `countSort` array in reverse order (from `n` down to `0`). Accumulate the counts, and check if the accumulated count is greater than or equal to the current index. If it is, that index is the h-index.

4. **Return the Result:**
   - Return the h-index when the condition is met.

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of papers. The algorithm iterates through the list of citations twice, once to populate the count array and once to determine the h-index.
  
- **Space Complexity:** O(n). The algorithm uses a count array of size `n+1`.

## Source

This problem is sourced from [LeetCode](https://leetcode.com). The solution provided here is my implementation and understanding of the problem and its solution.