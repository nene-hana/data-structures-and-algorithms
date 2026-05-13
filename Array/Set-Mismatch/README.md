# 645. Set Mismatch
LeetCode Easy | Arrays, Hashing(Set) | Python
<img width="1741" height="714" alt="image" src="https://github.com/user-attachments/assets/9f335b46-7e29-4f54-a5e2-6f6ca82a5222" />


# Problem

You have a set of integers from `1` to `n`.

Due to an error:
- one number appears twice
- one number is missing

Return:
```python
[duplicate, missing]
```

---

# Examples

## Example 1

Input:
```python
nums = [1,2,2,4]
```

Output:
```python
[2,3]
```

Explanation:
- `2` appears twice
- `3` is missing

---

## Example 2

Input:
```python
nums = [1,1]
```

Output:
```python
[1,2]
```

---

# Concept Used - Set

A `set` in Python:
- stores only unique values
- automatically removes duplicates
- allows fast lookup

Example:
```python
nums = [1,2,2,3]

print(set(nums))
```

Output:
```python
{1,2,3}
```

The duplicate `2` disappears.

---

# Approach

## Step 1
Use a set to track numbers already seen.

If a number already exists in the set:
- it is the duplicate number.

---

## Step 2
Create the expected set:
```python
{1,2,3,...,n}
```

---

## Step 3
Find missing number using set difference:
```python
expected - seen
```

---

# Solution

```python
class Solution:
    def findErrorNums(self, nums):
        seen = set()
        duplicate = -1

        for n in nums:
            if n in seen:
                duplicate = n

            seen.add(n)

        expected = set(range(1, len(nums) + 1))

        missing = list(expected - seen)[0]

        return [duplicate, missing]
```

---


# Pattern Learned

- Arrays
- Hashing
- Set Lookup
- Duplicate Detection
