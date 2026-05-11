def reverseArray(arr):
    reversed_list= arr[::-1]
    result = ' '.join(map(str,reversed_list))
    return result



num=int(input())
arr = list(map(int, input().strip().split()))
print(reverseArray(arr))
