# LeetCode Problem: Zigzag Conversion

## Problem Description

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR".

Write the code that will take a string and make this conversion given a number of rows.

### Examples

- **Example 1:**
  - **Input:** `s = "PAYPALISHIRING", numRows = 3`
  - **Output:** `"PAHNAPLSIIGYIR"`
  
- **Example 2:**
  - **Input:** `s = "PAYPALISHIRING", numRows = 4`
  - **Output:** `"PINALSIGYAHRPI"`
  - **Explanation:**
    ```
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
    ```

- **Example 3:**
  - **Input:** `s = "A", numRows = 1`
  - **Output:** `"A"`

### Constraints

- `1 <= s.length <= 1000`
- `s consists of English letters (lower-case and upper-case), ',' and '.'.`
- `1 <= numRows <= 1000`

## Approach

The implementation involves creating an array of empty strings for each row and then iterating through the input string to place each character in the correct row based on the current direction of the zigzag pattern. The direction switches whenever the top or bottom of the pattern is reached.

### Steps

1. **Initialize Rows:**
   - Create an array of empty strings to represent each row.

2. **Assign Characters to Rows:**
   - Iterate through the string, assigning each character to the appropriate row based on the current position and direction of travel (up or down).

3. **Toggle Direction:**
   - Change the direction of assignment (up or down) when the top or bottom of the row set is reached.

4. **Combine Rows:**
   - Join all rows into a single string in the correct order.

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of the string. Each character is processed exactly once.
- **Space Complexity:** O(n), as extra space is used for the rows.

## Source

This problem is sourced from [LeetCode](https://leetcode.com). The solution provided here is my implementation and understanding of the problem and its solution.