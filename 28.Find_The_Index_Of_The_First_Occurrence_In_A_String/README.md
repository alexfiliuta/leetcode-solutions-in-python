# LeetCode Problem: Find the Index of the First Occurrence in a String

## Problem Description

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or -1 if `needle` is not part of `haystack`.

### Examples

- **Example 1:**
  - **Input:** `haystack = "sadbutsad", needle = "sad"`
  - **Output:** `0`
  - **Explanation:** "sad" occurs at index 0 and 6. The first occurrence is at index 0.

- **Example 2:**
  - **Input:** `haystack = "leetcode", needle = "leeto"`
  - **Output:** `-1`
  - **Explanation:** "leeto" did not occur in "leetcode".

### Constraints

- `1 <= haystack.length, needle.length <= 10^4`
- Both `haystack` and `needle` consist of only lowercase English characters.

## Approach

This solution uses the **Knuth-Morris-Pratt (KMP) Algorithm**, which improves the worst-case time complexity for substring searches. The core idea is to build a prefix table that helps in skipping unnecessary comparisons in the haystack after a mismatch.

### Steps

1. **Build Prefix Table:** Compute the longest proper prefix which is also a suffix for all prefixes of the needle.
2. **Search in Haystack:** Use the prefix table to skip unnecessary comparisons when a mismatch occurs, by using the information of previous character matches.

## Complexity Analysis

- **Time Complexity:** O(m + n), where `m` is the length of `haystack` and `n` is the length of `needle`. This is due to the linear time required to both build the prefix table and execute the search.
- **Space Complexity:** O(n), where `n` is the length of `needle`, for storing the prefix table.

## Source

This problem is sourced from [LeetCode](https://leetcode.com). The solution provided here is my implementation and understanding of the problem and its solution.

