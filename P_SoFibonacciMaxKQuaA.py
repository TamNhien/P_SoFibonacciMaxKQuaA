A = int(input("Nhập số A: "))
fib_prev, fib_curr = 1, 1

while fib_curr <= A:
    fib_prev, fib_curr = fib_curr, fib_curr + fib_prev

print("Số Fibonacci lớn nhất nhưng không vượt quá A là : ", fib_prev)

