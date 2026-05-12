# 1929. Concatenation of Array

> LeetCode Easy | Arrays | Python
> <img width="1358" height="885" alt="image" src="https://github.com/user-attachments/assets/5007ab97-5265-4bbf-8b6b-6bf41a365855" />


## Examples

| Input | Output |
|-------|--------|
| `[1, 2, 1]` | `[1, 2, 1, 1, 2, 1]` |
| `[1, 3, 2, 1]` | `[1, 3, 2, 1, 1, 3, 2, 1]` |

## Solution

```python
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums
```

## Let me show you how it works:

In Python, `+` on two lists concatenates them , so `nums + nums` directly produces the doubled array without any manual indexing or loops.

`nums * 2` is an equivalent one-liner.

## Constraints

- `1 <= n <= 1000`
- `1 <= nums[i] <= 1000`

## Key Topic

- List concatenation with `+` in Python


---


Also read for  more on : [Read Article](https://steps-to-tech-world.hashnode.dev)
