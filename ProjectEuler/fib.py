def fib(arg_max_ith):
    f1, f2 = 0, 1
    while f1 < arg_max_ith:
        yield f1
        f1, f2 = f2, f1 + f2
        
if __name__ == "__main__":
    for elem in fib(10):
        print elem