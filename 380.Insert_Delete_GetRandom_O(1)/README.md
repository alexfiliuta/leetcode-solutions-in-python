# LeetCode Problem: Insert Delete GetRandom O(1)

## Problem Description

Implement the `RandomizedSet` class:

- `RandomizedSet()` Initializes the `RandomizedSet` object.
- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns true if the item was not present, false otherwise.
- `bool remove(int val)` Removes an item `val` from the set if present. Returns true if the item was present, false otherwise.
- `int getRandom()` Returns a random element from the current set of elements. It's guaranteed that at least one element exists when this method is called, and each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.

### Examples

- **Example 1:**
  - **Input:** `["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]`
  - **Output:** `[null, true, false, true, 2, true, false, 2]`
  - **Explanation:**
    ```
    RandomizedSet randomizedSet = new RandomizedSet();
    randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
    randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
    randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
    randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
    randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
    randomizedSet.insert(2); // 2 was already in the set, so return false.
    randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
    ```

### Constraints

- `-2^31 <= val <= 2^31 - 1`
- At most `2 * 10^5` calls will be made to insert, remove, and getRandom.
- There will be at least one element in the data structure when getRandom is called.

## Approach

The solution is implemented using a combination of a list and a hash map to maintain O(1) time complexity for insertion, deletion, and accessing a random element. The list holds the elements, while the hash map stores the indices of these elements within the list.

### Steps

1. **Initialization:**
   - Create a hash map and a list to store the elements and their indices.

2. **Insert Element:**
   - Check if the element is not in the hash map for uniqueness, then add the element to the list and its index to the hash map.

3. **Remove Element:**
   - If the element exists, swap it with the last element in the list and update the hash map, then remove the last element from the list and delete the element from the hash map.

4. **Get Random Element:**
   - Return a random element from the list using Python's `random.choice` method.

### Complexity Analysis

- **Time Complexity:** O(1) for each operation on average due to direct index access in a list and hash map operations.
- **Space Complexity:** O(n), where `n` is the number of elements in the `RandomizedSet`. The space is used by the list and the hash map.

## Source

This problem is sourced from [LeetCode](https://leetcode.com). The solution provided here is my implementation and understanding of the problem and its solution.
