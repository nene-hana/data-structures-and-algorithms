# Manual Rotation Using pop() and append() (BRUTE FORCE METHOD)
n =int(input())
d = int(input())

arr = list(map(int, input().split()))

for i in range(d):

    first = arr.pop(0)

    arr.append(first)

print(arr)


# Using Array Slicing (Efficient)
n =int(input())

d = int(input())

nums = list(map(int, input().split()))

d = d % len(nums)

result = nums[d:] + nums[:d]

print(result)

# insert either of the code to the function rotateLeft().
