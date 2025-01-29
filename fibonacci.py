def     fibonacci(n):
    a=0;b=1 
    for i in range(2,n+1): 
        b=a+b
        temp = b  
        a=temp
    return b  

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1])
    print(fibonacci(n))  