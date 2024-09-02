# LeetCode Problem: Reverse Words in a String

## Problem Description

Given an input string `s`, reverse the order of the words. A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space. The goal is to return a string of the words in reverse order concatenated by a single space.

Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words and should not include any extra spaces.

### Examples

- **Example 1:**
  - **Input:** `s = "the sky is blue"`
  - **Output:** `"blue is sky the"`

- **Example 2:**
  - **Input:** `s = "  hello world  "`
  - **Output:** `"world hello"`
  - **Explanation:** Your reversed string should not contain leading or trailing spaces.

- **Example 3:**
  - **Input:** `s = "a good   example"`
  - **Output:** `"example good a"`
  - **Explanation:** You need to reduce multiple spaces between two words to a single space in the reversed string.

### Constraints

- `1 <= s.length <= 10^4`
- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
- There is at least one word in `s`.

### Follow-Up

If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

## Approach

The solution utilizes Python's string manipulation capabilities to efficiently reverse the order of words in the string. It handles the elimination of extra spaces by using the split and join string methods.

### Steps

1. **Reverse the Entire String:**
   - The string `s` is reversed to bring the words into an approximately correct order but each word is individually backwards.

2. **Split and Reverse Each Word:**
   - The reversed string is split into words, stripping out extra spaces. Each word is then reversed again to correct its orientation.

3. **Concatenate the Words:**
   - The correctly oriented words are concatenated with a single space separating them to form the final output string.

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of the string. This encompasses reversing the string and processing each character during splitting and joining.
- **Space Complexity:** O(n), due to the space needed for the split words and the final output string.

## Source

This problem is sourced from [LeetCode](https://leetcode.com). The solution provided here is my implementation and understanding of the problem and its solution.