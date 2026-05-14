# 1365. How Many Numbers Are Smaller Than the Current Number
LeetCode Easy | Arrays | Python
<img width="1482" height="743" alt="image" src="https://github.com/user-attachments/assets/e52b164a-8bcd-4a7c-8bbd-645fa2126f63" />


# Problem

Given an array `nums`, for each element `nums[i]`, count how many numbers in the array are smaller than it.

Return the counts in a new array.

---

# Examples

## Example 1

Input:
```python
nums = [8,1,2,2,3]
```

Output:
```python
[4,0,1,1,3]
```

Explanation:
- `8` has four smaller numbers → `1,2,2,3`
- `1` has zero smaller numbers
- `2` has one smaller number → `1`
- `2` has one smaller number → `1`
- `3` has three smaller numbers → `1,2,2`

---

## Example 2

Input:
```python
nums = [6,5,4,8]
```

Output:
```python
[2,1,0,3]
```

---

## Example 3

Input:
```python
nums = [7,7,7,7]
```

Output:
```python
[0,0,0,0]
```

---

# Approach - Brute Force

For every number:
- compare it with every other number
- count how many are smaller

This uses nested loops.

---


# Dry Run

Input:
```python
nums = [8,1,2,2,3]
```

---

# First Iteration

```python
i = 0
nums[i] = 8
```

Compare with all elements:

```python
1 < 8  → yes
2 < 8  → yes
2 < 8  → yes
3 < 8  → yes
```

Count:
```python
4
```

ans:
```python
[4]
```

---

# Second Iteration

```python
i = 1
nums[i] = 1
```

No smaller numbers exist.

Count:
```python
0
```

ans:
```python
[4,0]
```

---

# Third Iteration

```python
i = 2
nums[i] = 2
```

Only:
```python
1 < 2
```

Count:
```python
1
```

ans:
```python
[4,0,1]
```

---

# Continue similarly

Final result:
```python
[4,0,1,1,3]
```

---

# Important Concepts Used

## Nested Loops

Outer loop:
```python
for i in range(len(nums))
```

Chooses current number.

Inner loop:
```python
for j in range(len(nums))
```

Compares against all numbers.

---

# Comparison

```python
nums[j] < nums[i]
```

Checks:
```python
Is current comparison number smaller?
```

---



# Pattern Learned

- Arrays
- Nested Loops
- Counting
- Brute Force Comparison
