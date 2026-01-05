# 1️⃣ Time Complexity

**Definition:** Time Complexity measures how fast your code runs as input size (n) grows.
- Input size = n (number of elements)
- Count of basic operations relative to n

**Think of it like this: If 1 million items arrive, will your solution take 1 second or 1 year?**

**Big O Notation (common cases):**

| Big O      | Name           | Example                                 | Notes                                    |
|------------|----------------|-----------------------------------------|------------------------------------------|
| O(1)       | Constant       | Accessing arr[5]                        | Always same time, independent of input   |
| O(n)       | Linear         | for i in arr: print(i)                  | Time grows proportionally with input     |
| O(n²)      | Quadratic      | for i in arr: for j in arr: print(i,j)  | Time grows fast with nested loops        |
| O(log n)   | Logarithmic    | Binary search in sorted array           | Efficient; halves problem each step      |
| O(n log n) | Linearithmic   | Merge sort, Quick sort                  | Fast for large arrays                    |
| O(2^n)     | Exponential    | Recursion generating all subsets        | Terrible for large n                     |

## Code Examples

### O(1) — Constant Time
```python
x = arr[0]

**Analogy:**  
- Time Complexity = how long a chef takes to cook n dishes.
- Space Complexity = how much counter space the dishes take.

**Note:** Constants are ignored (O(2n) → O(n)) because we focus on **growth trend** as n becomes large.