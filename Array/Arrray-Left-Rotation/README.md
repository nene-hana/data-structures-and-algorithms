# Left Rotation of an Array
Arrays | Python
<img width="885" height="942" alt="image" src="https://github.com/user-attachments/assets/418c2823-07e9-430f-8654-6e094918f2ac" />


# Problem

Given an array, rotate the array to the left by `d` positions.

A left rotation means:
- remove elements from the front
- move them to the back

---

# Example

| Input | Output |
|---|---|
| nums = [1,2,3,4,5], d = 2 | [3,4,5,1,2] |

---

# Explanation

Original array:

```python
[1,2,3,4,5]
```

Rotate left once:

```python
[2,3,4,5,1]
```

Rotate left twice:

```python
[3,4,5,1,2]
```

Final answer:

```python
[3,4,5,1,2]
```

---

# Solution 1 — Manual Rotation Using pop() and append()
 This is a brute force method and the logic I came up with

---

# How it works

This solution rotates the array one step at a time.

Each loop:

```python
pop(0)
```

removes the first element.

Then:

```python
append(first)
```

adds it to the end.

This simulates left rotation.

---

# Solution 2 — Using Array Slicing (Efficient)

It's optimal and standard solution

---

# How it works

The array is split into two parts.

Example:

```python
nums = [1,2,3,4,5]
d = 2
```

First part:

```python
nums[:d]
```

gives:

```python
[1,2]
```

Second part:

```python
nums[d:]
```

gives:

```python
[3,4,5]
```

Now combine in reverse order:

```python
[3,4,5] + [1,2]
```

Final result:

```python
[3,4,5,1,2]
```

---


# Core Pattern

```text
remove front → add to back
```

OR

```text
split array → swap order
```

---


# Constraints

```python
1 <= n <= 10^5
1 <= d <= 10^5
```

---

# What I Learned

- Difference between modifying a list safely vs unsafe index modification
- `pop(0)` always removes current first element
- `append()` adds to end
- `range(d)` means repeat d times, not loop through array
- `nums[i]` changes meaning if indexes shift after pop()
- Array slicing can solve rotation elegantly
- Modulo helps handle large rotations efficiently
