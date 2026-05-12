# 1470. Shuffle the Array

> LeetCode Easy | Arrays | Python

<img width="1155" height="572" alt="image" src="https://github.com/user-attachments/assets/558e0de6-e454-4699-86c9-c822b839ca14" />

## Problem

Given an array `nums` of `2n` elements in the form `[x1, x2, ..., xn, y1, y2, ..., yn]`, return it shuffled as `[x1, y1, x2, y2, ..., xn, yn]`.

## Examples

| Input | n | Output |
|-------|---|--------|
| `[2, 5, 1, 3, 4, 7]` | 3 | `[2, 3, 5, 4, 1, 7]` |
| `[1, 2, 3, 4, 4, 3, 2, 1]` | 4 | `[1, 4, 2, 3, 3, 2, 4, 1]` |

## Solution

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result
```

## How it works

The array has two halves — `nums[0:n]` is the x values, `nums[n:]` is the y values.

Loop from `0` to `n-1` and pick one element from each half alternately:
- `nums[i]` → element from first half
- `nums[i + n]` → matching element from second half (`+n` shifts to the same position in second half)

Only loop `range(n)` — not the full array ,otherwise `nums[i + n]` goes out of bounds.



## Constraints

- `1 <= n <= 500`
- `nums.length == 2n`
- `1 <= nums[i] <= 1000`

## What I learned

- `nums[i + n]` pattern to access matching elements in the second half
- Why `range(n)` and not `range(len(nums))` — avoid index out of bounds
- Difference between `i` (index) and `nums[i]` (value at that index)

---

Also read for  more on : [Read Article](https://steps-to-tech-world.hashnode.dev)


