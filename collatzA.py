def collatz(a, b, n):
    global call_count
    call_count+=1

    if n%2==0:
        res = n/2
    else:
        res = a * n + b
    
    if res == 1:
        return call_count
    else:
        collatz(a, b, res)

call_count=0
collatz(3, 1, 27)
print(call_count)