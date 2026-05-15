# 1431. Kids With the Greatest Number of Candies
---
LeetCode Easy | Arrays | Python
<img width="1202" height="770" alt="image" src="https://github.com/user-attachments/assets/f49923fa-6890-4b51-adde-7bd10d4de27e" />


## Problem

Given an array `candies` where each element represents the number of candies a kid has, and an integer `extraCandies`.

Return a boolean list where:
- `True` means the kid can have the greatest number of candies after receiving all extra candies.
- `False` means they cannot.

---

## Example

### Input
```python
candies = [2,3,5,1,3]
extraCandies = 3
```

### Output
```python
[True, True, True, False, True]
```

---

## Approach

1. Find the maximum candies among all kids.
2. Loop through each kid.
3. Add `extraCandies` to the current kid's candies.
4. Compare it with the maximum value.
5. Store `True` or `False` in the result list.

---

## Solution

```python
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        greatest = max(candies)

        result = []

        for i in candies:
            if i + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)

        return result
```

---

## Time Complexity

```python
O(N)
```

- The loop runs once through the array.

---

## Space Complexity

```python
O(N)
```

- Result list stores boolean values for every kid.

---
*This is an efficient and optimal approach for this problem, reaching an `O(N)` solution for this problem*


<img width="796" height="690" alt="image" src="https://github.com/user-attachments/assets/9fb31bf8-0c35-4e11-95af-69967f74a70b" />

