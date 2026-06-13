def find_sum(n):
    
    if n == 0:
        return 0

    return n + find_sum(n - 1)

print(find_sum(5))