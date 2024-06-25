import sys 

def numbers(end, start=0):
    print(start)
    
    # if start == end:
    #     return 1000
    start += 1

    return numbers(end, start=start)
 
# Set the stack size to 10000 
sys.setrecursionlimit(10001)

print(numbers(3))
