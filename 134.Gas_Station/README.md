# LeetCode Problem: Gas Station

## Problem Description

There are `n` gas stations along a circular route, where the amount of gas at the `i`th station is represented by `gas[i]`. You have a car with an unlimited gas tank, and it costs `cost[i]` amount of gas to travel from the `i`th station to its next `(i + 1)`th station.

You begin the journey with an empty tank at one of the gas stations. Your task is to find the starting gas station's index from which you can complete the circuit once in a clockwise direction. If it is not possible to complete the circuit, return `-1`.

### Examples

- **Example 1:**
  - **Input:** `gas = [1,2,3,4,5]`, `cost = [3,4,5,1,2]`
  - **Output:** `3`
  - **Explanation:** 
    - Start at station 3, where your tank gets filled with 4 units of gas.
    - Travel to station 4 (cost: 1), then to station 0 (cost: 2), then to station 1 (cost: 3), then to station 2 (cost: 4), and back to station 3.
    - You'll be able to complete the circuit starting at station 3.

- **Example 2:**
  - **Input:** `gas = [2,3,4]`, `cost = [3,4,3]`
  - **Output:** `-1`
  - **Explanation:** 
    - No matter which station you start from, you cannot complete the circuit. Thus, the output is `-1`.

### Constraints

- `n == gas.length == cost.length`
- `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 10^4`

## Approach

The problem is solved using a **greedy approach**. The goal is to find the correct starting point for the trip such that the total gas left is non-negative after every step.

### Steps

1. **Initial Check:** 
   - Check if the total gas is greater than or equal to the total cost. If not, return `-1` immediately, as completing the circuit is impossible.

2. **Greedy Search:** 
   - Traverse each station and calculate the current gas balance after subtracting the cost of traveling to the next station.
   - Keep track of the total gas deficit. If at any point, the total gas balance becomes negative, reset the starting station to the next station and reset the balance.
   - After traversing all stations, the last saved starting station is the answer.

3. **Return Result:** 
   - Return the starting station index if a solution exists; otherwise, return `-1`.

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of gas stations. We traverse through the gas stations once, calculating the balance at each step.
  
- **Space Complexity:** O(1). The algorithm only uses a constant amount of extra space for storing variables such as the total balance and the index of the starting station.


## Source

This problem is sourced from [LeetCode](https://leetcode.com). The solution provided here is my implementation and understanding of the problem and its solution.