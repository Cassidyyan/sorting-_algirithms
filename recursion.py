def recursion(n):
    if (n < 1):
        return
    else:
        print(n, end=" ")
        recursion(n - 1)
        print(n, end=" ")
        return

n = 4
recursion(n)