def findempty(arr):
    for i in range(len(arr) - 1):
        if arr[i] == '(' and ( "(" not in arr[i:] or '[' not in arr[i:]) and ')' in arr[i:]:
            b = arr[i:]
            j = b.index(')') + i
            if len(arr[i:j]) == 1: 
                return i, j
        elif arr[i] == '[' and ( "(" not in arr[i:] or '[' not in arr[i:]) and ']' in arr[i:]:
            b = arr[i:]
            j = b.index(']') + i
            if len(arr[i:j]) == 1:
                return i, j
def check(arr):
    if not findempty(arr):
        if len(arr) == 0:
            return True
        else:
            return False
    else:
        i, j = findempty(arr)
        arr.pop(j)
        arr.pop(i)
        check(arr)

arr = ['(', '[', ')']
print(check(arr))