def fun(x, y):
    return x + y


if __name__ == "__main__":
    import random
    y = round(10*random.random())
    print(fun(5, y)) # fun will return same value for 5 and same y
