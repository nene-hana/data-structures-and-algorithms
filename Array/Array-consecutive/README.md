# 485. Max Consecutive Ones

> LeetCode Easy | Arrays | Python
<img width="872" height="471" alt="image" src="https://github.com/user-attachments/assets/bf3b94ab-6c1f-41c5-8c3e-3d864a68a851" />

## Problem

Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.

## Examples

| Input | Output |
|-------|--------|
| `[1, 1, 0, 1, 1, 1]` | `3` |
| `[1, 0, 1, 1, 0, 1]` | `2` |

## Solution

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0
            max_count = max(max_count, count)
        return max_count
```

## How it works

Two variables do all the work:
- `count` : current streak of 1s right now
- `max_count` : best streak seen so far

Loop through every number:
- if `1` → extend the streak (`count + 1`)
- if `0` → reset the streak (`count = 0`)
- every step → update best if current streak is bigger

`max_count` never goes down : even when `count` resets to 0, the best is preserved.

## Dry run

```
nums = [1, 1, 0, 1, 1, 1]

num=1 → count=1, max=1
num=1 → count=2, max=2
num=0 → count=0, max=2  ← streak broken, max stays
num=1 → count=1, max=2
num=1 → count=2, max=2
num=1 → count=3, max=3  ← new best

return 3 ✅
```

## Complexity

| | |
|--|--|
| Time | O(n) : single pass through the array |
| Space | O(1) : only two extra variables |

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`

## What I learned

- Track + reset pattern, `count` tracks current streak, resets on condition break
- `max_count = max(max_count, count)` preserves the best value across resets
- Space O(1) is possible when you only need to track running values, not store anything

---

*Also read for  more on : [Read Article](https://steps-to-tech-world.hashnode.dev)*

