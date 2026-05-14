# 1071. Greatest Common Divisor of Strings
LeetCode Easy | Strings, Math | Python
<img width="996" height="827" alt="image" src="https://github.com/user-attachments/assets/eabdf39d-0a9c-4ee8-9401-483e4f54fe28" />


# Problem

For two strings `s` and `t`, we say:

```python
t divides s
```

if `s` can be formed by repeating `t` multiple times.

Return the largest string that divides both `str1` and `str2`.

If no such string exists, return:
```python
""
```

---

# Examples

## Example 1

Input:
```python
str1 = "ABCABC"
str2 = "ABC"
```

Output:
```python
"ABC"
```

Explanation:
```python
"ABCABC" = "ABC" + "ABC"
```

---

## Example 2

Input:
```python
str1 = "ABABAB"
str2 = "ABAB"
```

Output:
```python
"AB"
```

Explanation:
```python
"ABABAB" = "AB" + "AB" + "AB"
"ABAB" = "AB" + "AB"
```

---

## Example 3

Input:
```python
str1 = "LEET"
str2 = "CODE"
```

Output:
```python
""
```

No common repeating pattern exists.

---

# Concept

This problem is similar to finding the GCD (Greatest Common Divisor) of numbers.

Example:
```python
gcd(6,4) = 2
```

Because:
```python
2 divides both 6 and 4
```

Similarly for strings:
- find largest repeating pattern
- that can build BOTH strings

---



# Pattern Learned

- String Patterns
- GCD Concept
- String Concatenation
- Mathematical Observation
