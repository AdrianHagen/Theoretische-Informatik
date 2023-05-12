def collatz(a, b, n):
    global call_count
    call_count+=1
    if call_count > 200:
        return 0

    if n == 1:
        return True
    elif n%2==0:
        res = n/2
    else:
        res = a * n + b

    if res == 1:
        return True
    else:
        return collatz(a, b, res)

res = []
idx = 1
call_count = 0
while idx <= 20:
    if collatz(3, 7, idx) == True:
        res.append(idx)
    idx+=1
    call_count=0

print(res)