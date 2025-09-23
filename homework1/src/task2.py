def string (x) :
    return "hi"*x

def ints(x) :
    return len(string(x))

def floats(x) :
    return 0.5 * ints(x)

def bools(x) : 
    return floats(x) < 4 and ints(x) > 4

if __name__ == "__main__" :
    print(bools(10))
    print(floats(10))
    print(ints(2))
    print(string(2))